#!/bin/python3
import sys
import os
from image_ptr import ImagePtr
from PIL import Image

def main():
    # Check to see if it's directory
    if os.path.isdir(sys.argv[1]):
        # get all files in the current directory
        files = [f for f in os.listdir(sys.argv[1]) if os.path.isfile(f)]
        # append each image files into list
        ImagePtr.append(files)
 
