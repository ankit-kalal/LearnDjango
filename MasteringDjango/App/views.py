from django.http import HttpResponse
from django.shortcuts import render
from django.urls import is_valid_path
from django.views.generic import TemplateView
# Create your views here.
from .forms import ContactUsForm

def index(request):
    return render(request,'App/base.html')



class Index(TemplateView):
    template_name = 'App/base.html'

    def get_context_data(self ,**kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['data'] = "i am string"
        return context



def contackus(request):
    if request.method == "POST":
        print("post")
        form = ContactUsForm(request.POST)
        if form.is_valid():
            if len(form.cleaned_data.get('query'))>10:
                form.add_error('query', 'Query length is not right')
                return render(request, 'App/contackus.html', {'form':form})
            form.save()
            return HttpResponse("thanks")
        else:
            if len(form.cleaned_data.get('query'))>10:
                form.add_error('query', 'Query length is not right')
            return render(request,'App/contackus.html',{'form':form})
    form = ContactUsForm
    return render(request,'App/contackus.html',{'form':form})
