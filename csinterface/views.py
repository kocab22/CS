from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Company, PriceBid, Part
from .forms import NewPriceBidForm


def home(request):
    companies = Company.objects.all()
    bids = PriceBid.objects.all()
    
    for company in companies:
        bid_count = PriceBid.objects.all()
    context = {'companies':companies, 'bids':bids,'bid_count': bid_count, 'company': company}
    return render(request, 'home.html', context)

def company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    bids = PriceBid.objects.all()
    context = {'company':company, 'bids':bids}
    return render(request, 'company.html', context)

def about(request):
    # user = user.objects.first() #TODO: vezme aktualne prihlaseneho uzivatele
    
    if request.method == 'POST':
        form = NewPriceBidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewPriceBidForm()
    context = {'form':form}
    return render (request, 'about.html', context)
    
    

def price_bid(request, id):
    price_bid = get_object_or_404(PriceBid, id=id)
    parts_list = price_bid.parts.all()
    return render(request, 'price_bid.html', {'price_bid':price_bid, 'parts_list':parts_list,})
    
def new_bid(request, pk):
    company = get_object_or_404(Company, pk=pk)
    initial_company = company.pk

    if request.method == 'POST':
        form = NewPriceBidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = NewPriceBidForm(initial={'company': initial_company})
        
    context = {'company':company,'form':form}
    return render (request, 'new_bid.html', context)

def test(request, pk):
    company = get_object_or_404(Company, pk=pk)

    if request.method == 'POST':
        form = NewPriceBidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewPriceBidForm()
        
    context = {'company':company,'form':form}
    return render (request, 'test.html', context)