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

Django shell
python manage.py shell
(測試)
>>>from learning_logs.models import Topic
>>>Topic.objects.all()

>>>topics = Topic.objects.all()
>>>for topic in topics:
...  print(topic.id, topic)

>>>t = Topic.objects.get(id=1)
>>>t.text
>>>t.date_added
>>>t.entry_set.all()

離開按 crrl+z

建立使用者帳號
users應用程式
python manage.py startapp users

開啟Django shell會話模式
python manage.py shell
>>>from django.contrib.auth.models import User
>>>User.objects.all()
>>>for user in User.objects.all():
...  print(user.username, user.id)

python manage.py shell
>>>from learning_logs.models import Topic
>>>for topic in Topic.objects.all():
...  print(topic, topic.owner)

重建資料庫的結構
python manage.py flush

(要在虛擬環境執行)
安裝HEROKU必要的套件
pip install dj-database-url
pip install dj-static
pip install static3
pip install gunicorn

建立requirements.txt 放入套件清單
pip freeze > requirements.txt