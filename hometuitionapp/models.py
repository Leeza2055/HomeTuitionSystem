from django.db import models

# # Create your models here.

# # This model will not be used to create database table instead it is used as a base class for other models
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# To put common info into number of other models
    class Meta:
        abstract = True


# # This model is created to extract system info and display the info dynamically in the website
class HomeTuitionSystem(TimeStamp):
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to="logo")
    about = models.TextField()
    about_image1 = models.ImageField(upload_to="system")
    about_image2 = models.ImageField(upload_to="system")
    email = models.EmailField()
    phone_no = models.CharField(max_length=40)
    facebook = models.CharField(max_length=100)
# The __str__() method of the model will be called to generate string representations of the objects for use in the field’s choices.
# The self  keyword is used to accesss the attributed and methods of the class

    def __str__(self):
        return self.name


GENDER = (
    ("male", "MALE"),
    ("female", "FEMALE"),
    ("other", "OTHER"),
)


class Teacher(TimeStamp):
    teacher_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10,choices=GENDER)
