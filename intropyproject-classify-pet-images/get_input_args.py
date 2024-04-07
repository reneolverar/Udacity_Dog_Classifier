#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#
# PROGRAMMER: René Olvera Romero
# DATE CREATED: 31.03.2024
# REVISED DATE:
# PURPOSE: Create a function that retrieves the following 3 command line inputs
#          from the user using the Argparse Python module. If the user fails to
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument
#       collection that you created with this function
#
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module to created and defined these 3 command line arguments. If
    the user fails to provide some or all of the 3 arguments, then the default
    values are used for the missing arguments.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    """
    # Create Argument Parser
    parser = argparse.ArgumentParser()

    # Argument 1: Image Folder
    parser.add_argument('--dir', type = str, default = 'pet_images/', help = 'Path to image folder')

    # Argument 2: CNN Model Architecture
    parser.add_argument('--arch', type = str.lower, default = 'vgg', choices=['vgg', 'alexnet', 'resnet'], help = 'CNN Model Architecture')

    # Argument 3: Text File with Dog Names
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt', help = 'Text file with dog names')

    return parser.parse_args()

def main():
    # Get the input arguments
    in_arg = get_input_args()

    # Print the input arguments
    print("Command Line Arguments:\n dir = ", in_arg.dir, "\n arch = ", in_arg.arch, "\n dogfile = ", in_arg.dogfile)

# Call to main function to run the program
if __name__ == "__main__":
    main()