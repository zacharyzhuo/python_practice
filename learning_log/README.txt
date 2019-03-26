建立虛擬環境
python -m venv ll_env

啟用虛擬環境
ll_env\Scripts\activate

(停止虛擬環境)
deactivate

安裝Django
pip install Django

在Django中設定專案
django-admin.py startproject learning_log .

建立資料庫
python manage.py migrate

查看專案
python manage.py runserver

建立應用程式(先切換到manage.py所在的目錄)
python manage.py startapp learning_logs

啟用模型
(修改資料庫)
python manage.py makemigrations learning_logs

(套用這個遷移處理)
python manage.py migrate

建立Superuser
python manage.py createsuperuser

遷移Entry模型
python manage.py makemigrations learning_logs
python manage.py migrate

Django shell
python manage.py shell
(測試)
>>>from learning_logs.models import Topic
>>>Topic.objects.all()

>>>topics = Topic.objects.all()
>>>for topic in topics:
...	print(topic.id, topic)

>>>t = Topic.objects.get(id=1)
>>>t.text
>>>t.date_added
>>>t.entry_set.all()

離開按 crrl+z

# r''為原始字串，^$分別查看字串頭尾
    # 第二引數指定要呼叫的視窗函式
    # 第三引數把這個URL模式的名稱指定為index