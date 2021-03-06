# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TRUBMm2fTEuwzDlkr6I4SGDsbsMGThHf
"""

import tensorflow as tf
from tensorflow.python.platform import gfile
with tf.Session() as sess:
    model_filename ='/content/graph_opt.pb'
    with tf.gfile.GFile(model_filename, 'rb') as f:
        graph_def = tf.GraphDef()
        train_writer.flush()
        train_writer.close()
        graph_def.ParseFromString(f.read())
        g_in = tf.import_graph_def(graph_def)
LOGDIR='/content'
train_writer = tf.summary.FileWriter(LOGDIR)
train_writer.add_graph(sess.graph)

import datetime
!rm -rf ./logs/
#tf.reset_default_graph()
log_dir="/content" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard

!kill 1301

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir /content