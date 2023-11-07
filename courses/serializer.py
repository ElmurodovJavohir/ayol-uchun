from rest_framework import serializers
from .models import Course, Video, Certificate, CourseRating
from user.serailizer import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    watched_by = UserSerializer(many=True)
    class Meta:
        model = Video
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer()
    class Meta:
        model = Certificate
        fields = '__all__'

class CourseRatingSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    user = UserSerializer()
    class Meta:
        model = CourseRating
        fields = '__all__'