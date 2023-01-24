import cv2
import numpy as np

class Anterior_Posterior():
    
    def __init__(self, img):
        self.img = img
        self.detector_params = cv2.SimpleBlobDetector_Params()
        self.detector_params.filterByArea = True
        self.detector_params.maxArea = 1500
        self.detector = cv2.SimpleBlobDetector_create(self.detector_params)
        self.scale_percent = 30
        
    def image_process(self):
        try:
            width = int(self.img.shape[1] * self.scale_percent / 100)
            height = int(self.img.shape[0] * self.scale_percent / 100)
            dim = (width, height)
        
            resized = cv2.resize( self.img, dim, interpolation=cv2.INTER_AREA)
            gray_frame = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            _, img = cv2.threshold(gray_frame, 70, 255, cv2.THRESH_BINARY)
            img = cv2.erode(img, None, iterations=2)
            img = cv2.dilate(img, None, iterations=4)
            img = cv2.medianBlur(img, 5)
            keypoints = self.detector.detect(img)
            keypoints_coords = cv2.KeyPoint_convert(keypoints)
        
            '''cv2.imshow('Processed Image', img)
            cv2.imshow('Original Image', resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()'''

            #print(keypoints_coords)
            return keypoints_coords
        except Exception as e:
            print(e.args)
        