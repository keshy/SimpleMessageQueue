# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from Mongo.pyMongoConnection import dequeue

@require_GET
def consume(request):
    # msg = dequeue('log', 'messages')
    # while 1:
    print(dequeue('log', 'messages').__len__())
    return HttpResponse("Welcome consumer! : " + 'Complete')
