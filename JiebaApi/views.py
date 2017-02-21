from django.shortcuts import render
from django.http import JsonResponse
import jieba
import jieba.posseg as posseg
# Create your views here.
jieba.load_userdict('dbscan_w2v/NameDict_Ch_v2.txt')
def jiebacut(request):
	if request.POST and request.method == 'POST':
		data = request.POST
		data = data.dict()
		return JsonResponse(jieba.lcut(data['sentence']), safe=False)
	return JsonResponse({'result':False}, safe=False)

def jiebapos(request):
	if request.POST and request.method == 'POST':
		data = request.POST
		data = data.dict()
		return JsonResponse( list(map(lambda x:tuple(x), posseg.lcut(data['sentence']))), safe=False)
	return JsonResponse({'result':False}, safe=False)