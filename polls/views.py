from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render,redirect
import requests
import json


def home(request):
    return render(request, 'home.html')


def search_characters(name):

    url = 'https://rickandmortyapi.com/api/character'
    observable = requests.get(url)  # OJO CON EL REQUEST

    if observable.status_code == 200:
        jsonfin = json.loads(observable.text)
        tupla = tuple(jsonfin['results'])
        try:
            resultado = list(filter(lambda x: x['name'] == name, tupla))[0]

            return (f"id: {resultado['id']}\n"
                    f"Nombre: {resultado['name']}\n "
                    f"Genero: {resultado['gender']}\n")

        except:
            warning = "El personaje ingresado no se ha encontrado"
            return warning



def procesar(request):
    word = request.GET.get('word', '')
    temple = open("C:/Users/Personal/PycharmProjects/djangoProject/templates/results.html")
    template = Template(temple.read())
    temple.close()
    ctx = Context({'result': search_characters(word)})
    doc = template.render(ctx)
    return HttpResponse(doc)


