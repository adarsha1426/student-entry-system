from django.db import models

# Create your models here.
class Student(models.Model):
    MAJOR_CHOICES=[
        ('Science','Science'),
        ('Humanities','Humanities'),
        ('Arts','Arts'),
        ('Management','Management'),
    ]
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField() #Since age can't be naegative so using PostiveIntegerField
    address=models.TextField()
    grade=models.CharField(max_length=50)
    major=models.CharField(max_length=50,choices=MAJOR_CHOICES)

    class Meta:
        ordering=['age']
    
    def _str__(self):
        return f'{self.name} - {self.major} - {self.grade}'