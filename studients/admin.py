from django.contrib import admin

from studients.models import Parent, Person, Student

admin.site.register(Person)
admin.site.register(Parent)
admin.site.register(Student)
