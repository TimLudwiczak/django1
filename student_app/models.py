from django.db import models

# Create your models here.
class Student(models.Model): #create model class
    #create a character field up to a max length of 100 characters
    name = models.CharField(max_length=100)

    #create MANDATORY student_email only if 1 doesn't already exists
    student_email = models.EmailField(unique=True)

    #create personal_email if EmailField is not blank, unless NULL
    personal_email = models.EmailField(blank=True, null=True)

    #create locker number id
    locker_number = models.IntegerField()

    #create locker combo
    locker_combo = models.CharFiel(length=20)

    #create if student_good boolean
    good_student = models.BooleanField(default=True)