---
layout: page
title: Feasibility theory
---
# Companion Website
*Prepared by: Brian A. Cohn*

## Frontiers 2018
### **Abstract:**
We present a conceptual and computational framework to unify today's theories of neuromuscular control called feasibility theory.
We begin by describing how the musculoskeletal anatomy of the limb, the need to control individual tendons, and the physics of a motor task uniquely specify the family of all valid muscle activations that accomplish it (its `feasible activation space').
For our example of static force production with a finger with seven muscles, computational geometry characterizes, in a complete way, the structure of  feasible activation spaces as 3-dimensional polytopes embedded in 7-D.
The feasible activation space for a given task is _the_ landscape where all neuromuscular learning, control, and performance must occur.
This approach unifies current theories of neuromuscular control because the structure of feasible activation spaces can be separately approximated as either low-dimensional basis functions (synergies), high-dimensional joint probability distributions (Bayesian priors), or fitness landscapes (to optimize cost functions).
# [Interactive Parallel Coordinates Visualization](https://briancohn.github.io/space-parcoords/)
<img src="../../img/projects/cohn2017.gif">

# Have comments or questions about how to apply these methods to your work?
We'd be happy to help. Send us a message: brian.cohn@usc.edu

# Code to produce muscle activation patterns for a given task
[GitHub Repository](https://github.com/briancohn/space)

[Visualization of all three principal components (rows) at differing levels of subsampling (columns)](https://github.com/briancohn/space/raw/master/pca_figure_code/pca_loadings_bootstrapped.pdf)
```
Each plot shows how loading changes for each muscle. You can read each group of boxplots as a muscle's task-dependent loading distribution. As in the paper, we use 100 replicates (PCA was run 100 times for each boxplot; each boxplot has an n=100).
```

# Code to produce figures  
[Parallel Coordinates in R](https://github.com/briancohn/fig5_parcoord)  
[Histogram Heatmap in R](https://github.com/briancohn/space/blob/master/src/R/hist_heatmap.r)  
[PCA, Loadings, and Bootstrapped Figures](https://github.com/briancohn/space/tree/master/pca_figure_code)  
[Code used to calculate the size of the feasible activation space before and after post hoc constraints](https://github.com/briancohn/constraint_statistics/blob/master/main.Rmd)  

________


#
