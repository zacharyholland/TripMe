from django.db import models

# Create your models here.
class Grade_Level(models.Model):
    class_level = models.CharField(max_length=2, unique=True)
    description = models.CharField(max_length=20)
    
    class Meta:
        db_table = "grade_level"
    
    def __str__(self):
        return (self.description)

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    class_level = models.ForeignKey(Grade_Level, on_delete=models.DO_NOTHING,to_field='class_level')

    class Meta:
        db_table = 'student'
    
    def __str__(self):
        return (self.first_name + " " + self.last_name)