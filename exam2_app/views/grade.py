from rest_framework import generics
from exam2_app.models import Grade
from exam2_app.serializers import GradeSerializer


class GradelistAPIView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class GradeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.oobjects.all()
    serializer_class = GradeSerializer
