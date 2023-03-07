from django.db import models


class Person(models.Model):
    names = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    doc_id = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        unique=True,
    )

class Parent(Person):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.names} ({self.doc_id})"


class Student(Person):
    parent = models.ForeignKey(
        'Parent',
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.names
