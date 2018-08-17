#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import SectionInfo, Review


class AddCourseToSchedule(ModelForm):
    class Meta:
        model = SectionInfo
        fields = ('students',)
class CreateReview(ModelForm):
	class Meta:
		model = Review
		fields = ('review_text','difficulty','interesting','hours_per_week_of_homework','user')
