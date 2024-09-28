from django.shortcuts import render


def photos_add(request):
    return render(request, 'photos/photo-add-page.html')


def photos_edit(request, pk: int):
    return render(request, 'photos/photo-edit-page.html')


def photos_details(request, pk: int):
    return render(request, 'photos/photo-details-page.html')
