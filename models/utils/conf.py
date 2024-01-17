import os
import numpy as np
import pandas as pd
import torch

# define device.
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# parameter about dataset
mydir = os.getcwd()
#DATA_PATH = mydir + '\\content'
DATA_PATH = 'C:\\Users\\qowor\\Desktop\\open'
SAVE_ORIGIN_PATH = DATA_PATH+'\\origin'
SAVE_AGUMENT_PATH = DATA_PATH+'\\augment'
TRAIN_DF = pd.read_csv(DATA_PATH+'\\train.csv')
TRAIN_DF = pd.read_csv(DATA_PATH+'\\test.csv')

# parameter about model.
BATCH_SIZE = 32