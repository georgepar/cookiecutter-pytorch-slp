import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class MyModule(nn.Module):
    """Some Information about MyModule"""
    def __init__(self):
        super(MyModule, self).__init__()

    def forward(self, x):

        return x
