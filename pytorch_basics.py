# -*- coding: utf-8 -*-
"""PyTorch_basics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kYZ1IGzhTR5shFC95pd9LfQkQAHgoSvW
"""

import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(torch.__version__)

!nvidia-smi



"""###Introduction to Tensors"""

# creating tensors

## scalar

scalar = torch.tensor(7)
scalar

scalar.ndim

# tensor back as a Python int
scalar.item()

# Vector

vector = torch.tensor([7, 7])
vector

vector.ndim

vector.shape

# MATRIX

MATRIX = torch.tensor([[7, 8], [9, 10]])
MATRIX

MATRIX.shape

MATRIX[1]

# Tensor

tensor = torch.tensor([[[1, 2, 3], [3, 6, 9], [2, 4, 5]]])
tensor

tensor.ndim

tensor.shape

"""###Random Tensors

why random tensors?
Random tensors are important because the way many neural networks learn is that they start with tensors full of random numbers and then adjust those numbers  to better represent the data

Start with random numbers --> look at data --> update random numbers --> look at data --> updated random numbers

Torch random tensors: https://pytorch.org/docs/stable/generated/torch.rand.html#torch-rand


"""

## create a random tensor of size(3, 4)

random_tensor = torch.rand(3, 4)
random_tensor

random_tensor.ndim

# create a random tensor with similar shape to a an image

random_image_size_tensor = torch.rand(size=(224, 224, 3)) # height, width, color channels (R, G, B)
random_image_size_tensor.shape, random_image_size_tensor.ndim

random_tensor2 = torch.rand(3, 6)
random_tensor2

## Zeros and Ones


zeros = torch.zeros(3, 5)
zeros

ones = torch.ones(5, 8)
ones

ones.dtype

"""### Creating a range of tensors and tensors-like"""

# use torch.range()

torch.arange(start=1, end=51, step=1)

hello = torch.arange(start=1, end=11, step=1)
one_to_ten

# creating tensors like

ten_zeros = torch.zeros_like(input=hello)
ten_zeros

float_32_tensor = torch.tensor([3, 6.0, 9.0],
                               dtype=None,    # what dtype is the tensor
                               device="cuda", # what device is your tensor on
                               requires_grad=False) # whether or not to track gradinets with this tensors operations
float_32_tensor

float_32_tensor.dtype

x_16 = torch.tensor([1, 2, 3], dtype=torch.float16)
x_16.dtype

y_32 = torch.tensor([1, 2, 3], dtype=torch.float32)
y_32

y_32 // x_16

