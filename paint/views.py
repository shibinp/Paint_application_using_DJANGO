from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
'''
from django.template.loader import get_template

def pnt(request):
    return render(request,'paintapp.html',{})
'''
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import RequestContext
from paint.models import Pic
from django.template import Context
'''
from django.http import HttpResponse
from django.template.loader import get_template

from paint.models import Image
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
'''
def home(request):
    return render_to_response('paintapp.html')
def galle(request):
    return render_to_response('paintapp.html')

@csrf_exempt
def save(request):
	iname=request.POST.get('name')
	idata=request.POST.get('data')
	p=Pic(name=iname,data=idata)
	p.save()
	return render_to_response('paintapp.html')
'''
	t = get_template('home2.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
'''
def gall(request):
	posts=[dict(id=i.id,title=i.name) for i in Pic.objects.order_by('id')]
	return render(request, 'gallery.html', {'posts': posts})


def load(request,imgname):
        data=Pic.objects.filter(name=imgname)
        print data[0].id
	for i in Pic.objects.filter(name=imgname):
		print i.id
	posts=[dict(id=i.id,title=i.name,imagedata=i.data) for i in Pic.objects.filter(name=imgname)]
	return render(request,'picload.html',{'posts':posts})

