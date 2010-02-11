#!/bin/sh

## setup directories
mkdir downloads
cd downloads

## install django
wget http://www.djangoproject.com/download/1.1.1/tarball/
tar zxvf Django-1.1.1.tar.gz
cd Django-1.1.1
sudo python setup.py install
cd ../

## install boto
wget http://boto.googlecode.com/files/boto-1.9b.tar.gz
tar zxvf boto-1.9b.tar.gz
cd boto-1.9b
sudo python setup.py install

## reset
cd ../../
