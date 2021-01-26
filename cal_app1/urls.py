from django.urls import path
from .views import salary_topView
from .views import salary_calView, salary2_calView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(salary_topView.as_view()),
         name="cal_top"),
    path('salary_cal/', login_required(salary_calView.as_view()),
         name="sal_cal"),
    path('salary_cal/2/', login_required(salary2_calView.as_view()),
         name="sal_cal_2"),


    ]
