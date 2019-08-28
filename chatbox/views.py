from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import StudentDetails

# Create your views here.


def index(request):
    return redirect('home/')

@csrf_exempt
def home(request):


    if request.method == 'POST' :

        details = StudentDetails.objects.all()
        student_list=[]
        for person in details:
            dic={}
            dic['name'] = person.name
            dic['email'] = person.email
            dic['area'] = person.Area
            dic['imageurl'] = person.image.url
            dic['subject'] = person.subject
            dic['content'] = person.content
            dic['instagram'] = person.instagram
            dic['linkedin'] = person.linkedin
            student_list.append(dic)

        return JsonResponse({'data' : student_list})


    return render(request , 'home.html')