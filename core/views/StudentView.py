from rest_framework.viewsets import ModelViewSet
from ..models.Student import Student
from ..serializers.StudentSerializer import StudentSerializer


class SessionView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
