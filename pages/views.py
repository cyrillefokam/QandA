from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecordForm
from .models import Record
from django.contrib import messages
from .utils import ask_chatgpt


def home(request):
    return render(request, "pages/home.html")


@login_required
def generator(request):
    if request.POST:
        form = RecordForm(request.POST)

        if form.is_valid():
            form.instance.author=request.user
            try:
                print(form.instance.composer, form.instance.topic,
                    form.instance.number, form.instance.input == 'a')
                data = ask_chatgpt(form.instance.composer, form.instance.topic,
                    form.instance.number, form.instance.input == 'a')
                form.instance.generated_data = data
                form.save()
                messages.success(request, "The generation has been done succesfully.")
                form = RecordForm()
            except Exception as err:
                messages.error(request, err)

        else:
            messages.warning(request, "There is something wrong, the form is invalid.")
    else:
        form = RecordForm()
    return render(request, "pages/generator.html", {
        'form': form,
        'records': Record.objects.filter(author=request.user).order_by('-pk')
    })


def about(request):
    return render(request, "pages/about.html")
