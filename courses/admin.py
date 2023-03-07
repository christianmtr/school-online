from django.contrib import admin

from courses.models import Course, CourseGroup, Enrollment, Proffesor

admin.site.register(Proffesor)
admin.site.register(Course)
admin.site.register(CourseGroup)
admin.site.register(Enrollment)
