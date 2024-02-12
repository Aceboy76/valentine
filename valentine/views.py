from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Valentine


class ValentineView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class FormView(View):
    template_name = "form.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs): 
        if request.method == "POST":
            name = request.POST.get("name")
            date = request.POST.get("date")
            message = request.POST.get("message")

            new_valentine = Valentine(name=name, date=date, message=message)
            new_valentine.save()

            return redirect("home")