import matplotlib.pyplot as plt

 #Данные
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

 #Создание линейного графика
plt.plot(x, y)

 #Добавление подписей
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Линейный график')

 #Отображение графика
plt.show()
