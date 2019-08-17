from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
import requests
import json
from django.views.decorators.csrf import csrf_exempt

RUN_URL = 'http://api.hackerearth.com/code/run/'
def index(request):
	return render(request, 'base.html')

#From HackerEarth API
@csrf_exempt
def runCode(request):
	if request.is_ajax():
		source = request.POST.get('source')
		lang = request.POST.get('lang')
		data = {
			'client_id': 'a917a3f15fb08e0b663a55455590076d0b72a8cc60f6.api.hackerearth.com',
			'client_secret': '6907eaad6d8a58c66dd7827a9e7a1f7480785f10',
			'async': 0,
			'source': source,
			'lang': lang,
			'time_limit': 5,
			'memory_limit': 262144,
		}
		print(data)
		if 'input' in request.POST:
			data['input'] = request.POST['input']
		r = requests.post('http://api.hackerearth.com/code/run/', data=json.dumps(data))
		return JsonResponse(r.json(), safe=False)
	else:
		return HttpResponseForbidden()