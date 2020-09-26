from django.db import models
from django.contrib.auth.models import User, Group
# # Create your models here.

# # This model will not be used to create database table instead it is used as a base class for other models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# To put common info into number of other models
    class Meta:
        abstract = True


# # # This model is created to extract system info and display the info dynamically in the website
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


class Course(TimeStamp):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Subject(TimeStamp):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


GENDER = (
    ("male", "MALE"),
    ("female", "FEMALE"),
    ("other", "OTHER"),
)


class Teacher(TimeStamp):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER)
    photo = models.ImageField(upload_to="teacher")
    phone_no = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.CharField(max_length=40)
    education = models.CharField(max_length=100)
    experience = models.CharField(max_length=40)
    cv = models.FileField(upload_to="cv")
    citizenship = models.FileField(upload_to="citizenship")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        grp, created = Group.objects.get_or_create(name="teacher")
        self.user.groups.add(grp)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Student(TimeStamp):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=40)
    phone_no = models.CharField(max_length=40)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    report_card = models.FileField(upload_to="report_card")

    def save(self, *args, **kwargs):
        grp, created = Group.objects.get_or_create(name="student")
        self.user.groups.add(grp)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
