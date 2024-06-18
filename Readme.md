# This code is the source code implementation for the paper "TKDA: An Improved Method for K-degree Anonymity in Social Graphs."



# Abstract
Data anonymization is one of the most important directions in privacy-preserving. However, research shows that simple anonymization of data does not protect privacy. To solve this problem, we present a novel and effective algorithm named tree-based K-degree anonymity (TKDA). We devise a new anonymity sequence generation method to reduce the informa tion loss for social graphs. Then, the dynamic anonymization process is implemented by a depth-first search (DFS) traversal algorithm. Finally, the graph modification algorithm based on the anonymous sequence can keep the original graph structure stable. Average Path Length (APL), Average Clustering Coefficient (ACC), and Transitivity (T) are employed to evaluate the method. Experimental results on several datasets show that TKDA is closer to the values of the original graphs on the correlated three experimental metrics, which indicates that TKDA portrays the real data in more detail and improves the utility of the released data.(https://ieeexplore.ieee.org/abstract/document/9912964)

# Reference
```
@inproceedings{xiang2022tkda,
  title={TKDA: An improved method for k-degree anonymity in social graphs},
  author={Xiang, Nan and Ma, Xuebin},
  booktitle={2022 IEEE Symposium on Computers and Communications (ISCC)},
  pages={1--6},
  year={2022},
  organization={IEEE}
}
```
# Experimental Environment

```
Operating Environment: Python with Intel Core i5 CPU 1.8 GHz and 8 GB RAM, running MacBook.
-numpy 1.19.2
-collections 1.2.1
-random 1.1.1
-pandas 1.1.3
-networkx 2.5
-math 1.1.0
-Python 3.9
-torch==2.0.0
- torchvision~=0.15.1+cu117
```

# Datasets

`Polbooks,Ca-AstroPh,Ca-GrQc`

# Experimental Setup

The experimental setup in the paper focuses on evaluating the effectiveness of a novel graph anonymization algorithm called TKDA. The setup is designed to test the algorithm's ability to maintain data utility while ensuring privacy through graph modification. 

   - **Dataset Scanning**: O(n), where n is the dataset size.
   - **Tree Construction**: O(m), m being the number of leaf nodes.
   - **DFS Traversal**: Complexity ranges from O(km) to O(klogm), where k is the number of branches traversed.
   - **Total Complexity**: O(n+m+km) to O(n+m+klogm).
   - **Graph Modification**: Described as a P-problem solvable in polynomial time through logarithmic calculations of combinations.

The paper also compares TKDA with other anonymization techniques, emphasizing the graph modification approach for anonymizing social network data. This includes adding edges, modifying nodes, or a combination of both to meet K-degree anonymity requirements.


# Python Files

1. **ano_degreeSeq.py**:
   - This file contains code related to generating or manipulating the degree sequence of a graph for anonymization purposes. "Ano" could stand for "anonymization," and "degreeSeq" suggests that the focus is on the sequence of degrees of nodes within a graph. The script implement methods to adjust the degree sequence to meet certain privacy standards without altering the overall structure of the graph too drastically.

2. **GraphConstruct.py**:
   - This file likely involves constructing or modifying graphs based on specific algorithms or requirements. The term "GraphConstruct" suggests functions that either build new graphs from scratch or modify existing graphs according to defined rules or algorithms. 

3. **tree.py**:
   - This script is  related to tree data structures within the context of graph theory or network analysis. It might include functions for creating tree structures from graph data, possibly for efficient traversal, partitioning of the graph, or to facilitate operations like searches, insertions, and deletions within the graph structure. 
#  Experimental Results
Figure 5 presents a comparative analysis of error evaluations on the Polbooks dataset using three different algorithms: GA-KDA, TSRAM, and TKDA. This comparison is structured around three key metrics: (ACC), (T),  (APL). 
![输入图片说明](https://github.com/csmaxuebin/TKDA/blob/main/pic/fig5.jpg)



Figure 6 displays the Average Clustering Coefficient (ACC) values for anonymized graphs derived from two datasets, Ca-AstroPh and Ca-GrQc, using multiple anonymization algorithms: TKDA, KDVE, FKDA, Priority, and VertexAdd.
![输入图片说明](https://github.com/csmaxuebin/TKDA/blob/main/pic/fig6.jpg)


Figure 7 illustrates the impact of varying levels of K-anonymity on the transitivity metric of two datasets, Ca-AstroPh and Ca-GrQc, using five different anonymization algorithms: TKDA, KDVE, FKDA, Priority, and VertexAdd.
![输入图片说明](https://github.com/csmaxuebin/TKDA/blob/main/pic/fig7.jpg)


Figure 8 illustrates the impact of various K-anonymity levels on the Average Path Length (APL) for two datasets, Ca-AstroPh and Ca-GrQc, using multiple anonymization algorithms including TKDA, KDVE, FKDA, Priority, and VertexAdd.
![输入图片说明](https://github.com/csmaxuebin/TKDA/blob/main/pic/fig8.jpg)





## Update log

```
- {24.06.15} Uploaded overall framework code and readme file
```

