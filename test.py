#!/usr/bin/python
#coding:utf-8
import os, json
import sys

def add(a, b):
    return a + b

def get_os():
    print(commands.getoutput("uname -a"))

if __name__ == '__main__':
    get_os()
