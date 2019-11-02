import math
from graph import *

def ellipse(x0, y0, a, b): #возвращает массив точек для построения эллипса
    lst = []
    fii = 0.01
    c = (a*a-b*b)**(1/2)
    exc = c/a
    point(x0+a, y0)
    while fii <= 360:
        ro = (a - exc*c)/(1+exc*math.cos(fii))
        x = math.floor(x0 + c + ro*math.cos(fii))
        y = math.floor(y0 + (b*(1-((x-x0)/a)**2)**(1/2))*(math.sin(fii)/math.fabs(math.sin(fii))))
        temp = (x, y)
        lst.append(temp)
        fii = fii + 0.02
    return lst

def car (x0, y0):
    lst = ellipse(x0, y0+35, 20, 5) #выхлопная труба
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    polygon(lst)
    brushColor(0, 204, 255)
    rectangle(x0, y0, x0+210, y0+40) 
    rectangle(x0+30, y0, x0+150, y0-27)
    brushColor(213, 246, 255)
    rectangle(x0+45, y0-5, x0+80, y0-22) #окна
    rectangle(x0+100, y0-5, x0+135, y0-22)
    brushColor(0, 0, 0)
    lst1 = ellipse(x0+30, y0+40, 20, 15) #колеса
    lst2 = ellipse(x0+170, y0+40, 20, 15)
    polygon(lst1) 
    polygon(lst2)

def car2 (x0, y0):
    lst = ellipse(x0, y0+35, 20, 5) #выхлопная труба
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    polygon(lst)
    brushColor(0, 204, 255)
    rectangle(x0, y0, x0-210, y0+40) 
    rectangle(x0-30, y0, x0-150, y0-27)
    brushColor(213, 246, 255)
    rectangle(x0-45, y0-5, x0-80, y0-22) #окна
    rectangle(x0-100, y0-5, x0-135, y0-22)
    brushColor(0, 0, 0)
    lst1 = ellipse(x0-30, y0+40, 20, 15) #колеса
    lst2 = ellipse(x0-170, y0+40, 20, 15)
    polygon(lst1) 
    polygon(lst2)

def car3 (x0, y0):
    lst = ellipse(x0, y0+11, 6, 1.5) #выхлопная труба
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    polygon(lst)
    brushColor(0, 204, 255)
    rectangle(x0, y0, x0-65, y0+13) 
    rectangle(x0-10, y0, x0-45, y0-9)
    brushColor(213, 246, 255)
    rectangle(x0-14, y0-1.5, x0-25, y0-7) #окна
    rectangle(x0-31, y0-1.5, x0-42, y0-7)
    brushColor(0, 0, 0)
    lst1 = ellipse(x0-10, y0+13, 6, 5) #колеса
    lst2 = ellipse(x0-56, y0+13, 6, 5)
    polygon(lst1) 
    polygon(lst2)

def buildings2(x0, y0):
    penSize(0)
    brushColor(147, 167, 172)
    rectangle(x0, y0, x0+70, y0+245)
    brushColor(147, 172, 167)
    rectangle(x0+91, y0+14, x0+161, y0+250)
    brushColor(183, 200, 196)
    rectangle(x0+49, y0+49, x0+126, y0+294)
    brushColor(219, 227, 226)
    rectangle(x0+245, y0, x0+322, y0+247)
    brushColor(111, 145, 138)
    rectangle(x0+224, y0+63, x0+294, y0+301)

def buildings1(x0, y0):
    penSize(0)
    brushColor(147, 167, 172)
    rectangle(x0, y0, x0-70, y0+245)
    brushColor(147, 172, 167)
    rectangle(x0-91, y0+14, x0-161, y0+250)
    brushColor(183, 200, 196)
    rectangle(x0-49, y0+49, x0-126, y0+294)
    brushColor(219, 227, 226)
    rectangle(x0-245, y0, x0-322, y0+247)
    brushColor(111, 145, 138)
    rectangle(x0-224, y0+63, x0-294, y0+301)

def background0(x0,y0):
    penSize(0)
    brushColor(37,37,37)
    rectangle(x0+400,y0,x0+500,y0+100)
    brushColor(79,79,79)
    rectangle(x0+420,y0,x0+480,y0+100)
    brushColor(25,25,25)
    rectangle(x0+420,y0,x0+480,y0+30)

    brushColor(37,37,37)
    rectangle(x0+300,y0,x0+398,y0+100)
    brushColor(9,9,9)
    rectangle(x0+300,y0+50,x0+320,y0+100)
    rectangle(x0+330,y0,x0+380,y0+100)
    brushColor(105,105,105)
    rectangle(x0+50,y0,x0+300,y0+100)
    brushColor(30,30,30)
    rectangle(x0+200,y0+10,x0+300,y0+100)
    brushColor(125,125,125)
    rectangle(x0+255,y0,x0+300,y0+100)
    brushColor(13,13,13)
    rectangle(x0+250,y0+50,x0+280,y0+100)
    brushColor(126,126,126)
    rectangle(x0,y0,x0+50,y0+100)
    brushColor(40,40,40)
    rectangle(x0,y0+50,x0+50,y0+100)
    brushColor(63,63,63)
    rectangle(x0+50,y0+50,x0+90,y0+100)
    
    
    
def background(x0, y0):
    penSize(0)
    brushColor(83, 108, 103)
    rectangle(0, y0, x0, 1000)

def background1(x0, y0):
    penColor(255,255,255)
    penSize(2)
    brushColor(183, 196, 200)
    rectangle(180, 90, x0, y0)

def background2(x0, y0):
    penColor(255,255,255)
    penSize(2)
    brushColor(183, 196, 200)
    rectangle(0, 100, x0, y0+20)

def big_cloud(x0, y0):
    lst = ellipse(x0, y0, 220, 50)
    penSize(0)
    penColor(168, 186, 186)
    brushColor(168, 186, 186)
    polygon(lst)

def big_cloud1(x0, y0):
    lst = ellipse(x0, y0, 150, 33)
    penSize(0)
    penColor(168, 186, 186)
    brushColor(168, 186, 186)
    polygon(lst)
    

def clouds():
    big_cloud(110, 80)
    big_cloud(325, 200)
    big_cloud(80, 290)
    penColor(156, 180, 178)
    for x in range (155, 330): #там где облака полупрозрачны 
        for y in range (30, 85):
            if (((x-375)/220)**2+((y-35)/50)**2 <= 1) and (((x-110)/220)**2 + ((y-80)/50)**2 <= 1):
               point(x, y) 
def clouds1():
    big_cloud1(450, 150)  

background0(0, 0)
background(800, 350)
background1(800, 350)
clouds1()
buildings1(535, 103)
background2(288, 352)
buildings2(-60, 122)
penSize(0)
car (40, 460)
car2(460,530)

car3(460, 430)
car3(360, 410)
car3(255, 420)
car3(90, 410)

