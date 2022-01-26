from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Certificate

def home_view(request):
    return render(
        request,
        "certificate/home.html"
    )

def certificate_view(request):
    reference_number=request.GET.get('reference_number')
    certificate = Certificate.objects.filter(reference_number=reference_number)
    if certificate:
        return render(
            request,
            "certificate/certificate.html",
            {
                'certificate': certificate.first()
            }
        )
    else:
        return HttpResponse("<h1>Certificate not found</h1>")
        return render(
            request,
            "certificate/certificate.html",
            context={'reference_number':reference_number}
        )