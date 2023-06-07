from django.urls import path, include
from . import views

app_name = 'exam2_app'

urlpatterns = [
    path('courses/', views.CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetailAPIView.as_view(), name='course-detail'),

    path('students/', views.StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', views.StudentDetailAPIView.as_view(), name='student-detail'),

    path('grades/', views.GradeListAPIView.as_view(), name='grade-list'),
    path('grades/<int:pk>/', views.GradeDetailAPIView.as_view(), name='grade-detail'),
]
