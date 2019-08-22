#!/usr/bin/env python
from PIL import Image
import sys,os

def organizeGrid(inputData):
  width = 0
  height = 100*len(inputData)
  lengths = []
  for item in inputData:
    lengths.append(len(item))
  print lengths
  lengths.sort()
  width = lengths[-1] * 100
  outputData = []
  outputData.append(width)
  outputData.append(height)
  return outputData
   

textToPuppy = sys.argv[1]
inputData = textToPuppy.split(',')

geometry = organizeGrid(inputData)  

til = Image.new("RGB",(geometry[0],geometry[1]),(255, 255, 255))

row = 0
for item in inputData:
  textOffSet = (geometry[0]/100 - len(item))/2
  print textOffSet
  col = 0
  for letter in item:
    if letter == " ":
      letter = "space"
    im = Image.open("./cmsswConfig/" + letter + ".png")
    im = im.resize((100,100), Image.ANTIALIAS)
    coordinateX = (textOffSet + col)*100   
    coordinateY = row*100
    print coordinateX
    print coordinateY
    til.paste(im, (coordinateX, coordinateY))
    col = col + 1
  row = row + 1   

til.show()
