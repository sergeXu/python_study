# 函数定义
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# 位置实参
describe_pet('harry', 'hamster')
# 关键字实参,不关注顺序
describe_pet(pet_name='harry',animal_type='hamster')

# 参数带默认值，要放在最后
def describe_pet2(pet_name,animal_type = 'dog'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet2("lili")
describe_pet2("harry", "hamster")
# 使用默认值时，必须先在形参列表中列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参。


# 实参列表，任意数量
# *toppings中的星号让Python创建一个名为toppings的空元组,注意要放在形参列表后
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    print(toppings)
    for topping in toppings:
        print(f" -- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 模块引用函数  注意不要有执行的部分
print("\n *** 导入函数/类 ***")
# 导入函数  as 可选
from file import greet_user as gu
gu()
# 导入模块
import file as f
f.get_stored_user_name()

print("\n *** 注解逻辑 ***")
# 变量注解
name: str = "小明"
age: int = 20
height: float = 1.75
is_student: bool = True
# 函数参数 + 返回值
def add(a: int, b: int) -> int:
    return a + b
def say_hello(name: str) -> None:
    print(f"Hello, {name}")

# 列表、字典、元组
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 90}
point: tuple[int, int] = (10, 20)
# 空值（Optional）
from typing import Optional
def get_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "admin"
    return None
# 类也可以注解
class Person:
    def __init__(self, name: str):
        self.name = name
def greet(p: Person) -> str:
    return f"Hi, {p.name}"