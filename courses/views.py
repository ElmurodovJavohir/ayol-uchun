from rest_framework import generics
from .models import Course, Video, Certificate, CourseRating
from .serializer import CourseSerializer, VideoSerializer, CertificateSerializer, CourseRatingSerializer
from rest_framework import permissions

class IsVideoOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsCourseRatingOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_fields = ["price","average_rating"]
    search_fields = ["title","description",]
    ordering_fields = ["average_rating"]

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # permission_classes = [permissions.IsAuthenticated, IsVideoOwner]

    # def perform_update(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def perform_destroy(self, instance):
    #     instance.delete()

class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    # permission_classes = [permissions.IsAuthenticated, IsCourseOwner]

    # def perform_update(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def perform_destroy(self, instance):
    #     instance.delete()

class CertificateList(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CertificateDetail(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CourseRatingList(generics.ListAPIView):
    queryset = CourseRating.objects.all()
    serializer_class = CourseRatingSerializer

class CourseRatingDetail(generics.RetrieveUpdateAPIView):
    queryset = CourseRating.objects.all()
    serializer_class = CourseRatingSerializer

    # permission_classes = [permissions.IsAuthenticated, IsCourseRatingOwner]

    # def perform_update(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def perform_destroy(self, instance):
    #     instance.delete()