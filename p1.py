from PIL import Image
im=Image.open('Level_1_Input_Data/wafer_image_1.png','r')
pix_val=list(im.getdata())