from rest_framework import generics
from exam2_app.models import  Student
from exam2_app.serializers import  StudentSerializer


class StudentlistAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.oobjects.all()
    serializer_class = StudentSerializer
