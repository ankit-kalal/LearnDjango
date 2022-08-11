from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView,CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import *
# Create your views here.
from accounts.models import CustomUser,Seller,SellerAdditional
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    return render(request,'App/base.html')



class Index(TemplateView):
    template_name = 'App/base.html'

    def get_context_data(self ,**kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['data'] = "i am string"
        return context


def contactUs(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form  = ContactUsForm(request.POST)
        if form.is_valid():
            if len(form.cleaned_data.get('query'))>10:
                form.add_error('query','Query lenght is not right')
                return render(request, 'App/contactUs.html', {'form':form})
            form.save()
            return HttpResponse("Thank YOu")
        else:
            if len(form.cleaned_data.get('query'))>10:
                form.add_error('query','Query lenght is not right')
                return render(request, 'App/contactUs.html', {'form':form})

    return render(request,'App/contactUs.html',{'form':form})



class ContactUs(FormView):
    form_class = ContactUsForm
    template_name = 'App/contactUs.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if len(form.cleaned_data.get('query'))>10:
            form.add_error('query', 'Query length is not right')
            return render(self.request, 'firstapp/contactus2.html', {'form':form})
        form.save()
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        if len(form.cleaned_data.get('query'))>10:
            form.add_error('query', 'Query length is not right')
        response = super().form_invalid(form)
        return response



# class RegisterView(CreateView):
#     template_name = 'App/register.html'
#     form_class = RegistrationForm
#     success_url = reverse_lazy('index')

#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         if response.status_code == 302:
#             gst = request.POST.get('gst')
#             warehouse_location = request.POST.get('warehouse_location')
#             user = CustomUser.objects.get(email = request.POST.get('email'))
#             s_add = SellerAdditional.objects.create(user = user, gst = gst, warehouse_location = warehouse_location)
#             return response
#         else:
#             return response




class LoginViewUser(LoginView):
    template_name = "App/login.html"
    # success_url = reverse_lazy('index')

class RegisterView(CreateView):
    template_name = 'App/registerUser.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index')


class RegisterViewSeller(LoginRequiredMixin, CreateView):
    template_name = 'App/registerSeller.html'
    form_class = RegistrationFormSeller
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = self.request.user
        user.type = user.Types.SELLER
        # user.type.append(user.Types.SELLER)
        user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)


