from django.shortcuts import render
import requests
from rest_framework.views import APIView
import logging

logger = logging.getLogger(__name__)

class SayHello(APIView):
    
    def get(self,request):
        try:
            logger.info('Calling httpbin')
            result = requests.get('https://httpbin.org/delay/2')
            logger.info('Recive httpbin response')
            data = result.json() 
            return render(request, 'hello.html', {'name': data}) 
        except requests.ConnectionError:
            logger.critical('Httpbin is offline')

    


 

