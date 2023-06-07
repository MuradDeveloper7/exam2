from rest_framework import generics
from exam2_app.models import Course
from exam2_app.serializers import CourseSerializer


class CourseListAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



