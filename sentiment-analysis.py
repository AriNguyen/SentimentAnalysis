import tensorflow as tf
import pandas as pd

import os
import shutil

URL = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

dataset = tf.keras.utils.get_file(fname='aclImdb_v1.tar.gz', origin=URL, untar=True, cache_dir='.', cache_subdir='')

main_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')

train_dir = os.path.join(main_dir, 'train')

remove_dir = os.path.join(train_dir, 'unsup')
shutil.rmtree(remove_dir)

print(os.listdir(train_dir))

train = tf.keras.preprocessing.text_dataset_from_directory('aclImdb/train', batch_size=30000, validation_split=0.2, subset='training', seed=123)

test = tf.keras.preprocessing.text_dataset_from_directory('aclImdb/train', batch_size=30000, validation_split=0.2, subset='validation', seed=123)