from django.urls import path
from .views import indexView, salary_topView
from .views import salary_calView, salary2_calView
urlpatterns = [
    path('', indexView.as_view()),
    path('salary_top/', salary_topView.as_view()),
    path('salary_top/salary_cal/', salary_calView.as_view()),
    path('salary_top/salary_cal/salary_cal2/', salary2_calView.as_view()),


    ]
