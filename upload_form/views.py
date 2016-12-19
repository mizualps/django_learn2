from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.conf import settings
from django.http.response import HttpResponse
from upload_form.models import FileNameModel
from upload_form.models import imageFileModel
import sys, os
UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'

def form(request):
    if request.method != 'POST':
        c = {}
        c.update(csrf(request))
        return render_to_response('upload_form/form.html', c)

    file = request.FILES['file']
    path = os.path.join(UPLOADE_DIR, file.name)
    destination = open(path, 'wb')

    for chunk in file.chunks():
        destination.write(chunk)

    insert_data = FileNameModel(file_name = file.name)
    insert_data.save()

    return redirect('upload_form:complete')

def complete(request):
    return render_to_response('upload_form/complete.html')

def lookBy(request, id = None):
    fn = FileNameModel.objects.get(pk=id)
    return HttpResponse("<img src='/static/files/" + str(fn.file_name) + "'/>")
