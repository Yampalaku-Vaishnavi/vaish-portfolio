import tensorflow as tf

# Set the environment variable to disable oneDNN optimizations
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Check GPU devices
gpus = tf.config.list_physical_devices('GPU')
print("GPUs available: ", gpus)

# Example usage of the deprecated loss function using the compatibility module
loss = tf.compat.v1.losses.sparse_softmax_cross_entropy
