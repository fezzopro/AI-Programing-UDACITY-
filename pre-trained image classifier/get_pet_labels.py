#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Felix KAMANA
# DATE CREATED: 08/08/2021
# REVISED DATE: 09/08/2021
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
#     print(image_dir)
    results_dic = dict()
    
    if image_dir != None:
        
        try:
            # Read All The Files in the directory
            files_found = listdir(image_dir)
            
            #print("\nPrints 10 filenames from folder pet_images/")
            #for idx in range(0, len(files_found), 1):
            #    print("{:2d} file: {:>25}".format(idx + 1, files_found[idx]) )
        except IsADirectoryError as Err:
            print('Error: ' + Err)
            quit()

        # For every file in the directory, check if it doesn't start with a .
        for file_index in range(0, len(files_found), 1):
            
            pet_labels = []

            if files_found[file_index][0] != ".":
                if files_found[file_index] not in results_dic:
                    
                    tmp_label = ' '.join(files_found[file_index].split("_")[:-1]).lower().strip()
                    pet_labels.append(tmp_label)
                    results_dic[files_found[file_index]] = pet_labels
    
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    
    return results_dic