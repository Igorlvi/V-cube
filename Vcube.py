# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np
import turtle
import sys
from vispy import scene
from vispy.color import Color

print("Розрахуйте V обєм куба, та S площу його поверхні ")
print("Введіть розмір сторони ?")
a = float(input("a = "))
print("V Обєм = %.2f" % (a * a * a))
print("S площа поверхні = %.2f" % ((a * a) * 6))
print ("Поки Ви звіряєте свій розв'язок, дана програма побудує Вам Ваш куб ")
print("У графічному сервісі\n1-Turtle\n2-Matplotlib\n3-VisPy")
figure = input("Оберіть графічний сервіс : ")
if figure == '1':
    # будуємо екран
    tut = turtle.Screen() 
    # колір фону
    tut.bgcolor("grey") 
    # черепашка
    tut.title("Turtle") 
    my_pen = turtle.Turtle() 
    # колір креслення 
    my_pen.color("black") 
    tut=turtle.Screen()            
    # передній квадрат
    my_pen.forward(a*37) 
    my_pen.left(90) 
    my_pen.forward(a*37) 
    my_pen.left(90)
    my_pen.forward(a*37) 
    my_pen.left(90) 
    my_pen.forward(a*37) 
    my_pen.left(90)
    # в глибину
    my_pen.left(45)
    my_pen.forward((a-2)*37)
    my_pen.right(45)
    # дальній квадрат
    my_pen.forward(a*37) 
    my_pen.left(90) 
    my_pen.forward(a*37) 
    my_pen.left(90)
    my_pen.forward(a*37) 
    my_pen.left(90) 
    my_pen.forward(a*37) 
    my_pen.left(90)
    # решта
    my_pen.forward(a*37)
    my_pen.right(135)
    my_pen.forward((a-2)*37)
    my_pen.right(135)
    my_pen.forward(a*37)
    my_pen.right(45)
    my_pen.forward((a-2)*37)
    my_pen.left(135)
    my_pen.forward(a*37)
    my_pen.left(45)
    my_pen.forward((a-2)*37)
    my_pen.hideturtle()
    style = ('Courier', 15, 'italic')
    my_pen.write(" Turtle накреслила\n Вам ваш куб", font=style, align='right')
    turtle.title('Ваш куб')

elif figure == '2':
    # matplotlib
    data = np.ones(np.array([1,1,1]))
    fig = plt.figure(figsize=(a, a)) 
    ax = fig.add_subplot(111 , projection = '3d') 
    ax.voxels(data, facecolors=[1,1,1,.5],edgecolor='k')
    plt.title('Ваш куб накреслений на координатній сітці')
    plt.show()
    

elif figure == '3':
    #VisPy
    canvas = scene.SceneCanvas(keys='interactive', size=(a*40+200, a*40+200), show=True)
    view = canvas.central_widget.add_view()
    view.bgcolor = '#efefef'
    view.camera = 'turntable'
    view.padding = 1
    color = Color("grey")
    cube = scene.visuals.Box(a/4, a/4, a/4, color=color, edge_color="black",parent=view.scene)
    if __name__ == '__main__' and sys.flags.interactive == 0:
        canvas.app.run()


else:
    print("Помилка введення ???")
    
