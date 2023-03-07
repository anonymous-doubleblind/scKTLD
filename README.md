# scKTLD

## 1. Introduction
scKTLD is a method designed for the identification of TAD-like domains on single-cell Hi-C data. It treats the Hi-C contact matrix as a graph, embeds its structures into a low-dimensional space by combining sparse matrix factorization and spectral propagation, and identifies the TAD-like domains in the embedding space via a kernel model optimized by PELT

## 2. Installation & Example

**2.1 OS**
- ubuntu 18.04

**2.2 Required Python Packages**
Make sure all all the packages listed in the *requirements.txt* are installed.

- Python >= 3.6
- scipy >= 1.5.2
- numpy >= 1.18.0
- ticc >= 0.1.6
- networkx >= 2.5
- scikit-learn >= 0.24.2
- Cython >= 0.29.33

**2.3 Install from Github**

(1) Download the folder *scKTLD* by git clone
```
$ git clone https://github.com/anonymous-doubleblind/scKTLD/
```
(2) Install the package *scKTLD* with the following command:
```
$ cd scKTLD
$ python setup.py install  #or you can try pip install .
```

**2.4 Run example**
```
$ cd scKTLD
$ python example.py
```
![image](https://github.com/anonymous-doubleblind/scKTLD/blob/main/data/exp-sc/Figure_1.png)
