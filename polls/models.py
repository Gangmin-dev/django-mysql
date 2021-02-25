import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# 몇몇 Field는 필수 parameter 존재
# ex) Char => max_length 등
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # Field class 생성자의 첫번째 parameter로 사람이 읽기 좋은 이름 지정
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        # https://docs.djangoproject.com/ko/3.1/topics/i18n/timezones/ 참조하면 좋음
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # Question을 참조하겠다
    # CASCADE => Question이 삭제되면 나도 삭제
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    # default와 같은 선택적 parameter도 존재
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text