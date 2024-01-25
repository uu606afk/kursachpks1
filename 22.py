#Гистограмма:

```python
import matplotlib.pyplot as plt

 #Данные
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

 #Создание гистограммы
plt.hist(data, bins=5, edgecolor='black')

 #Добавление подписей
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма')

 #Отображение гистограммы
plt.show()
