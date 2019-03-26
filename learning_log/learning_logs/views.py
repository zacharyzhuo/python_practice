from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm
# 從views.py所在的資料夾中的model.py中匯入Topic類別

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    # 查詢資料庫 請求提供Topic物件並按照date_added屬性進行排序
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries }
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add a new topic."""
    # 檢測請求方法是GET還是POST
    if request.method != 'POST':
        # No data submitted; create a blank form. 返回一個空表單
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        # 驗證使用者該填的表單都填了沒(預設值是都要填)以及型態是否正確
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
            # 使用者提交表單之後重新導向topics網頁

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.object.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)