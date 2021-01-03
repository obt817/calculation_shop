from django .views.generic import TemplateView
from django.views.generic.edit import FormView
from . import forms
import math


class indexView(TemplateView):
    template_name = "cal_app1/index.html"


class salary_topView(TemplateView):
    template_name = "cal_app1/salary_top.html"


class salary_calView(FormView):
    form_class = forms.CalTimeForm
    template_name = "cal_app1/salary_cal.html"

    def form_valid(self, form):
        # form.cleaned_dataにフォームの入力内容が入っています
        data = form.cleaned_data
        wth = int(data["working_time_h"])
        wtm = int(data["working_time_m"])
        rth = int(data["restriction_time_h"])
        mwt = int(data["main_waking_time"])

        new_wt = wth + round(wtm / 60, 2)
        new_rt = rth
        new_time = math.ceil(new_wt - new_rt)
        new_lower_day = new_time // mwt
        new_lower_remainder = new_time % mwt

        lower_day = (
         str(mwt) + "時間労働を減らす日数は" +
         str(new_lower_day) + "日です"
        )
        lower_time = (
         "休憩時間をなどを使って減らす時間は"
         + str(new_lower_remainder) + "時間です"
        )

        new_time_1 = (
         "減らす必要がある時間は" +
         str(new_time) + "時間です"
        )

        ctxt = self.get_context_data(
         new_time_1=new_time_1,
         lower_day=lower_day,
         lower_time=lower_time,
         form=form
        )
        return self.render_to_response(ctxt)


class salary2_calView(FormView):
    form_class = forms.CalSalForm
    template_name = "cal_app1/salary_cal2.html"

    def form_valid(self, form):
        # form.cleaned_dataにフォームの入力内容が入っています
        data = form.cleaned_data
        osy = int(data["old_salary"])
        nsy = int(data["new_salary"])
        emd = int(data["early_morning_day"])
        nemd = emd * 3 * 977
        new_salary = "追加する金額は" + str(osy + nemd - nsy) + "円です"

        ctxt = self.get_context_data(
         new_salary=new_salary,
         form=form
        )
        return self.render_to_response(ctxt)
