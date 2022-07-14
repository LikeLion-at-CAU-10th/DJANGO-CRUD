from django.shortcuts import get_object_or_404
from .models import *
from django.http.response import JsonResponse
import json

# Create your views here.
def create_category(request):
    # 생성 과정은 post 요청에만 일어나도록!
    if request.method == "POST":

        # requests에 담겨서 온 데이터를 디코딩하기!(사용할 수 있도록 json 화)
        body =  json.loads(request.body.decode('utf-8'))
        
        # 장고 orm 을 통해 가져온 데이터의 자료형은 "queryset"이라는 특별한 자료형입니다.
        new_category = Category.objects.create(
            # requests에서 넘어온 데이터로 새로운 Category 생성)
            title       =  body['title'],
            view_auth   =  body['view_auth'],
            color       =  body['color']
        )

        # queryset 자료를 json 모양으로 데이터를 이쁘게 정리해주기
        new_category_json={
            "id"        : new_category.id,
            "title"     : new_category.title,
            "view_auth" : new_category.view_auth,
            "color"     : new_category.color,
            "pup_date"  : new_category.pup_date,
        }

        # 성공 할 경우 client가 받을 데이터 모양
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '생성 성공!',
                'data': new_category_json    # 이쁘게 만든 데이터를 respons['data']에 담아 보내줌
            })

    # request.method에 대한 분기처리(post 가 아닌경우)
    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
        })

## category 로 생성된 모든 데이터를 가져오는 함수
def get_category_all(requests):
    # 생성 과정은 get 요청에만 일어나도록!
    if requests.method == 'GET':
        # 쿼리셋 모양으로 가져옴(쿼리셋 모양은 for문 적용 가능)
        category_all = Category.objects.all() 

        ### 특정 속성의 category 여러개를 가져오고 싶을 때 ### 
        Category.objects.filter(view_auth = 0) # 여러개
        ###

        # 이쁘게 만들기
        # 여기에 최종 json 모양의 데이터가 담겨서 전달될 예정
        category_json_all=[] 
        for category in category_all:
            category_json={
                "id"        : category.id,
                "title"     : category.title,
                "view_auth" : category.view_auth,
                "color"     : category.color,
                "pup_date"  : category.pup_date,
            }
            category_json_all.append(category_json) # 나중에 serializer 배우면 생략 가능한 부분!!
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'category_all 수신 성공!',
                'data': category_json_all
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

# 많은 category 중 특정 id값(다른 속성도 가능하지만 보통 id)을 갖고 있는 category 를 가져오는 함수 
# 매개변수로 id 값도 받는다(url을 통해 전달)
def get_category(request, id):
    if request.method == "GET":
        
        # 특정한 category 하나를 가져오는 함수
        # pk는 실제로 모델이 id 값을 저장하고 있는 필드
        # => Category 모델로 저장된 애들중 pk 값이 id인 놈 가져와!! 아니면 404
        category = get_object_or_404(Category, pk = id)

        # 가져와서 이쁘게 만들기
        category_json={
                "id"        : category.id,
                "title"     : category.title,
                "view_auth" : category.view_auth,
                "color"     : category.color,
                "pup_date"  : category.pup_date,
        }
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'category 수신 성공!',
                'data': category_json
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

# 업데이트 또한 특정 category 의 정보를 바꾸는 일이기 때문에 id 값 받음
def update_category(request, id):
    # PATCH 메소드 사용함 주의
    if request.method == "PATCH":
        # 변경내용이 들어가 있는 body 수신
        body =  json.loads(request.body.decode('utf-8'))

        # 변강할 category 가져와서 해당 변수에 저장
        update_category = get_object_or_404(Category, pk = id)

        # 변수.필드명 을 통해 해당 속성에 접근, 변경(생셩과 비슷)
        update_category.title = body['title']
        update_category.view_auth = body['view_auth']
        update_category.color = body['color']

        # 해당과정으로 변경할 경우 꼭 .save()를 통해 저장 필요
        update_category.save()
        
        # 이쁘게 만들기
        update_category_json={
            "id"        : update_category.id,
            "title"     : update_category.title,
            "view_auth" : update_category.view_auth,
            "color"     : update_category.color,
            "pup_date"  : update_category.pup_date,
        }

        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '업데이트 성공!',
                'data': update_category_json
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

