from django import forms
from . import models
from cal_app1.models import shift


class CalTimeForm(forms.Form):
    working_time_h = forms.CharField(label="労働(時)　")
    working_time_m = forms.CharField(label="労働(分)　")
    restriction_time_h = forms.CharField(label="制限(時)　")
    main_waking_time = forms.CharField(label="シフト(時)")


class CalSalForm(forms.Form):
    old_salary = forms.CharField(label="変更前給料")
    new_salary = forms.CharField(label="変更後給料")
    early_morning_day = forms.CharField(label="早朝日数 ")


class shiftForm(forms.Form):
    name_form = forms.ModelChoiceField(
        models.arubaito_name.objects, label="名前")

    days_form = forms.ModelChoiceField(
        models.day.objects, label="曜日")

    time_form = forms.ModelChoiceField(
        models.time.objects, label="時間")

    def save(self):
        data = self.cleaned_data
        shift1 = shift(
          name=data["name_form"],
          Days=data["days_form"],
          Times=data["time_form"])
        shift1.save()
