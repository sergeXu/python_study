# Path路径
from pathlib import Path
path = Path('file/pi_digits.txt')
# 文本读取
contents = path.read_text()
contents = contents.rstrip()
print(contents)

print("\n splitlines() BY 每行输出")
lines = contents.splitlines()
for line in lines:
    print(line)

# 写入文件
path = Path('file/programming.txt')
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path.write_text(contents)


# 存储数据json
import json
from typing import Optional
datas = [
    {
        "name": "serge",
        "age": 21,
        "gender": "male",
    },
    {
        "name": "mary",
        "age": 22,
        "gender": "female",
    },
]
filename = "file/data.json"
with open(filename, "w") as f:
    json.dump(datas, f)
print("json写入",datas)
with open(filename, "r") as f:
    readData = json.load(f)
print(readData,type(readData))


# 原始输入版本
def greet_user_0():
    filename = 'file/user_name.json'
    try:
        with open(filename) as f:
            user_name = json.load(f)
    except FileNotFoundError:
        user_name = input("Please enter your name: ")
        with open(filename,'w') as f:
            json.dump(user_name,f)
            print(f"we will remember your name: {user_name}")
    else:
        print(f"welcome back, {user_name}")

# greet_user_0()

# json.dumps() 和 json.loads()
# 重构版本
def get_stored_user_name(file_path:Path)->Optional[str]:
    try:
        if file_path.exists():
            content= file_path.read_text()
            user_name = json.loads(content)
            return user_name
        else:
            return None
    except Exception as e:
        print("异常发生",e)

def get_new_user_name(file_path:Path)->str:
    user_name = input("Please enter your name: ")
    # dumps()
    content = json.dumps(user_name)
    file_path.write_text(content)
    return user_name

def is_current_user(user_name)-> Optional[bool]:
    check_bool = None
    # 信号量，保证输入正确
    while check_bool == None:
        check_input = input(f"Is the current user y/n? {user_name} ")
        if check_input == 'y':
            check_bool = True
        elif check_input == 'n':
            check_bool = False
        else:
            print("please enter y or n")
    return check_bool

def greet_user():
    path = Path('file/user_name.json')
    user_name = get_stored_user_name(path)
    if user_name:
        if is_current_user(user_name):
            print(f"welcome back, {user_name}")
        else:
            user_name = get_new_user_name(path)
            print(f"reset to new user: {user_name}")
    else:
        user_name = get_new_user_name(path)
        print(f"we will remember your name: {user_name}")

print("\n greet_user start")
greet_user()