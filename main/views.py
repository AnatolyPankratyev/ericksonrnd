from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


def index_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data[
                'message']
            copy = form.cleaned_data['copy']

            recipients = ['info@ericksonkazan.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'main/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'main/index.html', {'form': form})


def about_coaching_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data[
                'message']
            copy = form.cleaned_data['copy']

            recipients = ['info@ericksonkazan.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'main/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'main/aboutCoaching.html', {'form': form})


def basic_course_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data[
                'message']
            copy = form.cleaned_data['copy']

            recipients = ['info@ericksonkazan.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'main/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'main/basicCourse.html', {'form': form})


def science_and_art_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data[
                'message']
            copy = form.cleaned_data['copy']

            recipients = ['info@ericksonkazan.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'main/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'main/scienceAndArt.html', {'form': form})


def contacts_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data[
                'message']
            copy = form.cleaned_data['copy']

            recipients = ['info@ericksonkazan.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'main/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'main/contacts.html', {'form': form})


def for_business_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data[
                'message']
            copy = form.cleaned_data['copy']

            recipients = ['info@ericksonkazan.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'main/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'main/forBusiness.html', {'form': form})


def management_coaching_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data[
                'message']
            copy = form.cleaned_data['copy']

            recipients = ['info@ericksonkazan.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'main/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'main/managementCoaching.html', {'form': form})


def mentoring_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data[
                'message']
            copy = form.cleaned_data['copy']

            recipients = ['info@ericksonkazan.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'main/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'main/mentoring.html', {'form': form})


def professional_community_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data[
                'message']
            copy = form.cleaned_data['copy']

            recipients = ['info@ericksonkazan.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'main/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'main/professionalCommunity.html', {'form': form})


def training_programs_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data[
                'message']
            copy = form.cleaned_data['copy']

            recipients = ['info@ericksonkazan.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'main/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'main/trainingPrograms.html', {'form': form})
