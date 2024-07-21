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

    #create locker combo ### Link locker combination to locker number
    locker_combo = models.CharFiel(length=20)

    ###Found this as possible option to ensure XX-XX-XX format for combination
    #    locker_combination_validator = RegexValidator(
    #     regex=r'^\d{2}-\d{2}-\d{2}$',
    #     message='Locker combination must be in the format xx-xx-xx, where x is an integer.'
    # )

    #create if student_good boolean ### Need to define what is good studen
    good_student = models.BooleanField(default=True)