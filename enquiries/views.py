from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Enquiry
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def enquiry(request):
     if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
                check = Enquiry.objects.all().filter(listing_id=listing_id, user_id=user_id)
                if check:
                        messages.error(request, "An Enquiry on "+listing+" has already made")
                        return redirect("/listings/"+listing_id)

        new_enquiry = Enquiry.objects.create(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        messages.success(request, "Enquiry submitted succesfully. The realtor will get back to you shortly")
        # send_mail(
        # 'Django Application Testing',
        # 'You have applied to our enquiry for '+listing+' Please login as admin to see who has posted',
        # 'sunguru98@gmail.com',
        # [realtor_email, "rkguruin@yahoo.co.sg", "sunguru98@yahoo.co.in"],
        # fail_silently=False
        # )
        return redirect("/listings/"+listing_id)

    