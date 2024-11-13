from django.shortcuts import render
from . form import Form1
# Create your views here.

def form(reqquest):
    form1=Form1()
    return render(reqquest,'form.html',{'form':form1})