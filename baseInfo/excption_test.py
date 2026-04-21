# 基础使用
from langsmith import expect

try:
    print(5/0)
except ZeroDivisionError:
    print("can not divide by zero")


# 使用异常避免崩溃
# “只有 try 代码块成功执行才需要继续执行的代码，都应放到 else 代码块中”
from pathlib import Path

def count_words(path):
    """计算一个文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
path = Path('file/programming.txt')
count_words(path)

# 静默失败 pass
try:
    num = 5/0
except Exception as e:
    # 输出异常类型
    print(e)
    pass
else:
    print(f"right go:{num}")