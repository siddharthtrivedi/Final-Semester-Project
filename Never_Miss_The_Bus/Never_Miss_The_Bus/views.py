from django.shortcuts import render

def home(request):
	context = {}
	template = "Home.html"
	return render(request, template, context)