from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import requests
import os
import time

def test_get(request):
    print('Request inbound!')
    return Response('Get works with Pyramid!')


def test_post(request):
    print('Request inbound!')
    return Response('Docker works with Pyramid!')


def test_httpApp(request):
    print ('Request inbound!')
    requests.get('http://javaapp:8080/RR_ServApp_02/helloGet')
    #time.sleep(3)
    return Response('Docker works with Pyramid!')

def test_pyApp(request):
    requests.get("http://flaskapp:6000/pygetter")
    print('Request outbound!')
    return Response('Docker works with Pyramid!')

def test_error(request):
    print('error outbound!')
    if request.method == "POST":
        response.status_int=403
    return Response('Docker works with Pyramid!', 403)

def test_slow(request):
    print('slow outbound!')
    time.sleep(3)
    return Response('slow call works with Pyramid!')

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('getter', '/getter')
    config.add_view(test_get, route_name='getter')

    config.add_route('poster', '/poster')
    config.add_view(test_post, route_name='poster')

    config.add_route('httpgetter', '/httpgetter')
    config.add_view(test_httpApp, route_name='httpgetter')

    config.add_route('pypgetter', '/pypgetter')
    config.add_view(test_pyApp, route_name='pypgetter')

    config.add_route('error', '/error')
    config.add_view(test_error, route_name='error')

    config.add_route('slow', '/slow')
    config.add_view(test_slow, route_name='slow')

    return config.make_wsgi_app()
