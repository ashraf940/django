from django.shortcuts import render


from django.http import HttpResponse
def home(request):
    peoples = [
        {'name': 'Ashraf', 'age': 21},
        {'name': 'Qadir', 'age': 15},
        {'name': 'shahmeer', 'age': 18},
        {'name': 'Khan', 'age': 18},
        {'name': 'Asif', 'age': 17},
        {'name': 'Ali', 'age': 20},
        {'name': 'Hassan', 'age': 22},
        {'name': 'Tariq', 'age': 16}
        
    ]
    

    return render(request, "home/index.html", context = {'peoples': peoples})
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")

def success(request):
    print("*"*20)
    return HttpResponse("<h1>Success!</h1>")