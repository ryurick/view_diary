from django.urls import path
from .import views

app_name = 'diary'

urlpatterns = [
     #汎用Viewを使用するときは『.as_view()』を記載
    path('',views.IndexView.as_view(), name='index'), #diary/
    # path('add/',views.AddView.as_view(), name='add'), #diary/add
    # #ある特定のデータを取り出す<int:pk>　pk:primarykey modelsでmodelを作成した際、djangoが自動的に振るid。1,2,3…のように増加する
    # path('update/<int:pk>/',views.UpdateView.as_view(), name='update'), #diary/update/1
    # path('delete/<int:pk>/',views.DeleteView.as_view(), name='delete'), #diary/delete/1
    path('detail/<int:pk>/',views.DetailView.as_view(), name='detail'), #diary/detail/1
]