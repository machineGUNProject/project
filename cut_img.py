import find_pos
import shutil
from PIL import Image
import os

class img_devide():
    def __init__(self, img_path, i, j, a, x, d, leng, img_num):
        self.img_path = img_path
        self.path = ''
        self.call_num = 0
        self.lengh = 0
        self.width = 0
        self.height = 0
        self.img = ''
        self.i = i
        self.j = j
        self.a = a
        self.x = x
        self.d = d
        self.leng = leng
        self.img_num = img_num

    def devide_img(self):
        area = (self.i, self.j, self.a, self.x)
        cropped_img = self.img.crop(area)
        cropped_img.save("C:\\Users\\Ai\\Desktop\\img_cut\\first_cut\\" + str(self.d)+'.jpg')
        self.call_num+=1

    def height_img(self):
        area = ((self.width/3)*(self.j-1) , 0, ((self.width/3)*self.j), self.height)
        cropped_img = self.img.crop(area)
        cropped_img.save(self.img_path + str(self.d+1) + '.jpg')

    def wrong_img(self):
        area = ((self.width/(self.leng +1))*(self.d-self.img_num) , 0, ((self.width/(self.leng +1))*(self.d -self.img_num + 1)), self.height)
        cropped_img = self.img.crop(area)
        cropped_img.save("C:/Users/Ai/Desktop/final_cut/final_img/" + str(self.d)+'.jpg')

    def check_img(self):
        self.imgcheck = Image.open(self.img_path)
        self.width = self.imgcheck.size[0]
        self.height = self.imgcheck.size[1]
        if self.width // self.height >= 1.3 : # 2개 이상의 글자가 있을 경우
            return 1
        else : # 제대로 짤렸을 경우
            return 0

    def set_image(self):
        self.img = Image.open(self.img_path)
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        #print(self.width)
        #print(self.height)
        self.lengh = int(self.width / self.height)
        return self.height, self.width

    def pass_image(self):
        area = (self.i, self.j, self.width, self.height)
        cropped_img = self.img.crop(area)
        cropped_img.save("C:/Users/Ai/Desktop/final_cut/final_img/" + str(self.d)+'.jpg')
        self.call_num+=1

    def remove_file(self):
        try:
            shutil.rmtree('C:/Users/Ai/Desktop/img_cut/first_cut')
            shutil.rmtree('C:/Users/Ai/Desktop/final_cut/final_img')
        except:
            pass

    def add_dir(self) :
        try :
            os.mkdir('C:/Users/Ai/Desktop/img_cut/first_cut')
            os.mkdir('C:/Users/Ai/Desktop/final_cut/final_img')
        except:
            pass


def path_what(path):
    length = find_pos.position_num(path)
    a = 0
    j = 0
    z = 0
    x = 0
    d = 0
    leng = 0
    img_num = 0
    h = img_devide(path, a, j, z, x, d, leng, img_num)
    h.remove_file()
    h.add_dir()
    #find_pos의 position_find 함수 불러오기
    if length == 0 or (length == 1 and (h.set_image()[1] / h.set_image()[0]) >= 1.3):
        leng = h.set_image()[1] // h.set_image()[0]
        print(leng)
        for re in range(0,  leng+1) :
            h = img_devide(path, a, j, h.set_image()[0], h.set_image()[1], re, leng, img_num)
            h.set_image()
            h.wrong_img()

    else :
        d = 0
        for i in range(0, length):
            x1, y1 = find_pos.position_find(path, i)
            print(x1)
            print(y1)

            #좌표로 여백 자르기

            a = x1[0]
            j = x1[1]
            z = y1[0]
            x = y1[1]
            h = img_devide(path, a, j, z, x, d, leng, img_num)
            h.set_image()
            h.devide_img()
            d+=1
        for i in range(0, length):
            a = 0
            j = 0
            z = 0
            x = 0

            path = "C:/Users/Ai/Desktop/img_cut/first_cut/" + str(i) + ".jpg"
            h = img_devide(path, a, j, z, x, img_num, leng, img_num)
            h.set_image()
            final_img_check = h.check_img()
            if final_img_check == 0:
                h.pass_image()

            else :
                leng = h.set_image()[1] // h.set_image()[0]
                print(leng)
                a = 0
                j = 0
                for re in range(img_num,  img_num + leng + 1) :
                    h = img_devide(path, a, j, h.set_image()[0], h.set_image()[1], re, leng, img_num)
                    h.set_image()
                    h.wrong_img()
                img_num = leng

            img_num +=1




"""
for i in range(0, length):
    length = find_pos.position_num("C:/Users/Ai/Desktop/img_position/22.jpg" + str(i))
    h = img_devide("C:/Users/Ai/Desktop/img_position/22.jpg", a, j, z, x, d)
    h.set_image()
    if
"""
"""
a = 0
j = 0
z = 0
x = 0
d = 0
for j in range(1, 4):
    h = img_devide("C:/Users/Ai/Desktop/img_position/", a, j, z, x,d)
    h.set_image()
    h.height_img()
    z+=1
    x+=1
    d+=1
"""
