from django.shortcuts import render


def main(request):

    return render(
        request,
        'main/mainpage.html',
    )

# Create your views here.
