from django.urls import path

from . import views

urlpatterns = [
    path('', views.FoodListView.as_view()),
    # path('cze', views.index_cze, name='index_cze'),
    # path('eng', views.index_eng, name='index_eng'),
    # path('search', views.search, name='search'),
]
