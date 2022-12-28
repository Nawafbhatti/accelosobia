from django.shortcuts import render
from account.models import CONTACT, CAREER_DATA
from threading import Thread
from django.conf import settings
from django.template.loader import render_to_string

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# def contact_confirmation_email(email, request):

#     current_site = get_current_site(request)
#     email_subject = "Accelsobio mindcure"
#     email_body = render_to_string('accounts/email_confirmation.html', {
# 		"domain":current_site,
# 	})
#     email = EmailMessage(subject=email_subject, body=email_body, from_email=settings.EMAIL_FROM_USER, to=[email])
#     email.send()


def index(request):

	if request.method == "POST":
		name = request.POST.get("name", False)
		email = request.POST.get("email", False)
		note = request.POST.get("note", False)

		create_contact = CONTACT.objects.create(name=name, email=email, note=note)
		create_contact.save()

		user_mail = email
		subject, from_email, to = "Accelsobio LLC", settings.EMAIL_HOST_USER, user_mail
		html_content = render_to_string('accounts/email_confirmation.html')
		text_content = strip_tags(html_content)
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to],)
		msg.attach_alternative(html_content, "text/html")
		try:
			msg.send()
		except:
			pass

	return render(request, "index.html")

def career(request):

	if request.method == "POST":
		name = request.POST.get("name", False)
		email = request.POST.get("email", False)
		note = request.POST.get("note", False)

		create_contact = CAREER_DATA.objects.create(name=name, email=email, note=note)
		create_contact.save()

		# thread_for_client = Thread(target=contact_confirmation_email, args=(email, request))
		# thread_for_client.setDaemon(True)
		# thread_for_client.start()

	return render(request, "career.html")

def about(request):

	if request.method == "POST":
		name = request.POST.get("name", False)
		email = request.POST.get("email", False)
		note = request.POST.get("note", False)

		create_contact = CONTACT.objects.create(name=name, email=email, note=note)
		create_contact.save()

		thread_for_client = Thread(target=contact_confirmation_email, args=(email, request))
		thread_for_client.setDaemon(True)
		thread_for_client.start()


	return render(request, "about.html")

def our_work(request):
	return render(request, "our_work.html")

def partnership(request):
	return render(request, "partnership.html")

def privacy_policy(request):
	return render(request, "privacy_and_policy.html")

def who_we_are(request):
	return render(request, "who_we_are.html")

def test(request):
	return render(request, "test.html")


def partnership2(request):
	return render(request, "partnership2.html")