# 삭제 과정 또한 특정 category에 대한 보가 필요하여 id 값 받음
def delete_category(request, id):
    # method -> DELETE 주의
    if request.method == "DELETE":

        delete_category = get_object_or_404(Category, pk = id)
        # 그냥 이렇게 삭제하면 됨,,ㅎ
        delete_category.delete()
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '삭제 성공!',
                'data': None    #삭제의 경우 성공해도 데이터를 줄게 없음
            })
    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
        })


def create_todo(request, category_id):
    if request.method == "POST":

        # 이미지 파일이 있으므로 request에서 구분하여 받기
        body =  request.POST
        img = request.FILES['thumb_nail']
        
        new_todo = Todo.objects.create(
            # 'Category' X // Category(O)
            category = get_object_or_404(Category, pk = category_id),
            content = body['content'],
            thumb_nail = img
        )

        # queryset 자료를 json 모양으로 데이터를 이쁘게 정리해주기
        new_todo_json={
            "id"        : new_todo.id,
            "title"     : new_todo.content,
            "thumb_nail" : '/media/' + str(new_todo.thumb_nail),
            "pup_date"  : new_todo.pup_date,
        }

        # 성공 할 경우 client가 받을 데이터 모양
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo 생성 성공!',
                'data': new_todo_json    # 이쁘게 만든 데이터를 respons['data']에 담아 보내줌
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
        })

def get_todo_all(request, category_id):
    if request.method == "GET":

        ## 중요!! todo_all 에서는 모든 todo를 받아오는 것이 아니다!!
        ## 부모요소의 키값을 fk 로 갖고 있는 놈들 다가져오기 -> filter!!
        category_todo = Todo.objects.filter(category = category_id)
        

        # 이후 클라이언트가 필요한 모양으로 데이터 이쁘게~~
        category_todo_json=[]
        for todo in category_todo:
            new_set={
                "todo_id" : todo.id,
                "content" : todo.content,
                "thumb_nail" : "/media/" + str(todo.thumb_nail),
                "is_completed" : todo.is_completed,
                "pup_date" : todo.pup_date
            }
            category_todo_json.append(new_set)
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo_all 수신 성공!',
                'data': category_todo_json
            })

    return JsonResponse({
            'status': 405,
            'success': False,
            'message': 'method error',
            'data': None
        })


# 예는 특정 todo 하나만 불러오므로 todo_id 값을 인자로 받아야함!!!
def get_todo(request, todo_id):
    if request.method == "GET":

        # 해당 todo_id 에 해당하는 Todo 모델 가져오기
        todo = get_object_or_404(Todo, pk = todo_id)
        todo_json={
            "todo_id" : todo.id,
            "content" : todo.content,
            "thumb_nail" : "/media/" + str(todo.thumb_nail),
            "is_completed" : todo.is_completed,
            "pup_date" : todo.pup_date
        }
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo 수신 성공!',
                'data': todo_json
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

def update_todo(request, todo_id):
    if request.method == "POST":
        
        ### 중요!! method 를 UPDATE 로 진행하지 않고 POST로 진행!!
        body = request.POST
        img = request.FILES['thumb_nail']

        # 수정방법은 객체를 불러와서 각 속성에 접근하면 됨!!
        update_todo = get_object_or_404(Todo,pk = todo_id)
        update_todo.content = body['content']
        update_todo.is_completed = body['is_completed']
        update_todo.thumb_nail = img
        update_todo.save()

        
        update_todo_json={
            "id" : update_todo.id,
            "content" : update_todo.content,
            "thumb_nail" : "/media/"+ str(update_todo.thumb_nail),
            "is_completed" : update_todo.is_completed,
            "pup_date" : update_todo.pup_date
        }
        

        return JsonResponse({
            'status': 200,
            'success': True,
            'message': 'Todo 업데이트 성공!',
            'data': update_todo_json
        })

    return JsonResponse({
        'status': 405,
        'success': False,
        'message': 'method error',
        'data': None
    })

def delete_todo(request, todo_id):

    if request.method == "DELETE":
        delete_todo = get_object_or_404(Todo, pk = todo_id)
        delete_todo.delete()

        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo 삭제 성공!',
                'data': None
            })

    return JsonResponse({
            'status': 405,
            'success': False,
            'message': 'method error',
            'data': None
        })