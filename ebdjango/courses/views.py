from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CourseInfo, SectionInfo, Review
from.forms import AddCourseToSchedule, CreateReview

# Create your views here.
@login_required(login_url='/')
def departments(request):
    return render(request, 'courses/departments.html')

#querying and returning template with all courses for a department
@login_required(login_url='/')
def department_courses(request, dept_abbreviation):
    all_courses = CourseInfo.objects.all().filter(department_abbreviation=dept_abbreviation)

    context = {'courses':all_courses}
    #if user added the course
    if request.method == 'POST':
        if 'add_course' in request.POST:
            file = open('add_course.txt','w') 
            file.write('posting') 
            file.close()
            # if its a post request the data must be processed and validated
            form = AddCourseToSchedule(request.POST)
            if form.is_valid():
                user = request.user

                course = request.POST.getlist('courses[]')

                course_to_add = SectionInfo.objects.get(id=course[0])
                course_to_add.students.add(user)
                # pass in notification, wont be used except for one iteration to display a notification to a user
                # that they added a course succesfully
                # to display that the request went through:
        if 'add_review' in request.POST:
            form = CreateReview(request.POST)
            if form.is_valid:
                user = request.user
                course_text = request.POST.getlist('courses[]')
                course_to_review = CourseInfo.objects.get(id=course_text[0])            
                review_text = request.POST.getlist('review_text[]')[0]
                difficulty = request.POST.getlist('difficulty[]')[0]
                interesting = request.POST.getlist('interesting[]')[0]
                homework_time = request.POST.getlist('homework[]')[0]
                review_object = Review(user = user, review_text = review_text, difficulty = difficulty, 
                    interesting = interesting, hours_per_week_of_homework = homework_time,user_id=user.id,course=course_to_review)
                review_object.save()


    return render(request, 'courses/generic_department.html', context)
# returns the info about a specific course
# def return_course_info(request, dept_abbreviation, pk):
#     course_list = Course.objects.filter(nameID = str(pk)).order_by("course_number")
#     #we want individual instance of the course to print the information
#     oneCourse = Course.objects.filter(nameID = str(pk))[:1]
#     #if user added the course
#     if request.method == 'POST':
#         # if its a post request the data must be processed and validated
#         form = AddCourseToSchedule(request.POST)
#         if form.is_valid():
#             user = request.user

#             course = request.POST.getlist('courses[]')

#             course_to_add = Course.objects.get(id=course[0])
#             course_to_add.students.add(user)
#             # pass in notification, wont be used except for one iteration to display a notification to a user
#             # that they added a course succesfully
#             # to display that the request went through:
#             context = {'course_list': course_list, 'course_name': oneCourse, 'form': form,}
#             return (render(request, 'courses/generic_course.html', context))


#     else:
#         form = AddCourseToSchedule()
#     context = {'course_list': course_list, 'course_name': oneCourse, 'form': form,}
#     return (render(request, 'courses/generic_course.html', context))