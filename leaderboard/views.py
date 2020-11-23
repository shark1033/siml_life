from django.http import HttpResponse
from .models import Leaders


def index(request):

    #response = "Super secret exchange protocol v1 \r\n--Start of data transmission: \r\n"
    #for i in Leaders.objects.all():
    #    response += " id: "+ str(i.id) + " player_name: " + str(i.player_name) + " age: " +str(i.age) + " money: " + str(i.money)+ "max_health: " +str(i.max_health)+" friends_alive: " +str(i.friends_alive)+ "\r\n"

    #return HttpResponse(response, content_type='text/plain; charset=utf-8')
    
    return HttpResponse("Leoniddick is better then Vladickson")