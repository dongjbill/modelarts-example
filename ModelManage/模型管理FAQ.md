### 错误提示1： 模型发布失败, 模型原位置不满足规范


**答：** 模型存储位置需要满足模型包规范，  比如我想发布ocr的模型，ocr模型在用户obs桶中按如下方式进行存储。 用户在页面发布模型时选择模型来源只需要选择到ocr目录（**注意:不是选择到model目录**）

        test_bucket(obs桶名)
                |
                |------ocr   (ocr模型一级目录)
                           |
                           |------model （目录名需要固定）
                                        |
                                        |-----config.json （必须：模型配置文件，名字固定）
                                        |
                                        |-----customize_service.py(可选： 模型推理代码，如果有名字必须固定)
                                        |
                                        |------模型pb 权重等文件
                                        
### 错误提示2：获取模型配置文件错误,请检查路径是否存在配置文件
**答：** 按照上述例子所示， 请用户自己检查下model目录下是否存在config.json文件，该文件需要模型开发者按照模型配置文件规范自己编写config.json，放置在model目录下

### 错误提示3：界面提示参数无效
**答：** 模型名称、模型版本、模型类型、模型描述信息、模型发布路径等参数校验不符合规则时，统一返回ModelArts.0101无效参数。

----------
| 参数名 | 示例|参数校验规则说明 |
|:--------:|:------:|:------:|
| 模型名称 | model_1 |支持1-48位包含中文、英文字母大小写、数字、中划线(-) 、下划线(_)的可见字符，只能以中英文字符开头 | 
| 模型版本 |0.0.1| 版本格式为“数值.数值.数值”，其中数值为1-2位正整数，两位数字表示时不支持0开头，例如01 |
| 模型类型 | Caffe|取值为TensorFlow/ MXNet/ Caffe/ Spark_MLlib/ Scikit_Learn/ XGBoost/ MindSpore/Image|
| 模型描述 |This  model is used for object_detection.| 模型描述信息，不超过100个字符 |
| 模型路径 |https://test-model.obs.myhwclouds.com/XGBoost|模型发布路径必须为model目录的上一层。<br>例中test-model为模型所在的obs桶，XGBoost为模型model目录的上一层；发布模型时请参考[模型包规范](https://github.com/huawei-clouds/modelarts-example/blob/master/ModelManage/%E6%A8%A1%E5%9E%8B%E5%8C%85%E8%A7%84%E8%8C%83.md)|

### 错误提示4：ModelArts训练作业完成后，导入模型时报错，无法完成模型的导入
**答：** 由于模型管理模块升级，旧的训练作业生成的模型文件不满足当前模型包规范，可以采用以下两种方式解决:
- 方法一： 重新创建训练作业，训练完成后再执行导入模型操作。
- 方法二： 添加模型配置文件config.json，详细步骤如下：
1. 请参考[模型配置文件详解](https://github.com/huawei-clouds/modelarts-example/blob/master/ModelManage/%E6%A8%A1%E5%9E%8B%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E8%AF%A6%E8%A7%A3.md)编写config.json（名称命名为config，格式为.json）
1. 将编写好的config.json文件上传至OBS桶中（上传至训练作业输出文件下的model文件夹内），比如训练作业输出OBS路径为/ test_bucket/ocr

        test_bucket(obs桶名)
                |
                |------ocr   (ocr模型一级目录)
                           |
                           |------model （目录名需要固定）
                                        |
                                        |-----config.json （必须：模型配置文件，名字固定）
                                        |
                                        |-----customize_service.py(可选： 模型推理代码，如果有名字必须固定)
                                        |
                                        |------模型pb 权重等文件
