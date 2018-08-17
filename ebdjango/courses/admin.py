from django.contrib import admin
from .models import SectionInfo, CourseInfo	


# allowing courses to be added in admin view
admin.site.register(SectionInfo)
admin.site.register(CourseInfo)