# TKDA

算法1

本代码是论文<TKDA: An Improved Method for K-degree Anonymity in Social Graphs>的源码实现。

本代码将度序列转换为二元组，构成生成树，再通过DF遍历确定分区节点，最后通过随机边操作生成匿名图。（随机边操作源代码来源于2017 UMGA算法）

运行环境： Python with Intel Core i5 CPU 1.8 GHz and 8 GB RAM, running MacBook。

包                      版本

numpy                  1.19.2

collections            1.2.1

random                 1.1.1

pandas                 1.1.3

networkx               2.5

math                   1.1.0

GraphConstruct函数是对边进行操作，生成匿名图

Tree函数根据原始度序列生成树，并在GraphConstruct中作为包导入

get_tree1函数是生成树

ano_degreeSeq 通过DFS遍历确定最终的匿名度序列，并在GraphConstruct中作为包导入

probing函数用于添加噪声

edgeDeletion 删除边

edgeAddition 添加边

edgeSwitch   交换边

程序运行结果：

![image](https://user-images.githubusercontent.com/104848157/170966582-ac1ac85c-a53c-4cb8-bc22-7f3eb6becd59.png)


