from django.shortcuts import render
from django.http import HttpResponse
from .forms import RateForm

# Create your views here.
def rate_create_view(request):
    form = RateForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            age = form.cleaned_data['age']
            low_rate = 1
            high_rate = 2
            context = {
                'low_rate': calc_low_rate(age),
                'high_rate': calc_high_rate(age),
            }
            return render(request, 'rate/rate_view.html', context)
    else:
        context = {
            'form': form,
        }
        return render(request, 'rate/rate_create.html', context)

def calc_low_rate(age):
    return (208-0.7*age)*0.7

def calc_high_rate(age):
    return (208-0.7*age)*0.85
