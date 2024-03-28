from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic.edit import FormMixin
from .forms import SpecialistReviewForm, UserUpdateForm, ProfileUpdateForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Specialist, Client, Services
from .scrapers.delfi import img_title, img_links, links


def base(request):
    context = {
        'img_title': img_title,
        'img_links': img_links,
        'links': links,
        'title': 'Beauty',
    }
    return render(request, 'beauty/base.html', context)


def services(request):
    services_list = Services.objects.all()
    return render(request, 'beauty/services.html', {'services': services_list})


def specialist(request):
    specialist_list = Specialist.objects.all()
    return render(request, 'beauty/specialist.html', {'specialist': specialist_list})


class SpecialistListView(generic.ListView):
    model = Specialist
    template_name = 'beauty/specialist_list.html'
    extra_context = {'title': 'Home page'}


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
    query: str = request.GET.get('query')
    search_results = Specialist.objects.filter(Q(company__icontains=query) | Q(address__icontains=query))
    return render(request, 'beauty/search.html', {'specialist': search_results, 'query': query})


@csrf_protect
def register(request):
    if request.method == "POST":
        username: str = request.POST['username']
        first_name: str = request.POST['first_name']
        last_name: str = request.POST['last_name']
        phone_number: str = request.POST['phone_number']
        email: str = request.POST['email']
        password: str = request.POST['password']
        password2: str = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if Client.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if Client.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    Client.objects.create(first_name=first_name, username=username, last_name=last_name,
                                          phone_number=phone_number,
                                          email=email, password=password, register=timezone.now(),
                                          logo='profile_pics/default.png')
                    messages.info(request, f'Klientas  {first_name} {last_name} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'beauty/register.html')


@login_required
def view_profile(request):
    return render(request, 'beauty/profile.html')


@login_required
def update_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile update")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'beauty/profile.html', context)


class SpecialistsByUserListView(LoginRequiredMixin, ListView):
    model = Specialist
    context_object_name = 'specialists'
    template_name = 'beauty/user_client.html'
    paginate_by = 10

    def get_queryset(self):
        return Specialist.objects.filter(company=self.request.user)


class SpecialistByUserDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'beauty/user_specialist.html'


def client():
    pass


def registration():
    pass
