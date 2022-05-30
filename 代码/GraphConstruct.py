#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from collections import deque
import networkx as nx
import random as rn
import numpy as np
import copy
import collections
import pandas as pds
import time
 # import kdegree as kd
import tree as T  # bulid tree
import ano_degreeSeq as ano_dSeq  # 通过DFS遍历确定分区节点
nodesToAddEdge=[]
nodesToDeleteEdge=[]
# edgeDeletionNumTries = 0
edgeAdditionNumTries = 0
edgeSwitchNumTries = 0
# oneEdgeDeletion=None
# oneEdgeDeletion=None
dk=[]
# oneEdgeDeletion=False
 
# gk=g.copy()
# g 原图 gk 匿名图 d 度序列 dk 匿名度序列
class graphconstruct:
   def _init(self):
       self.dk=dk
       
       
def Regraphconstruct(g,dk):
    
    print("Starting graph reconstruction...")
    # 原始度序列
    vd = [(v,d) for v, d in g.degree()]
    vd.sort(key=lambda tup: tup[1], reverse=True)
     
    d0=[d for n, d in vd]
     
    changesVector =[]
    permution=[]
    
    for i in range(len(dk)):
           
            s=dk[i]-d0[i]
            permution.append(vd[i][0])
            changesVector.append(s)
    for i in range(len(changesVector)):
    # for i in permution:
    
    
            if (changesVector[i] < 0):# 需要删除边
                nodesToDeleteEdge.append(permution[i])
                    # j=j+1
            
            elif (changesVector[i] > 0):
                    nodesToAddEdge.append(permution[i])
    print("addlen",len(nodesToAddEdge))
    print("deletelen",len(nodesToDeleteEdge))
    # print(("nodesToDeleteEdge",nodesToDeleteEdge))
    
    # print("len",len(nodesToDeleteEdge))
    gk = graphconstruct()
    print("Original Graph  :",g.number_of_nodes(),"nodes,", g.number_of_edges(),"edges")
    print("Anonimized  Graph  :",gk.number_of_nodes(),"nodes,", gk.number_of_edges(),"edges")
    print("Graph reconstruction done!");

    return gk 
def graphconstruct():
        
    print("reconstructGraph: Starting graph reconstruction... [numEdges]=",g.number_of_edges(),"]")
    deleted = edgeDeletion()
    print("reconstructGraph: Deleted ", deleted,"edges [numEdges=",gk.number_of_edges(),"]" )
    added = edgeAddition()
    print("reconstructGraph: Added ", added,"edges [numEdges=",gk.number_of_edges(),"]" )
    changed = edgeSwitch()
    print("reconstructGraph: Changed ",changed ,"edges [numEdges=",gk.number_of_edges(),"]" )
    
    return gk

     # Reduce 'nodesToDeleteEdge' if it is larger than 'nodesToAddEdge'
def  edgeDeletion():
    removed=0
     
    # print(len(nodesToDeleteEdge),len(nodesToAddEdge))
    while(len(nodesToDeleteEdge)>len(nodesToAddEdge)):
        
        if(oneEdgeDeletion()!=True):
            print("edgeDeletion: NO EDGE HAS BEEN REMOVED!")
        # else:
        else:
           removed=removed+1
           print("edgeDeletion: EDGE HAS BEEN REMOVED!")   
    # print(removed)
    return removed
def doEdgeDeletion(vi, vj, vk, vl,score):
        numEdgesBefore = gk.number_of_edges()
        
        gk.remove_edge(vi, vk)
        
         
        gk.remove_edge(vj, vl)
       

        gk.add_edge(vk, vl)
        
        nodesToDeleteEdge.remove(vi)
        nodesToDeleteEdge.remove(vj)
        numEdgesAfter=gk.number_of_edges()
        if((numEdgesBefore-1)!= numEdgesAfter):
          print("doEdgeDeletion: WRONG NUMBER OF EDGES!")
def  edgeAddition():
        added = 0
        
        print("edgeAddition: *** Starting edge addition...")

        # /** if 'nodesToAddEdge' > 'nodesToDeleteEdge' then add new edges */
        while(len(nodesToDeleteEdge)<len(nodesToAddEdge)):
             # print("add")
             if(oneEdgeAddition()!=True):
               
                  print("edgeAddition: NO EDGE HAS BEEN ADDED!")
                 # print(added) 
             
             else:
                 # print("aaa")
                 added=added+1
                 
                 # print("edgeDeletion: NO EDGE HAS BEEN ADDED!")
                 
        # print("edgeAddition: number of tries =", edgeAdditionNumTries)   
        return added
    
def  doEdgeAddition(vi, vj,score):# edge addition
        gk.add_edge(vi, vj)
   

        nodesToAddEdge.remove(vi)
        nodesToAddEdge.remove(vj)
 
 #     * Change edges to reduce/increase degree of nodes

def  edgeSwitch():
        
        changed = 0
        n = gk.number_of_edges()
        
        print("edgeSwitch: *** Starting edge switch...") 

        
        while (len(nodesToDeleteEdge)> 0):

            # // select and remove 'vi'
            vi = nodesToDeleteEdge[0]
           

            # edge switch on 'vi'
            if(oneEdgeSwitch(vi)!=False):
                print("edgeSwitch: NO EDGE HAS BEEN SWITCHED!")
          
         
            else: 
               
              nodesToDeleteEdge.remove(vi)  
                        
              changed =changed+1
            
            
           
        print("edgeSwitch  : number of tries", edgeSwitchNumTries)

        return changed
    
    
    # oneEdgeSwitch(vi)
    
