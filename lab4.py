import math
import matplotlib.pyplot as plt

class Point_4:
    # Змінна класу для підрахунку екземплярів
    instance_count = 0

    def __init__(self, x=0.0, y=0.0):
        # Використання сеттерів для ініціалізації координат
        self.x = x
        self.y = y
        Point_4.instance_count += 1

    # Деструктор
    def __del__(self):
        Point_4.instance_count -= 1
        print(f"Точка ({self.__x}, {self.__y}) знищена.")

    # Геттери
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # Сеттери
    @x.setter
    def x(self, value):
        self.__x = value if -100 <= value <= 100 else 0

    @y.setter
    def y(self, value):
        self.__y = value if -100 <= value <= 100 else 0

    # Метод класу для отримання кількості створених екземплярів
    @classmethod
    def get_instance_count(cls):
        return cls.instance_count

    # Метод для зсуву точки
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    # Метод для обчислення відстані між точками
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# Завдання 2: Створення точок і виконання операцій
# Створення списку точок
points = [Point_4(10, 20), Point_4(30, 40), Point_4(-50, -60), Point_4(70, 80)]

# Збереження початкових координат
x_coords_before = [p.x for p in points]
y_coords_before = [p.y for p in points]

# Відстань між першою та четвертою точками
distance = points[0].distance_to(points[3])
print(f"Відстань між першою і четвертою точками: {distance:.2f}")

# Пересуваємо другу точку на 43 одиниці вгору
points[1].move(0, 43)
print(f"Нова координата другої точки: ({points[1].x}, {points[1].y})")

# Збереження координат після змін
x_coords_after = [p.x for p in points]
y_coords_after = [p.y for p in points]

# Завдання 3: Відображення об'єктів у графічному вікні
plt.figure(figsize=(12, 6))

# Графік "до змін"
plt.subplot(1, 2, 1)
plt.scatter(x_coords_before, y_coords_before, color='blue', label='До змін')
for i, (x, y) in enumerate(zip(x_coords_before, y_coords_before), start=1):
    plt.text(x + 2, y + 2, f"{i}")
plt.title('До змін')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.legend()

# Графік "після змін"
plt.subplot(1, 2, 2)
plt.scatter(x_coords_after, y_coords_after, color='red', label='Після змін')
for i, (x, y) in enumerate(zip(x_coords_after, y_coords_after), start=1):
    plt.text(x + 2, y + 2, f"{i}")
plt.title('Після змін')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# Завдання 4: Збереження координат у файл
with open("points_output.txt", "w") as file:
    for i, point in enumerate(points, start=1):
        file.write(f"{i}) {point.x}:{point.y}\n")

print("Координати точок збережено у файл 'points_output.txt'.")
