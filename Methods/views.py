from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect, requires_csrf_token, csrf_exempt
from django.middleware.csrf import CsrfViewMiddleware
from django.http import HttpResponseForbidden


@api_view(['GET', 'POST'])
def Cookies(request, *args, **kwargs):
    if request.method == 'GET':
        if 'name' in request.COOKIES:
            value = request.COOKIES['name']
            response = HttpResponse('Works')
            return response
        else:
            
            #response = HttpResponse()
            response = render(request, "form.html")
            response.set_cookie('simpletest', 'qwerty', httponly=True )
            # response.set_cookie('name', 'Osama', max_age=10 )
            # response.set_cookie('id', '1166', httponly=True) # httponly=True --> Cookie can't be accessed by JS
            
            return response
        
def TransferMoney(request, *args, **kwargs):
    # POST
    if request.method == 'POST':
       if request.COOKIES.get("simpletest") == "qwerty":
            response = HttpResponse("Sucess")
            return response
       else:
            response = HttpResponse("Filed")
            return response
    


@api_view(['PUT', 'DELETE',])
def Put(request, *args, **kwargs):
    if request.method == 'PUT':
        id = kwargs.get('pk')
        res = {
            "id": id,
            "username": "osama"
        }
        return Response(res)
    
    elif request.method == 'DELETE':

        return Response(f"ID: {kwargs.get("pk")} Deleted", status=204)

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request.data)
    
    elif request.method == 'POST':
        if not request.headers.get("x-auth-token"):
            return Response("No token", status=400)
        
        if request.headers.get("x-auth-token") != "123456":
            return Response("Not authorized", status=401)
        
        res = f"Loged in"
        return Response(res, status=201)

# Create your views here.
@api_view(['GET', 'POST'])
def Get_Post_Test(request): #FBV --> Function Based View

    # GET
    if request.method == 'GET':
        result = { 
            "result": "Hello from GET"
        }
        #data = request.headers.get('host')
        #data = request.headers.get('user-agent')
        data = request.headers

        return Response(data)

    # POST
    elif request.method == 'POST':
        #result = request.data
        #result = request.headers.get('Content-type')
        if not request.data.get("name"):
            return Response("Name is required", status=400)
        result = request.data.get("name")
        res = f"Hello {result}"
        return Response(res, status=201)