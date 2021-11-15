from django.db import models

class lesson(models.Model):
    word = models.CharField(max_length=128)
    comonmistake_1 = models.CharField(max_length=128)
    comonmistake_2 = models.CharField(max_length=128)
    comonmistake_3 = models.CharField(max_length=128)
    def __str__(self) -> str:
        return self.word

class quize(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question


