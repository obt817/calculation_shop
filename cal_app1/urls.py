from django.urls import path
from .views import salary_topView
from .views import salary_calView, salary2_calView
urlpatterns = [
    path('', salary_topView.as_view()),
    path('salary_cal/', salary_calView.as_view(), name="sal_cal"),
    path('salary_cal/2/', salary2_calView.as_view(), name="sal_cal_2"),


    ]
