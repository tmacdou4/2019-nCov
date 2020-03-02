# 2019-nCov

## Description
Efforts towards proposing a potentially highly active molecule against a target protein of the 2019 Novel Coronavirus. 

Submission for the Sage-health coronavirus deep learning competition. 

Structure of this repository:

The Jupyter Notebook: Report_Tom_MacDougall.ipynb serves as my submission, including all phases of dataset acquiring, prediction and molecular generation, docking of the final candidates and , including an autodock vina tutorial.

The requirements for this project are unfortunately pretty large. And also unfortunately, the used approaches make use of both Pytorch and Tensorflow so they have to each be installed if you want to work through the report notebook from start to finish. The notebook however does make a lot of use of pickling and saving intermeadiate answers, so you may even be able to do a kernel switch part way through. 

I have made an install.sh script that can install all of the dependencies in a fresh conda environment (called nCov_env). So, for the install script to work, you must have conda or miniconda installed. If you already have a environment with most or all of the requirements, go ahead and try the various parts. It might be however advisable to stick to tensorflow 1.XX however as I don't think backwards compatibility is guaranteed between major releases.

## Contents of this repo
I did most of the work in several separate notebooks, then consolidated the work into the final report notebook. So, there should be no need to dive into the other directories, but if you want to poke around the code or look at specific data files, be my guest!

3 video tutorials are found in /Videos
    One is an overview of my submission report
    One is an explanation of IC50 and activity values

Data is stored in /Data (for both dataset generation and the two methods)

Intermeadiate notebooks and rough work are stored in /notebooks

Input and output for docking studies is found in /Docking

Files for the predictive deep learning method, The Edge Memory Neural Network, are found in /EMNN

Files for the generative deep learning method, The Constrained Graph Variational Autoencoder, are found in /CGVAE

Various papers mentioned and referenced (including for the methods used) are found in /Literature

Various Pymol session are found in /PymolSessions

A nice final Vina tutorial by the original author is available in vina-tutorial/

Other files, notes and rough work can be found in /misc, but these are not strictly important to the narrative of the study and their contents have likely been added to the report notebook anyway.
