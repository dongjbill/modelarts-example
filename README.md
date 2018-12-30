# ModelArts案例指南

###  **案例 1**  &#160; &#160;[Using MXNet to Create a MNIST Dataset Recognition Application](https://github.com/huawei-clouds/modelarts-example/tree/master/Using%20MXNet%20to%20Create%20a%20MNIST%20Dataset%20Recognition%20Application)

本案例介绍在“[华为云ModelArts](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/dashboard)”平台如何使用MXNet实现MNIST数据集的手写数字图像识别应用。通过进入ModelArts平台的“[训练作业](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/trainingjobs/)” 界面创建训练作业，完成模型训练，之后 “[导入模型](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/models)”，“[部署上线](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/webservice/real-time)”，发起预测请求完成预测。

基本流程包含以下步骤：

1. **准备数据**：下载数据集，解压后上传至OBS桶中。
2. **训练模型**：使用MXNet原生接口编写模型训练脚本，新建训练作业进行模型训练。
3. **部署模型**：得到训练好的模型文件后，新建预测作业将模型部署为在线预测服务。
4. **发起预测请求**：发起预测请求获取预测结果。

###  **案例 2**  &#160; &#160;[Using MoXing to Create a Iceberg Images Classification Application](https://github.com/huawei-clouds/modelarts-example/tree/master/Using%20MoXing%20to%20Create%20a%20Iceberg%20Images%20Classification%20Application)

本案例介绍如何在“[华为云ModelArts](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/dashboard)”平台上使用MoXing实现Kaggle竞赛中的冰山图像分类任务。实验所使用的图像为雷达图像，需要参赛者利用算法识别出图像中是冰山（iceberg）还是船（ship）。通过进入ModelArts平台的“[训练作业](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/trainingjobs/)”界面创建训练作业，完成模型训练，之后创建一个预测作业，加载模型参数，获取预测结果。

基本流程包含以下步骤：

1. **准备数据**：下载数据集并上传至华为云OBS桶中，编写代码将数据集格式转换成TFRecord。
2. **训练模型**：使用MoXing API编写用实现冰山图像分类的网络模型，新建训练作业进行模型训练。
3. **预测结果**：再次新建训练作业，对test数据集进行预测，并将结果保存到csv文件。
4. **查看结果**：将预测结果的csv文件提交到Kaggle官网后获取分类结果。


###  **案例 3**  &#160; &#160;[Using MoXing to Create a MNIST Dataset Recognition Application](https://github.com/huawei-clouds/modelarts-example/tree/master/Using%20MoXing%20to%20Create%20a%20MNIST%20Dataset%20Recognition%20Application)

本案例介绍在“[华为云ModelArts](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/dashboard)”平台如何使用MoXing实现MNIST数据集的手写数字图像识别应用。通过进入ModelArts平台的“[训练作业](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/trainingjobs/)” 界面创建训练作业，完成模型训练，之后 “[导入模型](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/models)”，“[部署上线](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/webservice/real-time)”，发起预测请求完成预测。

基本流程包含以下步骤：

1. **准备数据**：下载文本数据集，上传至OBS桶中。
2. **训练模型**：使用MoXing框架编模型训练脚本，新建训练作业进行模型训练。
3. **部署模型**：得到训练好的模型文件后，新建预测作业将模型部署为在线预测服务。
4. **发起预测请求**：发起预测请求获取预测结果。

###  **案例 4**  &#160; &#160;[Using ModelArts to Create a Bank Marketing Application](https://github.com/huawei-clouds/modelarts-example/tree/master/Using%20ModelArts%20to%20Create%20a%20Bank%20Marketing%20Application)

本案例介绍在“[华为云ModelArts](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/dashboard)”平台如何根据客户特征（年龄、工作类型、婚姻状况、文化程度、是否有房贷和是否有个人贷款），预测客户是否愿意办理定期存款业务。通过进入ModelArts平台的“[自动学习](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/autoML)”界面创建“**预测分析模型**”并启动"训练作业"。训练作业运行完成后，即可发布模型成预测服务。

基本流程包含以下步骤：

