import cv2 as cv
import os


def face_detect(img):
    gary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #opencv management
    face_detect = cv.CascadeClassifier('/Users/liululin/PycharmProjects/pythonProject16/venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gary,1.01,150,0,(10,10),(400,400))
    #根据xywh，进行opencv算法
    for x,y,w,h in face:
        if w>=128 and h>=128:
            cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)

    i = 1
    for face__ in face:
        img_ = img[face__[1]:face__[1] + face__[3], face__[0]:face__[0] + face__[2]]
        # save the images
        # It makes sure that you can save many images at the same time if there are more than one face in the photo
        i = i + 1
        cv.imwrite(target_path2, img_)

#You should use your own path based on your computer
source_path = '/Users/liululin/Downloads/archive (3)/images/'
target_dir_name = 'target'
target_path = source_path + target_dir_name
if not os.path.exists(target_path):
    os.makedirs(target_path)
#the number "852" can be changed
for i in range(852):
    target_path2 = target_path +'/'+ 'NEW' + str(i) +'.png'
    file_path = source_path + 'maksssksksss' + str(i) + '.png'
    img = cv.imread(file_path)
    face_detect(img)

