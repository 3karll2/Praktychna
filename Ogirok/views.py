from django.http import HttpResponse

def index(request):
    return HttpResponse("Це додаток Ogirok")
