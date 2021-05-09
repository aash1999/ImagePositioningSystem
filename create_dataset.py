import image_slicer
import os
import shutil
from PIL import Image

#SLICE THE IMAGES INTO 20 GRIDS
for i in range(1,5):
    image_slicer.slice(str(i)+'.png', 19)
# shape (4,5)
count = 0
parent_path = "/Users/aakashsingh/Desktop/Create dataset"

#Move the image to Train and classification folders

for i in range(1,5):
    for j in range(1,6):
        count+=1
        print(count)
        new_dic_path = os.path.join('Train',str(count))
        path = os.path.join(parent_path,new_dic_path)
        mode = 0o777
        os.mkdir(path, mode)
        for file in os.listdir("/Users/aakashsingh/Desktop/Create dataset"):
            if file.endswith("_0"+str(i)+"_0"+str(j)+".png"):
                print(file)
                img_path = os.path.join(parent_path,file)
                shutil.move(img_path, path)

path = "/Users/aakashsingh/Desktop/Create dataset/Train"
for i in range(1,21):
    img_path = os.path.join(path,str(i))
    for file in os.listdir(img_path):
        print(i,' ',file)
        if(file != '.DS_Store'):

            img_temp_path = os.path.join(img_path,file)
            for k in range(1,360):
                Original_Image = Image.open(img_temp_path)
                rotated_image1 = Original_Image.rotate(k)
                img_name = file[:7]+str(k)+".png"
                #print(img_name)
                res_img_path = os.path.join(img_path,img_name)
                rotated_image1.save(res_img_path)
        else:
            pass
            print("False")
