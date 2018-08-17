from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

#creating a specific entry in this table for each section offering for each course
class SectionInfo(models.Model):   
    instructor = models.CharField(max_length = 200)
    location = models.CharField(max_length = 50)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    days = models.CharField(max_length = 20)
    final = models.CharField(max_length = 25)
    semester = models.CharField(max_length=10)
    section = models.CharField(max_length = 10)
    #creating M2M relationship with students, allow there to be no students in a section
    students = models.ManyToManyField(User, blank = True)
#creating a specific entry in this table for each course offered
class CourseInfo(models.Model):
    name = models.CharField(max_length = 200)
    department = models.CharField(max_length=50)
    department_abbreviation = models.CharField(max_length = 10)
    course_number = models.CharField(max_length = 20)
    description = models.TextField()
    units = models.CharField(max_length = 50)
    lab = models.CharField(max_length = 25)
    nameID = models.IntegerField()
    #creating M2M relationship with sections
    sections = models.ManyToManyField(SectionInfo, blank= True, related_name = "course")  
    @property
    def average_difficulty(self):
        return self.reviews.aggregate(Avg('difficulty'))
    @property    
    def average_interesting(self):
        return self.reviews.aggregate(Avg('interesting'))
    @property    
    def average_homework(self):
        return self.reviews.aggregate(Avg('hours_per_week_of_homework'))
   

class Review(models.Model):
    review_text = models.TextField()
    difficulty = models.PositiveSmallIntegerField()
    interesting = models.PositiveSmallIntegerField()
    hours_per_week_of_homework = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #creating O2M relationship with courses
    course = models.ForeignKey(CourseInfo,on_delete=models.CASCADE,null=True,related_name="reviews")
    created_at = models.DateField(auto_now_add=True)
