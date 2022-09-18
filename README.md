# CAT-UNet
CAT-UNet:Using CNN Attention Modules and TransUNet for Chest Lung Mass Segmentation from Chest X-ray Image

CAT-UNet:使用 CNN 注意力模組與 TransUNet 於胸部X光影像中肺腫瘤分割


# Architecture 
![CAT-UNet架構圖](https://user-images.githubusercontent.com/109962468/189515819-4d99263c-6f5f-4ab1-a03b-c9d0d9a84983.PNG)

# Usage
### 1. Download Google pre-trained ViT models ### 
[Get models in this link](https://console.cloud.google.com/storage/browser/vit_models;tab=objects?prefix=&forceOnObjectsSortingFiltering=false): R50-ViT-B_16


### 2.Prepare data ###
.
├── CAT-UNet
│   ├──datasets
│   │       └── dataset_*.py
│   ├──train.py
│   ├──test.py
│   └──...
├── model
│   └── vit_checkpoint
│       └── imagenet21k
│           ├── R50+ViT-B_16.npz
│           └── *.npz
└── data
    └──x-rays
        ├── train
        │   ├── images
        │   └── labels
        └── val
            ├── images
            └── labels

            
### 3.Environment ###
Please prepare an environment with python=3.6, and then use the command "pip install -r requirements.txt" for the dependencies.

### 4.Train/Test ###
Run train.py & test.py
