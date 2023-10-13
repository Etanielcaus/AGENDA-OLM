from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from contact.models import Contact


def create(request):
    context = {

    }

    # renderizando o template
    return render(
        request,
        'contact/create.html',
        context
    )
