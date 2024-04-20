# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np
import turtle

print("Розрахуйте V обєм куба, та S площу його поверхні ")
print("Введіть розмір сторони ?")
a = float(input("a = "))
print("V Обєм = a*a*a або, а в кубі.")
print("V Обєм = %.2f" % (a * a * a))
print("S площа поверхні = (a*a) * 6.")
print("S площа поверхні = %.2f" % ((a * a) * 6))
print ("Поки Ви звіряєте свій розв'язок із розв'язком даної програми, черепашка та matplotlib накреслили Вам ваш куб . Знайдіть їх у себе на моніторі.")

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
  
# передній прямокутник
for i in range(2): 
    my_pen.forward(a*37) 
    my_pen.left(90) 
    my_pen.forward(a*37) 
    my_pen.left(90) 
  
# в глибину
my_pen.left(45)
my_pen.forward((a-2)*37)
my_pen.right(45)
  
 # дальній прямокутник
for i in range(2): 
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

# matplotlib
data = np.ones(np.array([1,1,1]))
fig = plt.figure(figsize=(a, a)) 
ax = fig.add_subplot(111 , projection = '3d') 
ax.voxels(data, facecolors=[1,1,1,.5],edgecolor='k')
 
plt.show()

