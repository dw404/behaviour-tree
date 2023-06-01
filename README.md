# 无人机集群博弈仿真行为树模块

## 将静态画好的行为树json文件转变为对应行为代码的动态执行

* 行为树库py_trees的文档：https://py-trees.readthedocs.io/en/release-0.6.x/index.html  

* 自己创建的行为需要继承自库中的行为类

* behavior3editor.Setup.0.1.9是画行为树的软件，项目地址：https://github.com/zhandouxiaojiji/behavior3editor

  使用方法：
  
  	1.打开编辑器
  	2.工作区->节点定义->选择文件(json)
  	3.工作区->选择目录(指定行为树所在的目录)
  	4.工作区->另存为(将工作区保存起来，以便下次打开)
  	5.行为树->新建

* json2code.py：解析json文件

* mybehaviour.py：自己定义的行为动作

* tree.py:行为树的实际执行代码，根据文档中py_trees.demos.selector改编



