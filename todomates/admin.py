from django.contrib import admin

# 마찬가지로 모델 사용을 위해 import
from .models import *


## 여기는 기존 모델 등록
admin.site.register(Category)
admin.site.register(Todo)


## 여기는 부모 자식 쌍으로 볼 수 있도록 한 커스텀 부분
class Todo(admin.TabularInline):
    model = Todo

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        Todo,
    ]
admin.site.register(Category, CategoryAdmin)

# -> 코드의 이해보다는 코드의 사용과 용도를 알아가는게 중요할 것 같습니다!!