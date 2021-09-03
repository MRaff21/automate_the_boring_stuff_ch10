#!python3
#renameDates.py - Renames filesnames with american MM-DD-YYYY date format to European DD-MM-YYYY

import shutil, os, re

# Create a regex that matches files with the American date format.

date = "get this at home"

   # TODO: Loop over the files in the working directory.
   
for folder_name, sub_folders, file_names in os.walk("/home/lab/Documents/renamingFolder"):
	print('The current folder is ', folder_name)
	
	for sub_folder in sub_folders:
		print('SUBFOLDER OF' , folder_name , ': ', sub_folder)
	
	for file_name in file_names:
		print('FILE INSIDE', folder_name)
	print('')
	

   # TODO: Skip files without a date.

   # TODO: Get the different parts of the filename.

   # TODO: Form the European-style filename.

   # TODO: Get the full, absolute file paths.

   # TODO: Rename the files.
