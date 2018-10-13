from django.shortcuts import render, redirect

# Create your views here.
from cms.models import Text


def index(request, slug):
    texts = Text.objects.all().order_by('number')
    contents = Text.objects.get(id=slug)
    return render(request, 'index.html', {'texts': texts, 'conts': contents})


def redir(request):
    return redirect('/index/2')
