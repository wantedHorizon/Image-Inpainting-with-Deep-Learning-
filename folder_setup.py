import torch
import numpy as np
from PIL import Image
import os
import random
import time
import scipy.misc
import scipy.ndimage
import cv2



def add_hole(image,hole_size):
  image[image.shape[0] / 2 - hole_size / 2:image.shape[0] / 2 + hole_size / 2,
  image.shape[1] / 2 - hole_size / 2:image.shape[1] / 2 + hole_size / 2] = np.random.rand(hole_size,hole_size,3)*255
  return image

def get_hole(images,hole_size):
  x = images[images.shape[0] / 2 - hole_size / 2:images.shape[0] / 2 + hole_size / 2,images.shape[1] / 2 - hole_size / 2:images.shape[1] / 2 + hole_size / 2]
  return cv2.resize(x, dsize=(256, 256), interpolation=cv2.INTER_CUBIC)

def delete_black_and_white(folder):
  images_names = os.listdir(folder)
  for index, image_name in enumerate(images_names):
    try:
      if len(np.array(Image.open(folder + image_name)).shape) != 3:
        os.remove(folder + image_name)
        print index
    except:
      os.remove(folder + image_name)





def setup(folder_from, folder_to,hole_size,folder_name,train_num):
  folder_to2 = os.path.join(folder_to,folder_name)
  try:
    os.mkdir(folder_to2)
    os.mkdir(os.path.join(folder_to2,'checkpoint'))
    os.mkdir(os.path.join(folder_to2,'dataset'))
    os.mkdir(os.path.join(folder_to2,'generated'))
    # folder_to2 = os.path.join(folder_to2, 'facades')
    os.mkdir(os.path.join(folder_to2, 'dataset/facades'))
    os.mkdir(os.path.join(folder_to2,'dataset/facades/train'))
    os.mkdir(os.path.join(folder_to2, 'dataset/facades/test'))
    os.mkdir(os.path.join(folder_to2, 'dataset/facades/train/a'))
    os.mkdir(os.path.join(folder_to2, 'dataset/facades/train/b'))
    os.mkdir(os.path.join(folder_to2, 'dataset/facades/test/a'))
    os.mkdir(os.path.join(folder_to2, 'dataset/facades/test/b'))
  except: pass
  images_names = os.listdir(folder_from)
  for index in range(len(images_names)):
    if index % (len(images_names)/100) == 0:
      print(str(index/(len(images_names)/100))+'%')
    image = np.array(Image.open(folder_from + images_names[index]))
    holy =np.copy(image)
    holy = add_hole(holy,hole_size)

    if index < train_num:
      scipy.misc.imsave(folder_to2 + '/dataset/facades/train/a/image' + str(index) + '.png', holy)
    else:
      scipy.misc.imsave(folder_to2 + '/dataset/facades/test/a/image' + str(index) + '.png', holy)

    if index < train_num:
      scipy.misc.imsave( folder_to2 + '/dataset/facades/train/b/image'+str(index)+'.png',image)
    else:
      scipy.misc.imsave(folder_to2 + '/dataset/facades/test/b/image' + str(index) + '.png', image)









path = os.path.expanduser('~/../../media/rotem/disk1/datasets/')
dataroot = os.path.expanduser(path + 'places/imagesPlaces205_resize/data/vision/torralba/deeplearning/images256/b/ezer_badlands/badlands/')
data_to = path+'places/'


# delete_black_and_white(dataroot)
setup(dataroot,data_to,64,'badlands_hole4',12000)
















# from PIL import Image
# im = Image.fromarray(A)
# im.save("your_file.jpeg")
