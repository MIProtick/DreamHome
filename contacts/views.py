from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if the user make same query before
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "This query has already been made by you!!")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, 
        name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        """Configure the (sender_email here | EMAIL_HOST_USER and EMAIL_HOST_PASSWORD at settings file)"""
        # send_mail(
        #     'Property listing Inquery',
        #     'There has been an inquery for "'+ listing + '". SIgn into the admin panel for more info.',
        #     'sender_email',
        #     [realtor_email],
        #     fail_silently=False
        # )

        messages.success(request, "Your request has been submitted, a realtor will get back to you soon")
        return redirect('/listings/'+listing_id)

