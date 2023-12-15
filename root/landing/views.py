from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm, SubscribeForm

def contact_subscribe(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        subscribe_form = SubscribeForm(request.POST)

        if contact_form.is_valid():
            # Retrieve user's email from the form
            user_email = contact_form.cleaned_data['email']

            # Do something with the valid contact form data (e.g., save to database)
            contact_form.save()

            # Construct email message with all contact form data
            message = "New Contact Form Submission\n\n"
            for field, value in contact_form.cleaned_data.items():
                message += f"{field.capitalize()}: {value}\n"

            # Send email notification
            send_mail(
                'New Contact Form Submission',
                message,
                'iamparasghimire@gmail.com',  # Replace with your email
                ['iamparasghimire@gmail.com'],  # Replace with recipient email(s)
                fail_silently=False,
            )

            return redirect('/')  # Redirect to a success page

        if subscribe_form.is_valid():
            # Retrieve user's email from the form
            user_email = subscribe_form.cleaned_data['email']

            # Do something with the valid subscribe form data (e.g., save to database)
            subscribe_form.save()

            # Construct email message with all subscribe form data
            message = "New Subscribe Form Submission\n\n"
            for field, value in subscribe_form.cleaned_data.items():
                message += f"{field.capitalize()}: {value}\n"

            # Send email notification
            send_mail(
                'New Subscribe Form Submission',
                message,
                'iamparasghimire@gmail.com',  # Replace with your email
                ['iamparasghimire@gmail.com'],  # Replace with recipient email(s)
                fail_silently=False,
            )

            return redirect('/')  # Redirect to a success page

    else:
        contact_form = ContactForm()
        subscribe_form = SubscribeForm()

    return render(request, "landing/index.html", {'contact_form': contact_form, 'subscribe_form': subscribe_form})
