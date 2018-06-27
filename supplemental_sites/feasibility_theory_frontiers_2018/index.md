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

# PCA Loadings Bootstrapping Figure
*Prepared by: Brian A. Cohn*

<a href="https://github.com/briancohn/space/raw/master/pca_figure_code/pca_loadings_bootstrapped_formatted.jpg"><img src="https://github.com/briancohn/space/raw/master/pca_figure_code/pca_loadings_bootstrapped_formatted.jpg"></a>

> Click for full size figure

<b>Supplementary Figure: Normalized PC Loadings as task intensity increases, under different sampling sizes for PCA analysis.</b> How do PCA loadings act when the sample number of the input dataset is impoverished? Each facet (a squared-in set of boxplots) shows how loadings change over increasing task intensity. Each facet represents a different number of samples fed to PCA. You can read each group of boxplots as a muscle's task-dependent loading distribution. In the paper, we usd 100 replicates (PCA was run 100 times for each boxplot; each boxplot has an n=100) but for this supplemental visualization we did 1000 replicates. Each color represents a task intensity, so each cluster of boxplots (through the color pallete) represents a given loading's change over increasing distal force as the output task. The columns of faceted plots represent the number of *samples* fed to PCA, which were 10, 100, or 1000 (as in the paper), as well as 5000 samples.


#### Commands to replicate this figure on Linux or Mac.
Terminal:
```bash
$ git clone git@github.com:briancohn/space.git && cd space/pca_figure_code && R
```
In R:
```r
install.packages('ggplot2')
install.packages('devtools')
install.packages('pbmcapply')
install.packages('dplyr')
install.packages('gridExtra')
source('pca_bootstrapped_loadings_comparison.r')
```
R and git must be installed. The same commands can be used on PC via the <a href="https://gitforwindows.org/">Git Bash Terminal</a>.
________

# Muscle Task-Variance Visualization
*Prepared by: Brian A. Cohn*

<a href="https://github.com/briancohn/space/raw/master/pca_figure_code/pca_loadings_bootstrapped_formatted.jpg"><img src="https://github.com/briancohn/space/raw/master/pca_figure_code/muscle_variance_over_tasks.jpg"></a>
<b> Supplementary Figure: Visualization of activation variance for a given muscle, for a given task intensity.</b> We find that as the intensity of the task increases, the standard deviation of all muscles decreases, where each task intensity had 10,000 points sampled. Although the muscles appear to change in variance in a similar way, different muscles have differing starting values of variance.

#### Commands to replicate this figure on Linux or Mac
In R, after the commands from above:
```r
source('muscle_variance_over_tasks.r')
```


### Have comments or questions about how to apply these methods to your work?
We'd be happy to help. Send us a message: brian.cohn@usc.edu

# Code to produce figures  
[Code to produce muscle activation patterns for a given task](https://github.com/briancohn/space)
[Parallel Coordinates in R](https://github.com/briancohn/fig5_parcoord)  
[Histogram Heatmap in R](https://github.com/briancohn/space/blob/master/src/R/hist_heatmap.r)  
[PCA, Loadings, and Bootstrapped Figures](https://github.com/briancohn/space/tree/master/pca_figure_code)  
[Code used to calculate the size of the feasible activation space before and after post hoc constraints](https://github.com/briancohn/constraint_statistics/blob/master/main.Rmd)  
