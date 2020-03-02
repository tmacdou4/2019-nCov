import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rdkit import Chem
from rdkit.Chem import rdmolops
from rdkit.Chem import QED
import glob
import csv, json
import numpy as np
from utils import bond_dict, dataset_info, need_kekulize, to_graph,graph_to_adj_mat
import utils
import pickle
import random
from docopt import docopt

dataset = "protease"

def train_valid_split(download_path):
    # load validation dataset
    with open("valid_idx_protease.json", 'r') as f:
        valid_idx = json.load(f)

    print('reading data...')
    raw_data = {'train': [], 'valid': []}  # save the train, valid dataset.
    with open(download_path, 'r') as f:
        all_data = list(csv.DictReader(f))

    file_count = 0
    for i, data_item in enumerate(all_data):
        smiles = data_item['smiles'].strip()
        ACT = float(data_item['act'])
        if i not in valid_idx:
            raw_data['train'].append({'smiles': smiles, 'ACT': ACT})
        else:
            raw_data['valid'].append({'smiles': smiles, 'ACT': ACT})
        file_count += 1
        if file_count % 2000 == 0:
            print('finished reading: %d' % file_count, end='\r')
    return raw_data

def preprocess(raw_data, dataset):
    print('parsing smiles as graphs...')
    processed_data = {'train': [], 'valid': []}

    file_count = 0
    for section in ['train', 'valid']:
        all_smiles = []  # record all smiles in training dataset
        for i, (smiles, QED) in enumerate([(mol['smiles'], mol['QED'])
                                           for mol in raw_data[section]]):
            nodes, edges = to_graph(smiles, dataset)
            if len(edges) <= 0:
                continue
            processed_data[section].append({
                'targets': [[(QED)]],
                'graph': edges,
                'node_features': nodes,
                'smiles': smiles
            })
            all_smiles.append(smiles)
            if file_count % 2000 == 0:
                print('finished processing: %d' % file_count, end='\r')
            file_count += 1
        print('%s: 100 %%      ' % (section))
        # save the dataset
        with open('molecules_%s_%s.json' % (section, dataset), 'w') as f:
            json.dump(processed_data[section], f)
        # save all molecules in the training dataset
        if section == 'train':
            utils.dump('smiles_%s.pkl' % dataset, all_smiles)

if __name__ == "__main__":
    download_path = 'protease.csv'
    if not os.path.exists(download_path):
        print('downloading data to %s ...' % download_path)
        source = 'https://raw.githubusercontent.com/tmacdou4/2019-nCov/data/250k_rndm_zinc_drugs_clean_3.csv'
        os.system('wget -O %s %s' % (download_path, source))
        print('finished downloading')

    raw_data = train_valid_split(download_path)
    preprocess(raw_data, dataset)