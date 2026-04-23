# 安装更新 pip
#     python -m pip install --upgrade pip
# 安装第三方包 pytest
# python3 -m pip install --user pytest

def get_formatted_name(first_name, last_name ,middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else :
        full_name = f"{first_name} {last_name}"
    return full_name.title()