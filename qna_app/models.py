from django.db import models

# Create your models here.
class QuestionModel(models.Model):
    title=models.CharField(max_length=255)
    posted_by=models.CharField(max_length=120)
    timestamp= models.DateTimeField(auto_now_add=True)
    question_descp = models.TextField()
    question_img = models.ImageField(upload_to='QuestionImg',blank=True,null=True)
    question_votes = models.IntegerField(default=0)

    objects=models.Manager()

    def __str__(self):
        return(self.question_descp)


class AnswerModel(models.Model):
    answered_by =models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    answer_descp = models.TextField()
    answer_img = models.ImageField(upload_to='AnswerImg',blank=True,null=True)
    is_accept =models.BooleanField(default=0)
    ans_votes = models.IntegerField(default=0)
    question= models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
