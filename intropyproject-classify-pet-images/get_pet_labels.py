#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: René Olvera Romero
# DATE CREATED: 01.04.2024
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = dict()

    # Get a list of filenames from folder image_dir
    file_list = listdir(image_dir)

    for file_name in file_list:
        # Skip files that start with "."
        if file_name.startswith("."):
            continue
        
        # Retrieve the pet label from the filename, make it lower case, remove whitespaces and join with " "
        pet_label = " ".join(file_name.split("_")[:-1]).lower().strip()

        # Add file_name and label to dictionary if it doesn´t exist
        if file_name not in results_dic:
            results_dic[file_name] = [pet_label]
        else:
            print("** Warning: Key=", file_name, "already exists in results_dic with value=", results_dic[file_name])

    return results_dic

def main():
    ## Print 10 of the filenames from folder pet_images/
    filename_list = listdir("pet_images/")
    print("\nPrints 10 filenames from folder pet_images/")
    for idx in range(0, 10, 1):
        print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]))

    # Get the dictionary containing the file names and pet labels
    results_dic = get_pet_labels("pet_images/")

    # Print the result
    print("\nDictiorany of", len(results_dic), "files and pet labels:", results_dic)

# Call to main function to run the program
if __name__ == "__main__":
    main()
