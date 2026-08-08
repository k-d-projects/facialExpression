from django.shortcuts import render,redirect
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import requests
import subprocess
from django.http import HttpResponse
import sys
from myapp.models import Imgsave1

import time


def handel_phot(f):
    with open('myapp/static/saveimg/upload'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
 

            img1=cv2.imread('myapp/static/saveimg/upload'+f.name)
            plt.imshow(img1[:,:,::-1])
            res=DeepFace.analyze(img1,actions=['emotion'])
            print(res)
        
            sourceFile = open('python.txt', 'w')
            print(res, file = sourceFile)
            sourceFile.close()

            
            file_to_save=open('python.txt','r').read()
            new_entry=Imgsave1(value=file_to_save)
            new_entry.save()
            

            
    



            

            

            

            
            

            
    


