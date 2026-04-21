# 引入基础类定义
from dto.car import Car
from dto.car import ElectricCar
# 类实例化
myCar = Car("Honda", "Accord", 2023)
print(myCar.get_description())
myCar.read_odometer()

myCar.odometer_reading = 10000
myCar.read_odometer()
myCar.update_odometer(12000)
myCar.read_odometer()
myCar.increment_odometer(500)
myCar.read_odometer()

print("\n *** 继承 ***")
my_tesla  = ElectricCar("tesla", "model", 2022)
print(my_tesla.get_description())
my_tesla.print_battery_size()


