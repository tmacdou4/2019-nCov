#!/bin/bash

# create a new environment named cgvae_new
conda create --name cgvae_new python=3.5 pip
conda activate cgvae_new

# install cython
pip install Cython --install-option="--no-cython-compile"

# install rdkit
conda install -c rdkit rdkit

# install tensorflow 1.13.1
pip install tensorflow-gpu==1.13.1

# install other requirements
pip install -r requirements.txt