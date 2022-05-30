#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
import networkx as nx
import math
import random as rn
import numpy as np
import copy
import collections
import pandas as pds

 # def constructgraph(degree_sequence,oringinal_G):
   # n = len(degree_sequence)
  # if np.sum(degree_sequence) % 2 != 0:
    #    return None
   # G = nx.empty_graph(n)
    # transform list of degrees in list of (vertex, degree)
   # vd = [(v,d) for v,d in enumerate(degree_sequence)]
#节点类
class Node:
    def __init__(self,degree=None, degree_count=None):
        
        self.d=degree #节点度
        self.dc=degree_count#节点度的个数
        self.left = None #节点左孩子
        self.right = None #节点右孩子
        self.father = None # 节点父节点
        self.child=None
        
    # Q = queue.Queue()
    #判断是否是左孩子
    def is_left_child(self):
        return self.father.left == self

#创建最初的叶子节点
 
class HuffmanTree(object):

    #根据Huffman树的思想：以叶子节点为基础，反向建立Huffman树
    def PrintTree(self,data_set):
        
        self.a=[Node(part[0],part[1]) for part in data_set] 
        m=[]
        # self.root=self.a[-1]
        #根据输入的字符及其频数生成叶子节点
        # print(self.a)
        #以降序排列[(5,1),(4,2),(3,1),(2,2),(1,3)]
        for i,d in enumerate(self.a):
          m.append([self.a[i].d,self.a[i].dc])
        m.sort(key=lambda tup:tup[0],reverse=True)
        # print(m)
        b1=[]
        c=[]
        k=[]
        self.a.sort(key=lambda node:node.d,reverse=True)
        # print(len(self.a))
        if(len(self.a)%2!=0):
          # print("方案1",1)
          m.sort(key=lambda tup:tup[0],reverse=True)
          nn1=self.a.pop()
          k=self.get_tree1(self.a)
          last=m.pop()
          m.extend(k)
        else:
        #       print("方案2",2)
              # print(len(self.a))
           k=self.get_tree1(self.a)
           
           m.extend(k)
        return m
    def get_tree1(self,a):#get tree
        b1=[] 
         
        while len(self.a)!=1:
            
             
            if(self.a[0].dc>self.a[1].dc): 
                      # degree=self.a[0].d
                      degree=int(math.ceil(((self.a[1].dc*self.a[1].d)+(self.a[0].dc*self.a[0].d))/(self.a[0].dc+self.a[1].dc)))
            elif(self.a[0].dc<self.a[1].dc):
                       # degree=self.a[1].d
                      degree=int(math.floor(((self.a[1].dc*self.a[1].d)+(self.a[0].dc*self.a[0].d))/(self.a[0].dc+self.a[1].dc)))
            elif(self.a[0].dc==self.a[1].dc):
                 degree=int((self.a[0].d+self.a[1].d)/2)
            degree_count=(self.a[1].dc+self.a[0].dc)
            
            degree=int(degree)
             
            c=Node(degree,degree_count)
            c.left=self.a.pop(0)#c.left为队列的（5，1） 
            
            c.right=self.a.pop(0)#c.right为队列的（4，2）
             
           
            b1.append([c.d,c.dc])
            # b1.sort(key=lambda node:node.d,reverse=True) 
           
            self.a.append(c)
        if(len(self.a)%2!=0):
          self.a.sort(key=lambda node:node.d,reverse=True) 
        return b1
     

# if __name__=="__main__": 
#     # datafile = pds.read_csv("datasets/CA-HepTh.csv", header=None)
#     datafile = pds.read_csv("test.csv", header=None)
#     datafile=datafile.values
#     # print(datafile)#读取数据集
#     G=nx.Graph()
#     G.add_edges_from(datafile)
    
#     dv = [(d,v) for v, d in G.degree()]
#     # odered_degree_sequence=list(sorted([d for n, d in G.degree()],reverse=True))
#     orderdegree_sequence,permutation= zip(*dv)
#     # print("length:",len(permutation))
#     # print("orderdegree_sequence,permutation",orderdegree_sequence,"orderdegree_sequence,permutation",permutation)
#     degreeCount = collections.Counter(orderdegree_sequence)
#     data_set=degreeCount.items()
#     # data_set=[[5, 1], [4, 2], [3, 1], [2, 2]]
    
#     # print("data_set:",data_set)
#     attempt = 1
#     print("Attempt number",attempt)
#     tree=HuffmanTree()
#     anonymised_sequence =tree.PrintTree(data_set)
#     print(anonymised_sequence)
 
    
     


 