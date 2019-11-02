import math
from graph import *

#фон
penColor(151, 133, 17)
penSize(0.5)
brushColor(128, 102, 0)
rectangle(0, 600, 500, 250)
brushColor(85,68,0)
rectangle(0,0, 500, 250)

def window(x0,y0):
    penColor(192, 251, 249)
    brushColor(192, 251, 249)
    rectangle(x0,y0,x0+190, y0+225)
    brushColor(106, 197, 223)
    rectangle(x0+9,y0+7,x0+87, y0+80)
    rectangle(x0+98,y0+7,x0+180, y0+80)
    rectangle(x0+9,y0+95,x0+87, y0+220)
    rectangle(x0+98,y0+95,x0+180, y0+220)

def ellipse(x0, y0, a, b, alf): #возвращает массив точек для построения эллипса
    lst = []
    fii = 0.01
    c = (a*a-b*b)**(1/2)
    exc = c/a
    point(x0+a, y0)
    while fii <= 360:
        ro = (a - exc*c)/(1+exc*math.cos(fii))
        x = math.floor(x0 + c + ro*math.cos(fii))
        y = math.floor(y0 + (b*(1-((x-x0)/a)**2)**(1/2))*(math.sin(fii)/math.fabs(math.sin(fii))))
        new_x = x*math.cos(alf)-y*math.sin(alf)
        new_y = x*math.sin(alf)+y*math.cos(alf)
        if alf==0:
            temp = (x, y)
        else:
            temp = (new_x, new_y)
        lst.append(temp)
        fii = fii + 0.01
    return lst
def ellipsev(x0, y0, a, b): #возвращает массив точек для построения эллипса
    lst = []
    fii = 0.01
    c = (a*a-b*b)**(1/2)
    exc = c/a
    point(x0+a, y0)
    while fii <= 360:
        ro = (a - exc*c)/(1+exc*math.cos(fii))
        x = math.floor(x0 + c + ro*math.cos(fii))
        y = math.floor(y0 + (b*(1-((x-x0)/a)**2)**(1/2))*(math.sin(fii)/math.fabs(math.sin(fii))))
        temp = (y, x)
        lst.append(temp)
        fii = fii + 0.01
    return lst
def cat(x0,y0):
    penColor(3, 3, 3)
    penSize(0.1)
    brushColor(200, 113, 55)#body
    lst0 = ellipse(x0+280, y0-100, 100,34,-50)#хвост
    polygon(lst0)
    lst = ellipse(x0, y0, 150,75,0)#туловище
    polygon(lst)
    lst1 = ellipse(x0-96, y0+54, 40, 22,0)
    polygon(lst1)#передняя лапа нижняя
    lst2 = ellipsev(y0+24, x0-154, 30,18)# передняя лапа
    polygon(lst2)
    circle(x0-140,y0-18,56)# голова
    circle(x0+106,y0+30,46)#задняя лапа верх
    lst3 = ellipsev(y0+84, x0+148, 40,16)# задняя лапа
    polygon(lst3)
    #уши внешнее
    polygon([(x0-184,y0-44),(x0-190,y0-90),(x0-152,y0-64),(x0-184,y0-44)])
    polygon([(x0-96,y0-44),(x0-90,y0-90),(x0-128,y0-64),(x0-96,y0-44)])
    #уши внутренние
    brushColor(222, 170, 135)
    polygon([(x0-182,y0-50),(x0-186,y0-84),(x0-158,y0-64),(x0-182,y0-50)])
    polygon([(x0-98,y0-50),(x0-94,y0-84),(x0-122,y0-64),(x0-98,y0-50)])
    brushColor(136, 170, 0)#глаза
    circle(x0-166,y0-20,16)
    circle(x0-114,y0-20,16)
    brushColor(3, 3, 3)#зрачки
    lst6 = ellipsev(y0-20, x0-162, 15,2)
    polygon(lst6)
    lst7 = ellipsev(y0-20, x0-110, 15,2)
    polygon(lst7)
    brushColor(255, 199, 165)#нос
    polygon([(x0-145,y0),(x0-133,y0),(x0-139,y0+6),(x0-145,y0)])
    line(x0-139,y0+6,x0-139,y0+16)
    polyline([(x0-139,y0+16),(x0-143,y0+20),(x0-149,y0+19)])
    polyline([(x0-139,y0+16),(x0-135,y0+20),(x0-129,y0+19)])
    #усы
    #left
    polyline([(x0-150,y0+6),(x0-156,y0+5),(x0-162,y0+4),(x0-168,y0+3),
              (x0-176,y0+2),(x0-200,y0+1)])
    polyline([(x0-150,y0+10),(x0-156,y0+9),(x0-162,y0+8),(x0-168,y0+8),
              (x0-188,y0+9),(x0-200,y0+10)])
    polyline([(x0-150,y0+14),(x0-156,y0+14),(x0-162,y0+15),(x0-168,y0+16),
              (x0-176,y0+17),(x0-200,y0+22)])
    #right
    polyline([(x0-128,y0+6),(x0-122,y0+5),(x0-116,y0+4),(x0-110,y0+3),
              (x0-102,y0+2),(x0-78,y0+1)])
    polyline([(x0-128,y0+10),(x0-122,y0+9),(x0-116,y0+8),(x0-110,y0+8),
              (x0-90,y0+9),(x0-78,y0+10)])
    polyline([(x0-128,y0+14),(x0-122,y0+14),(x0-116,y0+15),(x0-110,y0+16),
              (x0-102,y0+17),(x0-78,y0+22)])
    #блики
    penColor(255, 255, 255)
    penSize(4)
    line(x0-165,y0-20,x0-175,y0-32)
    line(x0-113,y0-20,x0-123,y0-32)
    

def klubok(x0,y0):
    penColor(3, 3, 3)
    brushColor(153, 153, 153)
    circle(x0+80,y0+180,50)
    polyline([(x0+50,y0+160),(x0+74,y0+166),(x0+100,y0+190),(x0+106,y0+210)])
    polyline([(x0+60,y0+150),(x0+74,y0+152),(x0+100,y0+170),(x0+114,y0+200)])
    polyline([(x0+80,y0+144),(x0+100,y0+154),(x0+114,y0+170),(x0+122,y0+196)])
    polyline([(x0+70,y0+170),(x0+58,y0+180),(x0+50,y0+190),(x0+46,y0+208)])
    polyline([(x0+80,y0+180),(x0+70,y0+190),(x0+66,y0+200),(x0+64,y0+218)])
    polyline([(x0+90,y0+190),(x0+82,y0+200),(x0+80,y0+214),(x0+80,y0+222)])
    penColor(153, 153, 153)
    polyline([(x0+34,y0+202),(x0+28,y0+208),(x0+20,y0+210),(x0+10,y0+210),
              (x0-10,y0+206),(x0-20,y0+206),(x0-38,y0+216),(x0-50,y0+216),
              (x0-70,y0+208),(x0-80,y0+208),(x0-100,y0+214)])
klubok(200,350)
cat(200,350)
window(300,15)
run()
