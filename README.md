# GhostTown

Implementation of GhostTown mode of Insta360 camera. 

Have you ever experienced a problem of lot of moving pedestrians when you are trying to take a picture of Monuments? This project is intended to solve that problem.

Recently Insta360 OneX2 cam has released a feature called Ghost Town. which actually takes a video of less than a minute and extracts the background image by removing the moving objects from each frame. The background image is called ground-truth image of that video. 

The fundemental concept behind the feature is a Unsupervised Machine learning technique based upon Mathematics.

In this project, I tried to replicate the same feature as extracting information from the video footage of CCTV or any stable cameras and reproduce the Ground-Truth image also known as Background image. 

The code for teh concept is in util.py file. 
To reproduce the results, Run main.py which requires two arguments,

"--input" The input video file name

"--output" The backgroung image name to be created 
