from django.db.models import (
    Model,
    CharField,
    IntegerField,
    TextField,
    ImageField,
    ForeignKey,
    CASCADE
)
from .consts import MAX_RATE

CATEGORY = (('business','ビジネス'),('life','生活'),('other','その他'))
RATE_CHOICES = [(x,str(x)) for x in range(0,MAX_RATE + 1)]
class SampleModel(Model):
    title :CharField = CharField(max_length=100)
    number :IntegerField = IntegerField()

class Book(Model):
    title = CharField(max_length=100)
    text = TextField()
    thumbnail = ImageField(null=True, blank=True)
    category = CharField(max_length=100,choices=CATEGORY)
    user = ForeignKey('auth.User',on_delete=CASCADE)

    def __str__(self): #DBobjectの文字列化
        return self.title
    
    @property #数値計算で求めた値を取得するメソッドのアノテーション
    def getNewPk(self)->int:
        ADJUST_NUM = 5
        return int(self.pk * ADJUST_NUM)

class Review(Model):
    book = ForeignKey(Book, on_delete=CASCADE)
    title = CharField(max_length=100)
    text = TextField()
    rate = IntegerField(choices=RATE_CHOICES)
    user = ForeignKey('auth.User', on_delete=CASCADE)
    
    def __str__(self): #DBobjectの文字列化
        return self.title
    
        
    
