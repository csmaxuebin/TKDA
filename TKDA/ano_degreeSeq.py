#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import networkx as nx
import numpy as np
import random as rn
import pandas as pds
import collections
import time
# import kdegree as kd
import tree as T 
import GraphConstruct as GC
class Node():
    # 节点类
    def __init__(self, data=-1,d=-1):
        self.data= data
        self.d=d
        self.left = None
        self.right = None
 
 
class Tree():
    # 树类
    def __init__(self):
        self.root = Node()
 
    def add(self, a,b):
        # 为树加入节点
        
        node = Node(a,b)
        
        if self.root.data== -1:  # 如果树为空，就对根节点赋值
            self.root =node
        else:
            mystack = []
            treeNode = self.root
            mystack.append(treeNode)
            while mystack:  # 对已有的节点进行层次遍历
                treeNode = mystack.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    return
                else:
                    mystack.append(treeNode.left)
                    mystack.append(treeNode.right)
           
             
    def DFS(self,root):#深度优先遍历核心代码""" 
        # k=int(input("请输入K值:"))
        if root == None:
            return 
        stack = [] 
        s=[]
        current_line = 0
        stack.append([current_line,root])
        while stack:
    
            line,now_node= stack.pop(0)
            # return now_node.d     
        # 核心判断：是否换行
            if line!=current_line:
                 print("")  # 不同时换行，print()函数默认end=“\n”
                 current_line = line
                 
            s.append([now_node.data,now_node.d])
            # pr int(now_node.d)
            # return stack.d 
            if now_node.left!= None:
                stack.append([line+1,now_node.left])  # 将左子节点入队
            if now_node.right!= None:
                stack.append([line+1,now_node.right]) # 将本右子节点入队
             
         
        return s
    def Seq(self,root,k):
     if root == None:
      return
     stack = []
       
     stack.append(root)
     b=[]
    
     while stack:
            now_node= stack.pop(0)

           
            m=[]
            n=[]
            if(now_node==None):
               return  None
            else:
             s=[]
            # print(type(now_node.d))
            if(now_node.d>=k):
              
                 # print("now_node",[now_node.data,now_node.d])
                 if(now_node.left ==None or now_node.right== None):
                   # print("bb",[now_node.data,now_node.d])
                   s.append([now_node.data,now_node.d])
              
                 elif(now_node.left.d!= None and now_node.right.d != None):
                  
                    
                  # print(now_node.data)
                      
                   if(now_node.left.d>=k and now_node.right.d>=k):
                       
                       stack.append(now_node.left)
                      
                       stack.append(now_node.right)
                       
                      
                   elif(now_node.left.d<k or now_node.right.d<k):
                       
                    
                     s.append([now_node.data,now_node.d])
           
                     
                 
              
            b.extend(s)
        
             
    
      
     return b
    def partion(self,deg):
      
      mm=[]
      nn1=[]
      f=[]
      
       
      deg_seq, p=zip(*deg)
      # print()
      seq=[i for i in deg_seq]
      d=[d for d in p]
       
      for i,j in enumerate(seq):
         
                
          f.append(j)
          mm=f*d[i]
          nn1.extend(mm)                     
          f.pop()
      nn1=sorted(nn1,reverse=True)
      
      return nn1
    def sort_dv(self,dv):
        dv.sort(reverse=True)
    # permutation holds the mapping between original vertex and degree-sorted vertices
        degree_sequence,permutation = zip(*dv)
        degree_sequence =list(degree_sequence)
    # print("degree_sequence:",degree_sequence,"permutation:",permutation)
        return degree_sequence,permutation
    def seq_partion(self,anonymised_sequence,G,k):
        odered_degree_sequence=sorted([d for n, d in G.degree()],reverse=True)
        degreeCount = collections.Counter(odered_degree_sequence)
        degreeCount=degreeCount.items()
        degreeCount=list(degreeCount)
    
        last=degreeCount[-1]
         
        mm=[]
        f=[]
        nn1=[]
       
        
        if(len(degreeCount)%2!=0): 
            print("***********1")
            
            print("需要改进的匿名len",len(anonymised_sequence))
            anon_seq=anonymised_sequence[-1]
            if(last[1]>=k):
      
              f.append(last[0])
              mm=f*last[1]
              nn1.extend(mm) 
              # print(len(nn1))
            else:
              f.append(anon_seq) 
              mm=f*last[1]
              nn1.extend(mm)
    
            anonymised_sequence.extend(nn1) 
        else:
         
          anonymised_sequence=anonymised_sequence
          
        return anonymised_sequence
    def probing(self,degree_sequence,noise):    
     
      a=degree_sequence.pop()
      a=a+noise
      degree_sequence.append(a)
      return degree_sequence
        
 