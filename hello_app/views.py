from django.http import HttpResponse


class View:
    @staticmethod
    def hello(request):
        return HttpResponse("Hello, Danylo!")