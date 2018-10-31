from django.urls import path

from . import views

urlpatterns = [
    path('<word>',views.wordSearch, name='wordSearch')
]
