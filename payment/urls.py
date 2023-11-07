from django.urls import path
from django.urls import include
from .views import GeneratePayLinkAPIView, PaymeCallBackAPIView, OrderListView, OrderDetailView

urlpatterns = [
    path("merchant/", PaymeCallBackAPIView.as_view()),
    path('pay-link/', GeneratePayLinkAPIView.as_view(), name='generate-pay-link'),
    path("",OrderListView.as_view(),name='order-list'),
    path("<int:pk>/",OrderDetailView.as_view(),name='order-detail'),
]