from django.shortcuts import render

# Create your views here.
def Theme(request):
    return render(request,'theme.html')