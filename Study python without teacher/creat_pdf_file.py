'''
2020.3.19记录：
convert指令无法正常操作，需要详细学习。



'''




import os

file_path=os.path.join("d://",'IDM Download','1')
def CompressImage(image_name):
    os.system("convert -resize\"4000x6000\" %s %s" % (image_name,image_name))

def CompressAll():

   

    for each_image in os.listdir(file_path):
            if each_image.endswith('jpg'):

                CompressImage(each_image)

          

CompressAll()

os.system("convert*.jpg book.pdf")