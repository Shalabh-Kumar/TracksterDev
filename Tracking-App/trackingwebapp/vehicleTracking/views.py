from django.shortcuts import render

def index(request):
	return render(request, 'vehicleTracking/home.html')

def about(request):
	# about url
	return render(request, 'vehicleTracking/about.html',{'content':['About Us','Tracking Company']})