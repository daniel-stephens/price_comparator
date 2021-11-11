from django.shortcuts import redirect, render
from search.models import Phone, Region, Condition, Vendor

def home(request):

    
    results = []
    if request.GET.get('query'):
        phones = request.GET['query']
        results = Phone.objects.filter(name__icontains=phones)
        return render(request, 'results.html', {'requests':results})
    else:
        return render(request, 'home.html')
    


def results_view(request):

    vendors = Vendor.objects.all()
    regions = Region.objects.all()
    conditions = Condition.objects.all()
    results = []

    if request.GET.get('query'):

        phones = request.GET['query']
        results = Phone.objects.filter(name__icontains=phones)
        
    return render(request, 'results.html', {'results':results, 'regions':regions, 'conditions':conditions})

