import torch


class MyDataset(torch.utils.data.Dataset):
    """Some Information about MyDataset"""
    def __init__(self):
        super(MyDataset, self).__init__()

    def __getitem__(self, index):
        return

    def __len__(self):
        return
