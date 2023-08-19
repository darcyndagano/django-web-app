from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})


def band_change(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_change.html', {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()  # suppression dans la base de données
        return redirect('band-list')  # redirige vers la liste des bandes

    return render(request, 'listings/band_delete.html', {'band': band})


def listings(request):
    list = Listing.objects.all()
    return render(request, 'listings/listings_list.html', {'list': list})


def listing_detail(request, id):
    list = Listing.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', {'list': list})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})


def listing_change(request, id):
    list = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=list)
        if form.is_valide():
            form.save()
            return redirect('listing-detail', list.id)
    else:
        form = ListingForm(instance=list)
    return render(request, 'listings/listing_change.html', {'form': form})


def listing_delete(request, id):
    list = Listing.objects.get(id=id)
    if request.method == 'POST':
        list.delete()
        return redirect('listing-list')
    return render(request, 'listings/listing_delete.html', {'list': list})


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchez.xyz']
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request,
                  'listings/contact.html',
                  {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')


def about(request):
    return render(request, 'listings/about.html')
