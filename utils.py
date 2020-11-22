import os
import cv2
import numpy as np
from sklearn.decomposition import TruncatedSVD

class GhostTown:
  def __init__(self, video):
    self.video = video
    assert type(self.video) == str, 'give the filename of the video'
    assert self.video.split('.')[-1].lower() in ['avi','mp4','mpeg4','webm'], 'give the filename in proper format'
    assert os.path.exists(video) , 'file not exist'

    self.cap = cv2.VideoCapture(video)
    ret,self.frame = self.cap.read()
    if self.frame.shape[0] * self.frame.shape[1] > 512*512:
      self.istack = np.array([[0]*(512*512)])
    else:
      self.istack = np.array([[0]*(self.frame.shape[0]*self.frame.shape[1])])
    
  def preprocess(self,frame):
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if frame.shape[0] * frame.shape[1] > 512*512:
      resized_frame = cv2.resize(frame,(512,512),interpolation=cv2.INTER_CUBIC)
      return resized_frame
    return gray_frame
  
  def imageMatrix(self):
    while True:
      ret,frame = self.cap.read()

      if ret:
        image = self.preprocess(frame)
        flatten_arr = image.flatten()
        flatten_arr = flatten_arr[np.newaxis,:]
        self.istack = np.concatenate((self.istack,flatten_arr))
      else:
        break
    imgMatrix = self.istack[1:,:].T
    return imgMatrix
  
  def background(self):
    svd = TruncatedSVD(n_components=2)
    imgMat = self.imageMatrix()
    transformed_img = svd.fit_transform(imgMat)
    background_img = transformed_img[:,0].reshape((self.frame.shape[0],self.frame.shape[1]))
    return background_img

