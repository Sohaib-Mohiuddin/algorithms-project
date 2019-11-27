import os
from os import path
import sys

with open('original/original.txt', 'r') as myfile:
    data = myfile.read()

DIR = 'compare_with_original/'
print([name for name in os.listdir(DIR)])