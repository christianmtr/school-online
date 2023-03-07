from rest_framework import viewsets
from courses.api.serializers import CourseSerializers

from courses.models import Course


class CourseViewSets(viewsets.ModelViewSet):
    """
    Endpoints to create (post), update (put/patch),
    delete or get courses information.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
