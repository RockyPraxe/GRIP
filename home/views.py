from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from blog.models import Post
from products.models import Product

# Create your views here.


# def index(request):
#     """ A view to return the index page """

#     return render(request, 'home/index.html')


def index(request):
    """
    View to return the index page
    """
    posts = Post.objects.all()
    # Fetch the three newest posts for display
    latest_posts = Post.objects.order_by("-created_on")[:3]
    # new_arrivals = Product.objects.order_by("-created_at")

    context = {
        "posts": latest_posts,
        # "products": new_arrivals,
    }
    return render(request, "home/index.html", context)


def contact(request):
    """
    Render contact.html view
    """
    return render(request, "home/support/contact.html")


def contact_form(request):
    """
    Contact form view
    """
    template = "home/support/contact_form.html"
    form = ContactForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = ContactForm(request.POST, request.FILES)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.user = request.user
                contact.save()
                messages.success(request, "Successfully form submission!")
                return redirect(reverse("contact_form"))
            else:
                messages.error(
                    request,
                    "Failed to submit the form. "
                    "Please ensure the form is valid.",
                )
        else:
            messages.warning(request, "You need to be logged in.")
    context = {
        "form": form,
    }
    return render(request, template, context)
