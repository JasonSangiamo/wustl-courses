from django import forms
from django.forms import ModelForm
from courses.models import SectionInfo


class RemoveCourseFromSchedule(ModelForm):
    class Meta:
        model = SectionInfo
        fields = ('students',)

        
class AddCourseToSchedule(ModelForm):
    class Meta:
        model = SectionInfo
        fields = ('students',)