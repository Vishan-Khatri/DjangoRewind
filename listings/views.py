from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Listing, ContactMessage
from .forms import ListingForm, ContactForm, SearchForm

def home(request):
    listings = Listing.objects.filter(is_active=True)[:6]
    return render(request, 'listings/home.html', {'listings': listings})

def listing_list(request):
    form     = SearchForm(request.GET or None)
    listings = Listing.objects.filter(is_active=True)
    if form.is_valid():
        d = form.cleaned_data
        if d.get('city'):       listings = listings.filter(city=d['city'])
        if d.get('room_type'):  listings = listings.filter(room_type=d['room_type'])
        if d.get('gender'):     listings = listings.filter(gender_pref__in=[d['gender'], 'A'])
        if d.get('rent_min'):   listings = listings.filter(rent__gte=d['rent_min'])
        if d.get('rent_max'):   listings = listings.filter(rent__lte=d['rent_max'])
        if d.get('furnished'):  listings = listings.filter(furnished=True)
        if d.get('wifi'):       listings = listings.filter(wifi=True)
    return render(request, 'listings/listing_list.html', {'listings': listings, 'form': form})

def listing_detail(request, pk):
    listing      = get_object_or_404(Listing, pk=pk, is_active=True)
    contact_form = ContactForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, 'Please log in to send a message.')
            return redirect('login')
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            msg = contact_form.save(commit=False)
            msg.listing = listing
            msg.sender  = request.user
            msg.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('listing_detail', pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing, 'contact_form': contact_form})

@login_required
def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            messages.success(request, 'Listing posted successfully!')
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_form.html', {'form': form, 'action': 'Post'})

@login_required
def listing_edit(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listing updated!')
            return redirect('listing_detail', pk=pk)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_form.html', {'form': form, 'action': 'Edit'})

@login_required
def listing_delete(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    if request.method == 'POST':
        listing.is_active = False
        listing.save()
        messages.success(request, 'Listing removed.')
        return redirect('my_listings')
    return render(request, 'listings/listing_confirm_delete.html', {'listing': listing})

@login_required
def my_listings(request):
    listings = Listing.objects.filter(owner=request.user, is_active=True)
    return render(request, 'listings/my_listings.html', {'listings': listings})

@login_required
def my_messages(request):
    # Messages received on user's listings
    received = ContactMessage.objects.filter(listing__owner=request.user).order_by('-created_at')
    sent     = ContactMessage.objects.filter(sender=request.user).order_by('-created_at')
    return render(request, 'listings/my_messages.html', {'received': received, 'sent': sent})
