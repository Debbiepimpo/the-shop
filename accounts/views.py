from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.contrib import auth, messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm, ContactForm
from items.models import Items
from checkout.models import Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    """View to return index"""
    return render(request, 'index.html')


def contact(request):
    """View handle contact form requests"""
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            message = request.POST['message']
            subject = request.POST['subject']
            send_mail(
                subject,
                "Message from: " +
                request.POST['email'] +
                "\nMessage: " +
                message,
                'SERVER_EMAIL',
                ['deboraperaltaorozco@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent!",
                                      extra_tags="alert-success")
            return redirect(reverse('index'))
        else:
            messages.error(request, "Unable to send message at this time",
                                    extra_tags="alert-danger")
    else:
        if request.user.is_authenticated:
            contact_form = ContactForm(initial={'email': request.user.email, 'name': request.user.get_full_name})
        else:
            contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})


@login_required
def logout(request):
    """View to log user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!",
                              extra_tags="alert-success")
    return redirect(reverse('index'))


def login(request):
    """View to log user in"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!",
                                          extra_tags="alert-success")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None,
                                     "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """View to register user"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered",
                                          extra_tags="alert-success")
                return redirect(reverse('index'))
            else:
                messages.error(
                    request,
                    "Unable to register your account at this time, please try later.",
                    extra_tags="alert-danger")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


@login_required
def orders(request):
    """A view that displays the orders page of a logged in user"""
    orders = Order.objects.filter(user_id=request.user.id).order_by('-id').exclude(status='Inactive')
    Items_bought = []
    for order in orders:
        Items_bought.append(get_object_or_404(Items_bought, pk=order.Item_id))

    """
    This paginator is for the articles_all
    into the orders section, it will show 6 items bought
    per page.
    """
    paginatorItemBought = Paginator(Items_bought, 6)

    page = request.GET.get('page')
    try:
        Items_bought = paginatorItemBought.page(page)
    except PageNotAnInteger:
        Items_bought = paginatorItemBought.page(1)
    except EmptyPage:
        Items_bought = paginatorItemBought.page(paginatorItemBought.num_pages)
        

    return render(request, 'orders.html', {'Orders':orders,
                    'Items_bought': Items_bought,
    })
