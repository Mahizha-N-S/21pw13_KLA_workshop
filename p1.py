from PIL import Image
im1=Image.open('Level_1_Input_Data/wafer_image_1.png','r')
im2=Image.open('Level_1_Input_Data/wafer_image_2.png','r')
im3=Image.open('Level_1_Input_Data/wafer_image_3.png','r')
im4=Image.open('Level_1_Input_Data/wafer_image_4.png','r')
im5=Image.open('Level_1_Input_Data/wafer_image_5.png','r')


import json
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
    
#checking for defects
def find_defect(image1,image2):
    defect=[]
    for i in range(len(image1)):
        if image1[i]!=image2[i]:
            defect.append(coordinate_list[i])
    return defect

defect_list=[]        
for x in [pix1,pix2,pix3,pix4,pix5]:
    for y in [pix1,pix2,pix3,pix4,pix5]:
        while(x!=y):
            defect_list.append(find_defect(x,y))
            
        

        
        
