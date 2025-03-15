class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

make = input("Введіть марку автомобіля: ")
model = input("Введіть модель автомобіля: ")
year = input("Введіть рік випуску автомобіля: ")

car = Car(make, model, year)
print(car.get_info())
