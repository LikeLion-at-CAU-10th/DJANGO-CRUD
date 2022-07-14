from django.urls import path
from .views import *

urlpatterns = [
    path('create-category/', create_category, name="create-category" ),
    path('get-category-all/', get_category_all, name= 'get-category-all'),
    
    # id 값을 url을 통해 함수에 전달하는 문법
    # url 뒤에 있는 숫자를 int 취급하여 함수의 id 매개변수에 줘라~ 
    path('get-category/<int:id>', get_category, name= 'get-category'),
    path('update-category/<int:id>', update_category, name= 'update-category'),
    path('delete-category/<int:id>', delete_category, name= 'delete-category'),
    
    path('create-todo/<int:category_id>', create_todo, name= 'create-todo'),


]