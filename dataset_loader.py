import os
from itertools import chain
from jcamp import JCAMP_reader
import numpy as np

# CONSTANTS, DO NOT CHANGE
dataset_path = './dataset'
directory_path = 'directory_path'
dataset_file_extension = '.dx'
dataset_file_extension_index = -1


# This function allows you to load all data from all directories contained in './dataset' or chosen directory
def load_dataset(**kwargs):
    # Check for params
    if directory_path in kwargs:
        # If param found -> load data from directory passed
        dataset_loading_path = kwargs[directory_path]
    else:
        # If not -> load whole dataset dir
        dataset_loading_path = dataset_path
    dataset = {}
    for root, directories, files in os.walk(dataset_loading_path):
        for dataset_file in files:
            # If file extension is '.dx'
            if os.path.splitext(dataset_file).__getitem__(dataset_file_extension_index) == dataset_file_extension:
                # Receive file path
                file_path = os.path.join(root, dataset_file)
                # Logging
                print('Loading data from ' + file_path)
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
