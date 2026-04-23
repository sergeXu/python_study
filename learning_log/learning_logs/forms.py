from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

# “最简单的 ModelForm 版本只包含一个内嵌的 Meta 类，告诉 Django 根据哪个模型创建表单以及在表单中包含哪些字段。
# 这里指定根据模型 Topic 创建表单（见❷），并且其中只包含字段 text（见❸）。字典 labels 中的空字符串告诉 Django 不要为字段 text 生成标签（见❹）”

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}