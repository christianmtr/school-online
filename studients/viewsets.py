from rest_framework import viewsets
from studients.api.serializers import ParentSerializer, StudentSerializers

from studients.models import Parent, Student


class ParentViewsets(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class StudientViewsets(viewsets.ModelViewSet):
    """
    Endpoints to create, update, delete or get
    students information.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
