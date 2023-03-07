# scKTLD

## 1. Introduction
scKTLD is a method designed for the identification of TAD-like domains on single-cell Hi-C data. It treats the Hi-C contact matrix as a graph, embeds its structures into a low-dimensional space by combining sparse matrix factorization and spectral propagation, and identifies the TAD-like domains in the embedding space via a kernel model optimized by PELT

## 2. Installation & Example

**2.1 OS**
- ubuntu 18.04

**2.2 Required Python Packages
Make sure all all the packages listed in the *requirements.txt* are installed.

-Python >= 3.6
-scipy >= 1.5.2
-numpy >= 1.18.0
-ticc >= 0.1.6
-networkx >= 2.5
-scikit-learn >= 0.24.2
-Cython >= 0.29.33
