from django.conf.urls import url
from payments import views

urlpatterns = [
    url(r'^testpayment/$', views.test_payment)
]