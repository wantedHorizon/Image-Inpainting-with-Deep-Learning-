from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
from torch import nn, optim
import os
import matplotlib.pyplot as plt
import torch
from torchvision import datasets, transforms


image_size = 256
hole = 64
models_names = [[
  'input',      'original'],[
  'autoencoder','gan']]

rows = len(models_names)
cols = len(models_names[0])
bezzel = 5
canvas_width = image_size * cols + bezzel * cols
canvas_height = image_size * rows + bezzel * rows # + 50

current_image = 0
click_x = canvas_width/2
click_y = canvas_height/2

imgs = []
widgetimgs = []
show = []
showing = 1
if showing == 0:
  for i in range(140):
    show.append(i)
elif showing == 1:
  show = [17,23,25,29,30,31,34,36,37,38,39,44,46,47,50,72,90,99,100,105,118,120,143,147]

def key(e):
  if e.keysym == 'space':
    next_image()

def next_image():
  global current_image
  current_image+=1
  if current_image >= len(show):
    current_image = 0
  for row in range(rows):
    for col in range(cols):
      print current_image
      widget.itemconfig(widgetimgs[row][col],image=imgs[current_image][row][col])


tkroot = Tk()
tkroot.title('hole inpainting')
widget = Canvas(tkroot,width=canvas_width,height=canvas_height)

widget.bind("<KeyPress>", key)

for i in show:
  ezerarr2 = []
  for row in range(rows):
    ezerarr1 = []
    for col in range(cols):
        ezerarr1.append(ImageTk.PhotoImage(Image.open('images/'+models_names[row][col]+'/img' + str(i + 1) + '.png')))
    ezerarr2.append(ezerarr1)
  imgs.append(ezerarr2)

bezzel = 5
for row in range(rows): # 2
  ezerarr = []
  for col in range(cols): # 4
    ezerarr.append(widget.create_image((image_size/2)*(col*2+1) + bezzel * (col+1), (image_size/2)*(row*2+1) + bezzel*(row+1), image=imgs[current_image][row][col]))
    widget.create_rectangle((image_size/2)*(col*2+1) + bezzel * (col+1) - 42, (image_size/2)*(row*2) + bezzel * (row+1) - 10 + 20,
                            (image_size/2)*(col*2+1) + bezzel * (col+1) + 42, (image_size/2)*(row*2) + bezzel * (row+1) + 10 + 20, fill='#3f3f3f')
    widget.create_text(((image_size/2)*(col*2+1) + bezzel * (col+1), (image_size/2)*(row*2) + bezzel * (row+1) + 20), text=models_names[row][col], fill="white")
  widgetimgs.append(ezerarr)



widget.pack(expand=YES, fill=BOTH)
widget.focus_set()


tkroot.mainloop()
