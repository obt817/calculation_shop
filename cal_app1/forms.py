from django import forms


class CalTimeForm(forms.Form):
    working_time_h = forms.CharField(label="労働(時)　")
    working_time_m = forms.CharField(label="労働(分)　")
    restriction_time_h = forms.CharField(label="制限(時)　")
    main_waking_time = forms.CharField(label="シフト(時)")


class CalSalForm(forms.Form):
    old_salary = forms.CharField(label="変更前給料")
    new_salary = forms.CharField(label="変更後給料")
    early_morning_day = forms.CharField(label="早朝日数 ")
