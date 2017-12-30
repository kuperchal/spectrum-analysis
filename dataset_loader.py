
import os
from itertools import chain
from jcamp import JCAMP_reader
import numpy as np


dataset_file_extension = '.dx'
dataset_file_extension_index = -1


def load_dataset():
    return 0


def load_dataset_from_dir(directory_path):
    dataset = {}
    # Walk around passed directory
    for root, directories, files in os.walk(directory_path):
        # For each file found in the directory
        for dataset_file in files:
            # If file extension is '.dx'
            if os.path.splitext(dataset_file).__getitem__(dataset_file_extension_index) == dataset_file_extension:
                print('Loading data from ' + dataset_file)
                # Receive file path
                file_path = os.path.join(root, dataset_file)
                # Read received file with JCAMP
                spectra = JCAMP_reader(file_path)
                # Transmission is vertical axis
                transmission = spectra['y']
                # Stack up the results to the returned dataset as (k = './dataset/data-.../', v = transmission)
                if root in dataset:
                    # If there are such key, then add value
                    dataset[root] = np.vstack((dataset[root], transmission))
                else:
                    # If no - create new
                    dataset[root] = transmission
    return dataset
