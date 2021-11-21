from django.shortcuts import render
from search.models import Phone, Region, Condition, Vendor
from django.core.paginator import Paginator
from .form import RegionForm, ConditionForm


regionform = RegionForm()
conditionform = ConditionForm()
regions = Region.objects.all()
conditions = Condition.objects.all()

def home(request):

    
    results = []
    if request.GET.get('query'):
        phones = request.GET['query']
        results = Phone.objects.filter(name__icontains=phones)


        return render(request, 'results.html', {'requests':results})
    else:
        return render(request, 'home.html')
    
def filters(request):
    region=regionform(request.GET)
    if region.is_valid():
        selected = region.cleaned_data['region']
        print(selected)
    return render(request, ".html", {'region':region})


def results_view(request):
   
    results = []
    
    if request.GET.get('query'):

        phones = request.GET['query']
        results = Phone.objects.filter(name__icontains=phones)
        paginator = Paginator(results, 20)
        page  = request.GET.get('page')
        results = paginator.get_page(page)

        return render(request, 'results.html', {'results':results, 'regions':regions, 'conditions':conditions, 'phones':phones})

    return render(request, 'results.html', {'results':results, 'regions':regions, 'conditions':conditions})



def radio(request):
    
    return render(request, 'radio.html', {"regions" : regions, "conditions": conditions } )




