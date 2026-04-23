from django.shortcuts import render, redirect

from .forms import TopicForm,EntryForm
from .models import Topic,Entry



# Create your views here.
def index(request):
    # 学习笔记的首页
    return render(request, 'learning_logs/index.html')
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
def topic(request, topic_id):
    # 形参视图参数
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    # 添加新主题
    if request.method != 'POST':
            form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            # “redirect 函数，用户提交主题后将使用这个函数重定向到网页 topics”
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id)
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(data=request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'form': form, 'topic': topic, 'entry': entry}
    return render(request, 'learning_logs/edit_entry.html', context)