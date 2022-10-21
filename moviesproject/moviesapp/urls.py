from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('movies/<int:movies_id>/',views.details,name='details'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]