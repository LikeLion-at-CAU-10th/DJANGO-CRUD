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
    
    ## SESSION 03

    ## 이 두 친구의 동작은 category(부모) id 값이 인자로 필요함
    path('create-todo/<int:category_id>', create_todo, name= 'create-todo'),
    path('get-todo-all/<int:category_id>', get_todo_all, name="get-todo-all"),
    
    ## 이 친구들의 동작은 todo id 값이 인자로 필요함
    path('get-todo/<int:todo_id>', get_todo, name="get-todo"),
    path('update-todo/<int:todo_id>', update_todo, name="update-todo"),
    path('delete-todo/<int:todo_id>', delete_todo, name="delete-todo"),

]