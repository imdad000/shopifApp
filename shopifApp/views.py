from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect

def home_page(request):
	context={
	 "title":"Hello Home Page",
	 "content":"Welcome to Home Page"
	}
	return render(request,"home_page.html",context)
