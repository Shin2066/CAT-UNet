# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:01:49 2021

@author: SHIN
"""

import cv2
import os
import numpy as np
from skimage import io, transform

dice = 0.0
fn = 0
fp = 0
mass = 0
normal = 0

gt = r"C:\Shin_kfold\other_size\480\kfold3"
predict = r"C:\Shin_kfold\predict\kfold3\TU_own480\TU_pretrain_R50-ViT-B_16_skip4_epo150_bs2_480_s0"
gt_file = os.listdir(gt)
predict_file = os.listdir(predict)
# print(predict_file)
for file1 in gt_file:
    for file2 in predict_file:
        if file1 == file2:
            s2 = cv2.imread((gt+"/"+file1),0)
            #print(s1)
            row, col = s2.shape[0], s2.shape[1]
            s1 = cv2.imread((predict+"/"+file2),0)
            #print(s1)
            d = []
            s = []
            for r in range(row):
                for c in range(col):
                    if s1[r][c] == s2[r][c]:  # 计算图像像素交集
                        s.append(s1[r][c])
            m1 = np.linalg.norm(s)
            m2 = np.linalg.norm(s1.flatten()) + np.linalg.norm(s2.flatten())
            #print(s)
            # print(m1)
            #print(m2)
        
            if(m1>0.0 and m2>0.0):
                d.append(2*m1/m2)
                msg = "第{}張圖的dice".format(file1) + str(2 * m1 / m2)
                if "mass" in msg:
                    mass+=1
                img_dice = (2 * m1 / m2)
                # print(img_dice)
                dice+=float(img_dice)
                
            if(m1==0.0 and m2==0.0):
                d.append(1.0)
                msg = "第{}張圖的dice=".format(file1) + str(1.0)
                img_dice = 1.0
                # print(img_dice)
                dice+=float(img_dice)
                if "mass" in msg:
                    mass+=1
                #print(msg)
                
            if(m1==0.0 and m2>0.0):
                msg = "第{}張圖的dice=".format(file1) + str(0.0)
                img_dice = 0.0
                d.append(0.0)
                print(msg)
                # print(img_dice)
                dice+=float(img_dice)
                if "mass" in msg:
                    mass+=1
                    fn+=1
                else:
                    fp+=1
                    
                #print(d)
            # if(m1>0.0 and m2==0.0):
            #     msg = "第{}張圖的dice=".format(file1) + str(0.0)
            #     img_dice = 0.0
            #     d.append(0.0)
            #     if "mass" in msg:
            #         mass+=1
            #     print(msg)
            #     dice+=float(img_dice)
            #     fp+=1
            #     print("111111111111111111111111111111")
                
print(fn)
print(fp)        
print("Mass總數=",mass)        
print("Dice=",(dice/638))        
print("FN=",(mass-fn)/(mass))
print("FP=",(638-mass-fp)/(638-mass))     
print("ACC=",(638-fn-fp)/638)       