# Pytorch-VAE
This is an implementation of the VAE (Variational Autoencoder) for Cifar10

You can read about dataset here -- [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html)

## Example

All images are taken from the test set. Left row is the original image. Right row is the reconstruction.

Original                      |  Reconstruction
:-------------------------:|:-------------------------:
frog  |  ![](https://github.com/SashaMalysheva/Pytorch-VAE/blob/master/data/1-1.jpg)
bird | ![](https://github.com/SashaMalysheva/Pytorch-VAE/blob/master/data/3-1.jpg)


## Setup

```
conda env create
python setup.py develop
```

### To train on new dataset:

To initialize training, simply go ahead

```
./main.py --train
 [--dataset {mnist,cifar10,cifar100}]
 [--kernel-num KERNEL_NUM] [--z-size Z_SIZE]
 [--epochs EPOCHS] [--batch-size BATCH_SIZE]
 [--sample-size SAMPLE_SIZE] [--lr LR]
 [--weight-decay WEIGHT_DECAY]
 [--loss-log-interval LOSS_LOG_INTERVAL]
 [--image-log-interval IMAGE_LOG_INTERVAL]
 [--resume] [--checkpoint-dir CHECKPOINT_DIR]
 [--sample-dir SAMPLE_DIR] [--no-gpus]
```

dataset == 'mnist', 'cifar10', 'cifar100'

It will convert imgs from срщщыут dataset 

### To test 

```
./main.py --test
 [--dataset {mnist,cifar10,cifar100}]
 [--kernel-num KERNEL_NUM] [--z-size Z_SIZE]
 [--epochs EPOCHS] [--batch-size BATCH_SIZE]
 [--sample-size SAMPLE_SIZE] [--lr LR]
 [--weight-decay WEIGHT_DECAY]
 [--loss-log-interval LOSS_LOG_INTERVAL]
 [--image-log-interval IMAGE_LOG_INTERVAL]
 [--resume] [--checkpoint-dir CHECKPOINT_DIR]
 [--sample-dir SAMPLE_DIR] [--no-gpus]
```


### VAE  
PyTorch implementation of [Auto-Encoding Variational Bayes, arxiv:1312.6114](https://arxiv.org/abs/1312.6114)
