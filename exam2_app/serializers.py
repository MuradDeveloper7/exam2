from rest_framework import serializers
from .models import Course, Student, Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ("value", "data", "course", "student")


class CourseSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ("title", "discribtion", "duratioiin")


class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    grades = GradeSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ("first_name", "last_name", "email", "courses")





