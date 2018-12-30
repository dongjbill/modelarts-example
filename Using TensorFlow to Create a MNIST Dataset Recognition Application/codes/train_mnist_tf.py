from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import os
from tensorflow.python.framework import graph_util
import moxing as mox

tf.flags.DEFINE_string('data_url', None, 'Dir of dataset')
tf.flags.DEFINE_string('train_url', None, 'Train Url')
tf.flags.DEFINE_integer('max_num_steps', 1000, 'training epochs')
tf.flags.DEFINE_boolean('is_training', True, 'train')

_S3_SECRET_ACCESS_KEY = (os.environ.get('SECRET_ACCESS_KEY', None)
                         or os.environ.get('S3_SECRET_ACCESS_KEY', None)
                         or os.environ.get('AWS_SECRET_ACCESS_KEY', None))
_S3_ACCESS_KEY_ID = (os.environ.get('ACCESS_KEY_ID', None)
                     or os.environ.get('S3_ACCESS_KEY_ID', None)
                     or os.environ.get('AWS_ACCESS_KEY_ID', None))

mox.file.set_auth(ak=_S3_ACCESS_KEY_ID, sk=_S3_SECRET_ACCESS_KEY)

flags = tf.flags.FLAGS

def main(*args):

  def train(data_url):
    mnist = input_data.read_data_sets(data_url, one_hot=True)

    image = tf.placeholder(tf.float32, [None, 784], name='input_image')
    label = tf.placeholder(tf.float32, [None, 10])

    W = tf.get_variable(name='W', initializer=tf.zeros([784, 10]))
    b = tf.get_variable(name='b', initializer=tf.zeros([10]))

    label_predict = tf.nn.softmax(tf.matmul(image, W) + b, name='label_predict')
    cross_entropy = -tf.reduce_sum(label * tf.log(label_predict))
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
    global_step = tf.train.get_or_create_global_step()

    correct_prediction = tf.equal(tf.argmax(label_predict, 1), tf.argmax(label, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

    with tf.control_dependencies([train_step]):
      inc_global_step = global_step.assign_add(1).op

    scaffold = tf.train.Scaffold(saver=tf.train.Saver(), )
    with tf.train.MonitoredTrainingSession(scaffold=scaffold,
                                           save_checkpoint_steps=50,
                                           checkpoint_dir=flags.train_url) as sess:

      for step in range(flags.max_num_steps):

        batch_xs, batch_ys = mnist.train.next_batch(64)
        sess.run(inc_global_step, feed_dict={image: batch_xs, label: batch_ys})
        if step % 10 == 0:
          cro, acc = sess.run([cross_entropy, accuracy], feed_dict={image: mnist.test.images, label: mnist.test.labels})
          print("Step:%03d\tcost:%.3f\taccuracy:%.3f" % (step, cro, acc))

  def freeze_graph(input_checkpoint, output_graph):
    output_node_names = 'label_predict'
    saver = tf.train.import_meta_graph(input_checkpoint + '.meta', clear_devices=True)
    graph = tf.get_default_graph()
    input_graph_def = graph.as_graph_def()

    with tf.Session() as sess:
      saver.restore(sess, input_checkpoint)
      output_graph_def = graph_util.convert_variables_to_constants(
        sess=sess,
        input_graph_def=input_graph_def,
        output_node_names=output_node_names.split(","))

      with tf.gfile.GFile(output_graph, "wb") as f:
        f.write(output_graph_def.SerializeToString())
      print("%d ops in the final graph." % len(output_graph_def.node))

  def freeze_graph_test(pb_path, image_path):

    with tf.Graph().as_default():
      output_graph_def = tf.GraphDef()
      with tf.gfile.GFile(pb_path, "rb") as f:
        output_graph_def.ParseFromString(f.read())
        tf.import_graph_def(output_graph_def, name="")
      with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        input_img_name = sess.graph.get_tensor_by_name('input_image:0')
        output_tensor_name = sess.graph.get_tensor_by_name('label_predict:0')
        image_raw = tf.gfile.FastGFile(image_path, 'rb').read()
        image = tf.image.decode_jpeg(image_raw).eval()
        image.resize((1, 784))
        out = sess.run(output_tensor_name, feed_dict={input_img_name: image})
        score = tf.nn.softmax(out, name='pre')
        class_id = tf.argmax(score, 1)
        print("Predict number is:{}".format(sess.run(class_id)))


  model_path = os.path.join(flags.train_url, 'model')
  output_graph = os.path.join(model_path, 'saved_model.pb')

  if flags.is_training:

    if tf.gfile.IsDirectory(model_path):
      tf.gfile.DeleteRecursively(model_path)
    tf.gfile.MkDir(model_path)

    train(data_url=flags.data_url)
    with tf.gfile.GFile(os.path.join(flags.train_url, 'checkpoint'), 'rb') as f:
      input_checkpoint = f.readline().split('"')[1]
    input_checkpoint = os.path.join(flags.train_url, input_checkpoint)
    freeze_graph(input_checkpoint, output_graph)

  else:
    test_image = [os.path.join(flags.data_url, img) for img in tf.gfile.ListDirectory(flags.data_url)]
    for image in test_image:
      freeze_graph_test(output_graph, image)

if __name__ == '__main__':
  tf.app.run(main=main)
