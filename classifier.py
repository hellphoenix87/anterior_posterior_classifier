import cv2
from a_p_class import Anterior_Posterior

def image_classfier(image):
    try:
        open_image = cv2.imread(image, cv2.IMREAD_UNCHANGED)
        proccess_image = Anterior_Posterior(open_image).image_process()
        #print(proccess_image)
    
        if len(proccess_image) > 0:
            #print ('Anterior')
            return 'Anterior'
        else:
            #print('Posterior')
            return 'Posterior'
    except Exception as e:
        print(e.args)

image_classfier('anterior.jpg')