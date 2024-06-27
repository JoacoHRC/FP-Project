from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

def formularioContacto(request):
    return render (request ,"formularioContacto.html")
def contactar (request):
    if request.method=="POST":
        asunto = request.POST["txtAsunto"]
        mensaje= request.POST["txtMensaje"]+"/ Email" + request.POST["txtEmail"]
        email_desde= settings.EMAIL_HOST_USER
        email_para = ["isaac.martel.b@uni.pe"]
        send_mail(asunto,mensaje,email_desde,email_para,fail_silently=False)
        return render(request , "contactoExitoso.html")
    return render(request , "formularioContacto.html")


def index(request):
    return render(request, "index.html")