1. **准备数据**：下载文本数据集，上传至OBS桶中。
2. **训练模型**：使用ModelArts服务，新建训练作业进行模型训练。
3. **发布预测**：将训练好的模型发布，并测试预测结果。

###  **案例 5**  &#160; &#160;[Using ModelArts to Create a Yunbao Detection Model](https://github.com/huawei-clouds/modelarts-example/tree/master/Using%20ModelArts%20to%20Create%20a%20Yunbao%20Detection%20Model)

聪明可爱的“云宝”是华为云的吉祥物。本样例将详细介绍怎样用自动学习方法和预置算法快速生成云宝检测模型。通过使用ModelArts平台的“[自动学习](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/autoML)”界面的“**物体检测**”功能，智能生成“云宝”检测模型；以及使用ModelArts平台的“[训练作业](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/trainingjobs/)”界面的“**预置算法**”功能生成“云宝”检测模型。

基本流程包含以下步骤：

1. **使用自动学习实现云宝检测模型**
2. **使用预置模型实现云宝检测模型**

###  **案例 6**  &#160; &#160;[Using Spark MLlib to Create a Precise Recommendation Application](https://github.com/huawei-clouds/modelarts-example/tree/master/Using%20Spark%20MLlib%20to%20Create%20a%20Precise%20Recommendation%20Application)

本案例介绍如何借助华为云ModelArts服务平台上的自动学习场景，为您提供精准营销的方向和辅助决策，提升消费品转化率和商家利润，改善消费者的消费体验。通过进入ModelArts平台的“[训练作业](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/trainingjobs/)” 界面创建训练作业，完成模型训练，之后 “[导入模型](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/models)”，“[部署上线](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/webservice/real-time)”，发起预测请求完成预测。


基本流程包含以下步骤：

1. **准备工作**：下载数据集、实例代码，然后上传至OBS桶中。
2. **训练模型**：编写基于Spark MLlib中ALS算法的模型训练脚本，新建训练作业进行模型训练。
3. **部署模型**：得到训练好的模型文件后，新建预测作业将模型部署为在线预测服务。
4. **验证模型**：下载并导入客户端工程，发起预测请求获取预测结果。

###  **案例 7**  &#160; &#160;[Using a Built-in Model to Create a Flower Images Classification Application](https://github.com/huawei-clouds/modelarts-example/tree/master/Using%20a%20Built-in%20Model%20to%20Create%20a%20Flower%20Images%20Classification%20Application)

本案例介绍在华为云ModelArts平台如何使用flowers数据集对预置的ResNet\_v1\_50模型进行重训练，快速构建花卉图像分类应用。通过使用ModelArts平台的“[训练作业](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/trainingjobs/)” 界面的“**预置算法**”功能创建训练作业，完成模型训练，之后 “[导入模型](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/models)”，“[部署上线](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/webservice/real-time)”，发起预测请求完成预测。


基本流程包含以下步骤：

1. **准备工作**：下载flowers数据集，并上传至华为云对象存储服务器（OBS）中。
2. **训练模型**：使用flowers训练集，对ResNet_v1_50模型重训练，得到新模型。
3. **部署模型**：将得到的模型，部署为在线预测服务。
4. **发起预测请求**：发起预测请求获取请求结果。


###  **案例 8**  &#160; &#160;Using TensorFlow to Create a MNIST Dataset Recognition Application

本案例介绍如何在“[华为云ModelArts](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/dashboard)”平台上使用TensorFlow实现MNIST数据集的手写数字图像识别应用。通过进入ModelArts平台的“[训练作业](https://console.huaweicloud.com/modelarts/?region=cn-north-1#/manage/trainingjobs/)”界面创建训练作业，完成模型训练，之后创建一个预测作业，加载模型参数，获取预测结果。

基本流程包含以下步骤：

1. **准备数据**：通过ModelArts市场预置数据集创建所需数据集版本。
2. **训练模型**：使用TensorFlow框架编模型训练脚本，新建训练作业进行模型训练。
3. **预测结果**：得到训练好的模型文件后，新建训练作业对test数据集进行预测，并输出预测结果。
