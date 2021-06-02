from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args, **kwargs):
    # print(request.user)
    return render(request,"home.html",{})

def  contact_view(request,*args, **kwargs):
    my_context={
        "my_text":"This is our contact",
        "my_number":123,
        "my_html":"<h1>Hello World</h1>",
        "my_list":[123,22,44,3,'Abc']
    }
    return render(request,"contact.html",my_context)