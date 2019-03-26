from django import forms

from .models import Topic, Entry
class TopicForm(forms.ModelForm):
# 最簡單的版本是由一個巢狀嵌套的meta類別組成，告訴djago哪個模型是以表單為基礎，哪些欄位要涵在表單中
    class Meta:  
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ""}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        # widget小工具是個HTML表單元素 例如單行式的文字方塊、多行式的文字方塊或下拉式清單等