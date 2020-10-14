from django.shortcuts import render


def cookies(request):
	template_name = 'cookies.html'
	current_color = 0xaeaeae  # default color
	if request.method == 'GET':
		if 'color' in request.COOKIES:
			current_color = request.COOKIES['color']
			print("GET:color:" + request.COOKIES.get('color'))
	elif request.method == 'POST':
		current_color = request.POST.get('color')
		print("POST:color:" + request.POST['color'])
	response = render(request, 'cookies.html', {
		'current_color': current_color
	})
	response.set_cookie('color', current_color)
	return response