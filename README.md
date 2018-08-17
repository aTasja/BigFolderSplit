# BigFolderSplit

Task to create a Python script to move images of same file name (different extension), in batch of 5000:

I have a folder with a very large quantities of files (over 88 000). The folder is REALLY slow because of the quantity of files found there.

There are 2 to 3 versions of the same file with exact same filename (ex: MyFile-1.eps, MyFile-1.jpg, MyFile-1.zip). 

I would like to have a PYTHON script that would:

1- Create a new folder, named (Batch1, Batch2, Batch3, Batch4, etc.)

2- Move 5000 items of to each folder (1 item = 2 or 3 files of the same file name, with different extension (.eps, .jpg and sometimes .zip).

Solution
-----------------------
Place script to folder with a very large quantities of files and run it.
All files with the same filenames and different extensions will be moved to appropriate folders like: 
"../folder-with-a-very-large-quantities-of-files/file-name/moved-files"

Script may be used again. In such case all files with new filenames will be moved in new folders.
If some folder with moved files has already contain file which have to be moved (names of files equal) script will print worning message. Such files will not be moved.

<a href="url"><img src="https://github.com/aTasja/BigFolderSplit/blob/master/start.png" align="left" height="250" width="250"></a> <a href="url"><img src="https://github.com/aTasja/BigFolderSplit/blob/master/Finish.png" align="left" height="250" width="250"></a> <a href="url"><img src="https://github.com/aTasja/BigFolderSplit/blob/master/Finish-Folder.png" align="left" height="250" width="250"></a>



