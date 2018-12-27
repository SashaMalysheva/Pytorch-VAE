from os import path

from setuptools import setup, find_packages

# Gets the long description from the README file.
_here = path.abspath(path.dirname(__file__))
with open(path.join(_here, 'README.md'), encoding='utf-8') as f:
    _long_description = f.read()

setup(
    name='Pytorch-VAE',
    version='0.0.1',

    description='This is an implementation of the VAE (Variational Autoencoder) for Cifar10',
    long_description=_long_description,
    long_description_content_type='text/markdown',

    url='git@github.com:SashaMalysheva/Pytorch-VAE',

    author='Malysheva Sasha',
    author_email='malyshevasasha777@gmail.com',

    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)