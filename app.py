import math
class SphereBase:
    team_info = "Команда разработчиков: Ширинкин Тимофей - разработчик 1, Сальников Виталий - разработчик 2, Бикентаева Сауле - разработчик 3"
    
    @staticmethod
    def about():
        return SphereBase.team_info
    
    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        """Метод для установки радиуса"""
        self.__radius = radius

    def get_radius(self):
        """Метод для получения радиуса"""
        return self.__radius

class Sphere(SphereBase):
    def __init__(self, radius):
        super().__init__(radius)

    def calculate_volume(self):
        """Метод для расчета объема шара"""
        radius = self.get_radius()
        return (4 / 3) * math.pi * (radius ** 3)

try:
    a = float(input("Введите радиус шара: "))
    if a > 0:
        sphere = Sphere(a)
        print("Радиус шара:", sphere.get_radius())
        print("Объем шара:", sphere.calculate_volume())
        print(SphereBase.about())
    else:
        print("Радиус должен быть положительным числом.")
except ValueError:
    print("Попробуйте еще раз и введите корректное числовое значение.")











