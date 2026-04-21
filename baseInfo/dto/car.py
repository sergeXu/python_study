class Car:
    # 初始化函数
    def __init__(self, make, model, year):
        self.make:str = make
        self.model:str  = model
        self.year :str = year
        self.odometer_reading:int = 0 #里程数，带默认值
    def get_description(self) -> str:
        return f"{self.make} {self.model} {self.year}".title()
    def read_odometer(self) -> None:
        print(f"This car has {self.odometer_reading} miles on it.")
    # 修改属性值
    def update_odometer(self, mileage:int) -> None:
    # 将里程表读数设置为指定的值。禁止将里程表读数往回调。
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    def print_battery_size(self):
        print(f"This car has {self.battery_size} kWh battery.")