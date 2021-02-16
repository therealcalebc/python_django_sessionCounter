from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	if 'page_views' in request.session:
		request.session['page_views'] += 1
	else:
		request.session['page_views'] = 1
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1
	context = {
		"title": "Counter"
	}
	return render(request, 'index.html', context)

def add_two(request):
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1
	return redirect('/')

def add_custom(request):
	count = 0
	incr = int(request.POST['custom_increment_amount'])
	if 'count' in request.session:
		count = request.session['count']
		if incr > 0:
			count += incr - 1
	else:
		count = 0
	request.session['count'] = count
	return redirect('/')

def reset(request):
	if 'count' in request.session:
		del request.session['count']
	return redirect('/')