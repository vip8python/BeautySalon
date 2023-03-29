from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import *
from django.views import generic
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic.edit import FormMixin
from .forms import *
from django.db.models import Q


def base(request):
    return render(request, 'beauty/base.html', {'title': 'Beauty'})


def services(request):
    sevices_list = Services.objects.all()
    return render(request, 'beauty/services.html', {'services': sevices_list})


def client(request):
    pass


def specialist(request):
    specialist_list = Specialist.objects.all()
    return render(request, 'beauty/specialist.html', {'specialist': specialist_list})

def registration(request):
    pass

class SpecialistListView(generic.ListView):
    model = Specialist
    template_name = 'beauty/specialist_list.html'

class SpecialistDetailView(FormMixin, generic.DetailView):
    model = Specialist
    template_name = 'beauty/specialist_detail.html'
    form_class = SpecialistReviewForm

    def get_success_url(self):
        return reverse('specialist_detail', kwargs={'pk': self.object.id})


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        form.instance.specialist = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(SpecialistDetailView, self).form_valid(form)




def search(request):
    query = request.GET.get('query')
    search_results = Specialist.objects.filter(Q(company__icontains=query) | Q(address__icontains=query))
    return render(request, 'beauty/search.html', {'specialist': search_results, 'query': query})

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'beauty/register.html')
