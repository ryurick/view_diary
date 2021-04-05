from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day

class IndexView(LoginRequiredMixin,generic.ListView):
    model = Day
    paginate_by = 3

#CreateView,UpdateViewでデフォルトで探すtemplatesは『モデル名_form.html』。今回でいうと『day_form.html』
class AddView(LoginRequiredMixin,generic.CreateView):
    model = Day
    #↓は『fields = '__all__'』でも可。単純なformを作る場合はこれを定義すればforms.pyは不要。
    form_class = DayCreateForm
    #success_url:データの作成に成功したら、リダイレクトさせるページ（reverse_lazyは文字列としてurlが欲しい場合に使用）
    success_url = reverse_lazy('diary:index')

class UpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

class DeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')

class DetailView(LoginRequiredMixin,generic.DetailView):
    model = Day
    

