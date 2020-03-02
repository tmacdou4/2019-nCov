#!/bin/bash

# create a new environment named nCov_env
conda create --name nCov_env python=3.5 pip
conda activate nCov_env


# install cython
pip install Cython --install-option="--no-cython-compile"

# install rdkit
conda install -c rdkit rdkit

#sklearn
conda install scikit-learn=0.20.3

#IPython!
conda install ipykernel

python -m ipykernel install --user --name nCov_env --display-name "nCov_env"

# Pytorch 1.0.1
conda install pytorch==1.0.1 torchvision==0.2.2 -c pytorch

# install tensorflow 1.13.1
pip install tensorflow-gpu==1.13.1

# install other requirements
pip install -r requirements.txt