def  doEdgeSwitch(vi,vk, vj,score):
         
        # // edge switc
        # print("vi,vk, vj,",vi,vk, vj)
        gk.remove_edge(vi, vk)
        # gk.remove_edge(vk, vi)
        gk.add_edge(vk, vj)
        gk.add_edge(vj, vk)
       
        d1 =[d for n, d in gk.degree()] 
        # print(d1)
        nodesToAddEdge.remove(vj)
        # nodesToDeleteEdge.remove(vi)  
def oneEdgeDeletion():
        edgeDeletionNumTries=0
        i = 0
        while (i < len(nodesToDeleteEdge)):
            vi = nodesToDeleteEdge[i]
            # print("vi=",vi)
            
            vks=list(gk[vi])
            
            # print("vks",vks)
            # print("edges",gk.edges(vi))
            
            
            # print("j",j)
            j=i+1
            while (j <len(nodesToDeleteEdge)):
                # print(j)
               
                # vj=36629
                # 
               
                # continue
                vj = nodesToDeleteEdge[j] 
                # print("vj",vj)
                
                vls = list(gk[vj])
                # print("vls",vls)
               
                #print("edges_vj",gk.edges(vj))
                # print("oneEdgeDeletion: deleting edges from nodes", vi,"and", vj)
                for vk in vks:
                    # print("vk",vk)
                    # print(list(gk[vk]))
                    for vl in vls:
                        # print("vl",vl)
                        
                       
                        if (vk!=vl and (gk.has_edge(vk, vl)!=True)):
                        
                               doEdgeDeletion(vi, vj, vk, vl, -1)

                            # // number of tries
                               edgeDeletionNumTries+=1
                        
                        
                               
                            # print("edgeDeletionNumTries",edgeDeletionNumTries)
                               return True
                j = j + 1
                        # edgeDeletionNumTries=edgeDeletionNumTries+1
                        # print("edgeDeletionNumTries",edgeDeletionNumTries)
            i=i+1
        return False
    

    
    #  Edge Addition 
  
def  oneEdgeAddition():
        edgeAdditionNumTries=0
        i = 0;
        while (i<len(nodesToAddEdge)):
            
            vi = nodesToAddEdge[i]
            # print("vi",vi)
            j = i + 1
           
            while (j < len(nodesToAddEdge)):
                
                vj = nodesToAddEdge[j]
                # print("vj",vj)
                if ((vi != vj) and gk.has_edge(vi, vj)!=True):
               
                    doEdgeAddition(vi, vj, -1)

                    # // number of tries
                    edgeAdditionNumTries+=1
                   
                    return True
                j=j+1
            
           
            i=i+1
        

        return False
    

    
   
def oneEdgeSwitch(vi):  #  Edge Switch  
         
        edgeSwitchNumTries=0
        vks = list(gk[vi])
        
        for vk in  vks:
            for vj in nodesToAddEdge:
                
                if (vi != vj and vk != vj and (vj in list(gk[vi]))!=True):
                    
                  
                    doEdgeSwitch(vi, vk, vj, -1)
                   
                    edgeSwitchNumTries+=1
                    
                    return True
                
            
        

        return False
    


        
if __name__=="__main__": 
     #CA-AstroPh CA-CondMat CA-GrQc CA-HepTh Email-Enron
    # datafile = pds.read_csv("datasets/CA-HepTh.csv", header=None)
    # datafile = pds.read_csv("Polbook.csv", header=None)
    datafile = pds.read_csv("FB.csv", header=None)
    datafile=datafile.values
    # print(datafile)
   
    g=nx.Graph()
    g.add_edges_from(datafile)
    s=[] 
    odered_degree_sequence=sorted([d for n, d in g.degree()],reverse=True)
    gk=g.copy()
   
    degreeCount = collections.Counter(odered_degree_sequence)
    
    degreeCount=degreeCount.items()
    
    
   
    degreeCount=list(degreeCount)
    
    t=T.HuffmanTree()
    data=t.PrintTree(degreeCount)
    
     

    data.reverse()
     
    a=[x[1] for x in data]
    b=[y[0] for y in data]
     
    start=time.time()
    tree=ano_dSeq.Tree()
    for i in range(len(b)):
    
        tree.add(b[i],a[i])
     
    k=2
    n=tree.Seq(tree.root,k)
    
    attempt=1
    noise=1
     
    
     
    vd = [(v,d) for v, d in g.degree()]
    vd.sort(key=lambda tup: tup[1], reverse=True)
   
    d0=[d for n, d in vd]
    anonymised_sequence=tree.partion(n)
    # print(type(anonymised_sequence))
    anonymised_sequence=tree.seq_partion(anonymised_sequence,g,k)
    print(len(anonymised_sequence))
    print("Total execution time =",time.time()-start)
    if np.sum(anonymised_sequence) % 2 != 0:
        print("添加噪声")
        dk = tree.probing(anonymised_sequence,noise)
    else:
        dk=anonymised_sequence
    print(len(dk),"dk",np.sum(dk))
    degreeC = collections.Counter(anonymised_sequence)
    degreeC=degreeC.items()
    degreeC=list(degreeC)
    # print(degreeC)
    gk=Regraphconstruct(g,dk) 
    
    s=[]
    print("原始平均聚类系数(average clustering): ", nx.average_clustering(g))
    print("原始网络传递性(transitivity): ", nx.transitivity(g))
    for C in (gk.subgraph(c).copy() for c in nx.connected_components(gk)):
        # print("最短平均路径",nx.average_shortest_path_length(C))
        s.append(nx.average_shortest_path_length(C))
    print("平均路径长度",max(s))
     
    print("平均聚类系数(average clustering): ", nx.average_clustering(gk))
    print("网络传递性(transitivity): ", nx.transitivity(gk))
    # # print("Total execution time =",time.time()-start)
    print("k=",k)

     
    


    
    
 










