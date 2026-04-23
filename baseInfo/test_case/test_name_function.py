from name_function import get_formatted_name

# “测试文件的名称很重要，必须以 test_打头”
def test_name_function():
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_name_function2():
    formatted_name = get_formatted_name(first_name='lion', middle_name="scot",last_name='kennedi')
    assert formatted_name == 'Lion Scot Kennedi'

# “终端窗口中执行命令 python3 -m pytest 执行全部测试脚本”


