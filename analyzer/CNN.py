import os
import numpy as np
import torch
import glob
import torch.nn as nn
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torch.optim import Adam
from torch.autograd import Variable
import torchvision
import pathlib

# Check Device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

transformer = transforms.Compose([
    transforms.Resize((300, 300)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),  # 0-255 to 0-1, numpy to tensor
    # 0-1 to [-1,1], formula x-mean/stand deviation
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

# DataLoader
train_path = r"TrainningSet\my_train\my_train"
test_path = r"TrainningSet\my_test\my_test"
print(train_path, test_path)
train_loader = DataLoader(
    torchvision.datasets.ImageFolder(train_path, transform=transformer),
    batch_size=128, shuffle=True
)
test_loader = DataLoader(
    torchvision.datasets.ImageFolder(test_path, transform=transformer),
    batch_size=128, shuffle=True
)

# categories (show all folder name categories)
root = pathlib.Path(train_path)
categories = sorted([j.name.split('/')[-1] for j in root.iterdir()])
print(categories)

# CNN Network


class ConvNet(nn.Module):
    def __init__(self, num_categories=5):
        super(ConvNet, self).__init__()

        # Output size after convolution filter [(w-f+2P)/s]+1
        # w = width and height
        # f = kernel_size
        # p = padding
        # s = stride

        # Input shape=(batch size,channel size,width,height)
        # the 1st out_channel should be same as the 2nd in_channel
        self.conv1 = nn.Conv2d(
            in_channels=3, out_channels=12, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features=12)
        self.relu1 = nn.ReLU()
        # group channels into a group
        self.pool = nn.MaxPool2d(kernel_size=2)
        self.conv2 = nn.Conv2d(
            in_channels=12, out_channels=20, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()

        self.conv3 = nn.Conv2d(
            in_channels=20, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(num_features=32)
        self.relu3 = nn.ReLU()

        self.fc = nn.Linear(in_features=32*150*150,
                            out_features=num_categories)

        # Feed forward function
    def forward(self, input):
        # same as above
        output = self.conv1(input)
        output = self.bn1(output)
        output = self.relu1(output)

        output = self.pool(output)

        output = self.conv2(output)
        output = self.relu2(output)

        output = self.conv3(output)
        output = self.bn3(output)
        output = self.relu3(output)

        output = output.view(-1, 32*150*150)
        # feed inside fully connected layer
        output = self.fc(output)

        return output


model = ConvNet(num_categories=5).to(device)
# Optimizer and loss function
optimizer = Adam(model.parameters(), lr=0.001, weight_decay=0.0001)
loss_function = nn.CrossEntropyLoss()

numEpochs = 100
# count image number to check
train_count = len(glob.glob(train_path+'/**/*.jpg'))
test_count = len(glob.glob(test_path+'/**/*.jpg'))

print(train_count, test_count)

# Model trainning and save best model

best_acc = 0.0

for epoch in range(numEpochs):
    # train dataset
    model.train()
    train_acc = 0.0
    train_loss = 0.0

    for i, (images, labels) in enumerate(train_loader):
        if torch.cuda.is_available():
            images = Variable(images.cuda())
            labels = Variable(labels.cuda())

        optimizer.zero_grad()

        outputs = model(images)
        loss = loss_function(outputs, labels)
        loss.backward()
        optimizer.step()

        train_loss += loss.cpu().data*images.size(0)
        _, prediction = torch.max(outputs.data, 1)

        train_acc += int(torch.sum(prediction == labels.data))

    train_acc = train_acc/train_count
    train_loss = train_loss/train_count

    # test dataset
    model.eval()

    test_acc = 0.0
    for i, (images, labels) in enumerate(test_loader):
        if torch.cuda.is_available():
            images = Variable(images.cuda())
            labels = Variable(labels.cuda())

        outputs = model(images)
        _, prediction = torch.max(outputs.data, 1)
        test_acc += int(torch.sum(prediction == labels.data))

    test_acc = test_acc/test_count

    print('Epoch: '+str(epoch)+' Train Loss: '+str(train_loss) +
          ' Train Acc: '+str(train_acc)+' Test Acc: '+str(test_acc))

    # Save the highest acc model
    if test_acc > best_acc:
        torch.save(model.state_dict(), 'my_trainner.model')
        best_acc = test_acc
        print("better acc model file generated")
