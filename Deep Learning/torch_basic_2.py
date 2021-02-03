import numpy as np
import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# Data Loader

batch_size = 32
test_batch_size = 32

train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('dataset/', train = True, download=True,
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5,), std=(0.5,))
    ])),
    batch_size=batch_size,
    shuffle=True
)

test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('dataset', train=False,
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5))
    ])),
    batch_size=test_batch_size,
    shuffle=True)

# 첫번째 iteration에서 나오는 데이터 확인
images, labels = next(iter(train_loader))
print(images.shape) # batch size, channel, height, width

# 시각화
images[0].shape
torch_image = torch.squeeze(images[0])
