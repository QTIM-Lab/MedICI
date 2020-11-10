import torchvision
import torchvision.transforms as transforms

# 1. Loading and normalizing CIFAR10

# The output of torchvision datasets are PILImage images of range [0, 1]. We transform them to Tensors of normalized range [-1, 1]. .. note:

# normalization
transform = transforms.Compose(
    [transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

# train
trainset = torchvision.datasets.CIFAR10(root='/mnt/in/data', train=True,
                                        download=True, transform=transform)

# test
testset = torchvision.datasets.CIFAR10(root='/mnt/in/data', train=False,
                                       download=True, transform=transform)
