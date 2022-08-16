import random
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import FileForm
from .models import TestFile


def index(req):
    return render(req, "main/index.html")


def upload_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = TestFile(
                name=str(random.randint(0, 1000)),
                file=request.FILES["docfile"],
            )
            newdoc.save()

            return HttpResponseRedirect("/upload_file")
    else:
        form = FileForm()

    documents = TestFile.objects.all()

    return render(
        request,
        "main/upload.html",
        {"documents": documents, "form": form},
    )
