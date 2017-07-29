from django.http.response import HttpResponse

def call_service(request):
	print ('check')

	return HttpResponse({True})