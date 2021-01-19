# CCRSSVED
The implementation of “Classifying Conserved RNA Secondary Structures with Pseudoknots by Vector-Edit Distance”.  

## Requirement

- Python 3.6

- Numpy

- re

- pickle


## Data 
### The RNA sequences and their secondary structures in Cluster 86486: RNAz cluster #86486.txt
### The RNA sequences and their secondary structures of RNAz Cluster 16165, 25547, 58284, 61845, 80001, 86486 and 113047 from Cluster A-F: abcdef.txt
### The  438 Structures and 1545 RNAs included in the selection of high scoring structures: SOHSS.txt
### PseudoBase contains 393 RNA sequences with pseudoknots, and their secondary structures with dot-bracket notation.: PseudoKnots.txt


## Run
### The distance between RNAs without pseudoknots: knot-free.py
### Convert RNA secondary structures to the tree nodes : STRtoNode.py
### Build modified adjoining grammars binary tree: BuildTree.py
### Vector distance: compute_distance.py
### Edit distance: compute_editor.py
### Calculate and store Vector-Edit distances: Store.py
## Obtain the distance matrix: 
### If you want to obtain distance matrix  between RNAs with pseudoknots, please run total_struct.py directly.