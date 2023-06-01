import py_trees
import json
import mybehaviour #自建的行为库

def Compositenode(name):
    if name == "Selector":
        return py_trees.composites.Selector("Selector")
    elif name == "Sequence":
        return py_trees.composites.Sequence("Sequence")

def create_tree(children,parent):
    for child in children:
        if child['name']=="Selector" or child['name']=="Sequence":
            node = Compositenode(child['name'])
            parent.add_child(node)
            if 'children' in child:
                create_tree(child['children'],node)
        else :
            node = eval("mybehaviour."+child['name'])(name=child['name'])# 根据json文件中的名字创建行为节点
            parent.add_child(node)
            if 'children' in child:
                create_tree(child['children'],node)

def mycreate():#创建行为树
    with open("my.json",'r',encoding='utf-8') as load_f:
        btree=json.load(load_f)
    btree = btree['root'] 
    root = Compositenode(btree['name'])
    if 'children' in btree :
        create_tree(btree['children'],root)
    return root
