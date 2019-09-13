# OpenCV-face-detection
OpenCV face detection<br>
This program needs a database(.yml file) which contains the face data. This program won't run on itself.<br> 
It needs a recognizer program which trains the data and creates a '.yml' file.<br>
You will also need a lot of images of people you want to be detected by the program as the model needs a lot of data to improve the accuracy of the model.<br>Arrange atleast 50 images for better results.<br>
update(13/9/19): I have added the recognition program in the git.<br>
1)now to use the programs first create a folder(lets say FR) and place these two files inside folder. Name anything u want.<br>
2)Create a new folder named 'images'.<br>
3)Inside this folder create a folder and give it the name of a person. lets say 'harsh'.<br>
4)paste the images(more the better) inside the this folder named 'harsh'. and then run the recognition program.<br>
5)'.yml' file will be created automatically.. do not try to edit this file!<br>
6)Now run the 'CameraTest2' file. You will need a webcam for this file to work or it will throw some error.<br>
7)A frame will open where webcam will show its input.<br>
8)If face is recognised then the name will appear above the detected face.<br>
