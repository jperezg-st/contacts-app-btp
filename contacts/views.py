from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'index.html', {'contacts': contacts, 'search_input': search_input})

def addContact(request):
    if request.method == 'POST':

        new_contact = Contact(
            name=request.POST['Name'],
            last_name=request.POST['last_name'],
            company=request.POST['company'],
            phone_number=request.POST['phone-number'],
            email=request.POST['email'],
            )
        new_contact.save()
        return redirect('/')

    return render(request, 'new.html')

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.name = request.POST['Name']
        contact.last_name = request.POST['last_name']
        contact.company = request.POST['company']
        contact.phone_number = request.POST['phone-number']
        contact.email = request.POST['email']
        contact.save()

        return redirect('/profile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')

    return render(request, 'delete.html', {'contact': contact})

def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact':contact})
