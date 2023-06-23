from PIL import Image
import csv
import json

im1=Image.open('Level_1_Input_Data/wafer_image_1.png','r')
im2=Image.open('Level_1_Input_Data/wafer_image_2.png','r')
im3=Image.open('Level_1_Input_Data/wafer_image_3.png','r')
im4=Image.open('Level_1_Input_Data/wafer_image_4.png','r')
im5=Image.open('Level_1_Input_Data/wafer_image_5.png','r')


coordinate_list=[]
pix1=[]
pix2=[]
pix3=[]
pix4=[]
pix5=[]

def1=[]
def2=[]
def3=[]
def4=[]
def5=[]

with open('Level_1_Input_Data/input.json') as json_file:
    data=json.load(json_file)
    care_areas=data['care_areas']
    care_areas=care_areas[0]
    top_left=care_areas['top_left']
    bottom_right=care_areas['bottom_right']
    width=data['die']['width']
    height=data['die']['height']
    for x in range(top_left['x'],bottom_right['x']):
        for y in range(bottom_right['y'],top_left['y']):
            coordinate_list.append([x,y])
        
for i in coordinate_list:
    c=i[0],i[1]
    pix1.append(im1.getpixel(c))
    pix2.append(im2.getpixel(c))
    pix3.append(im3.getpixel(c))
    pix4.append(im4.getpixel(c))
    pix5.append(im5.getpixel(c))
  
#checking for dfects
def find_defect(j,image1,image2,image3):
    defect=[]
    for i in range(len(image1)):
        if image1[i]!=image2[i] and image1[i]!=image3[i]:
            defect.append((j,coordinate_list[i][0],height-coordinate_list[i][1]-1))
    return defect
           
def1=find_defect(1,pix1,pix2,pix3)
def2=find_defect(2,pix2,pix3,pix4)
def3=find_defect(3,pix3,pix4,pix5)
def4=find_defect(4,pix4,pix5,pix1)
def5=find_defect(5,pix5,pix1,pix2)




# #write into csv files

with open('defect_coordinates.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(def1)
    writer.writerows(def2)
    writer.writerows(def3)
    writer.writerows(def4)
    writer.writerows(def5)

    
    
    
        

        
        
