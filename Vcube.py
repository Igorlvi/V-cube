# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np

print("Розрахуйте V обєм куба, та S площу його поверхні ")
print("Введіть розмір сторони ?")
a = float(input("a = "))
print("V Обєм = a*a*a або, а в кубі.")
print("V Обєм = %.2f" % (a * a * a))
print("S площа поверхні = (a*a) * 6.")
print("S площа поверхні = %.2f" % ((a * a) * 6))
print ("Поки Ви звіряєте свій розв'язок із розв'язком даної програми, MATPLOTLIB накреслив Вам ваш куб. Знайдіть його у себе на моніторі.")

data = np.ones(np.array([1,1,1]))
fig = plt.figure(figsize=(a, a)) 
ax = fig.add_subplot(111 , projection = '3d') 
ax.voxels(data, facecolors=[1,1,1,.5],edgecolor='k')
 
    
plt.show()
