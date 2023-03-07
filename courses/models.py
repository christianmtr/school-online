from django.db import models

from django.utils.translation import gettext_lazy as _

from studients.models import Person


class Proffesor(Person):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.names} ({self.doc_id})"



class Course(models.Model):
    class CourseLevelChoices(models.TextChoices):
        BASIC = 'B', _('Basic')
        MEDIUM = 'M', _('Medium')
        ADVANCED = 'A', _('Advanced')

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    level = models.CharField(
        max_length=1,
        choices=CourseLevelChoices.choices,
        default=CourseLevelChoices.BASIC,
    )


class CourseGroup(models.Model):
    course = models.ForeignKey(
        'Course',
        on_delete=models.PROTECT,
    )
    proffesor = models.ForeignKey(
        "Proffesor",
        on_delete=models.PROTECT,
    )
    semester = models.CharField(
        max_length=6,
        null=False,
        blank=False,
    )
    students = models.ManyToManyField(
        'students.Student',
        through='Enrollment'
    )

    def __str__(self) -> str:
        return f'{self.course} ({self.proffesor}), {self.semester}'

class Enrollment(models.Model):
    group = models.ForeignKey(
        'CourseGroup',
        on_delete=models.PROTECT,
    )
    student = models.ForeignKey(
        "studients.Student",
        on_delete=models.PROTECT,
    )
    added_at = models.DateTimeField(auto_now_add=True)
