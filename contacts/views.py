from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail # This is importing the package useful for sending mail
from .models import Contact # This is importing the contact model from models.py

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

    #  Check if user has made inquiry already
    # This below code prevents from making multiple times of enquiries on the same site
    if request.user.is_authenticated:
      user_id = request.user.id
      # In the below line we are checking whether id of an user making an inquiry is already there or not
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email
    send_mail(
        'Property Listing Inquiry',
        'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        'glakshmi.nyros@gmail.com', # This is the from email address
        [realtor_email, 'glakshmi.nyros@gmail.com'], # This is to email address means we are specifiying where should the email goes
        fail_silently=False
        )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listing_id)
