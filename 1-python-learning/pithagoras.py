import numpy as np

weights = np.array([1,2])
input_data = np.array([3,4])

target = 6
learning_rate = 0.01

preds = (weights * input_data).sum() 
error = preds - target 

slope = 2 * input_data * error

weights_updated = weights - learning_rate * slope

preds_updated = (input_data * weights_updated).sum()

error_updated = preds_updated - target
