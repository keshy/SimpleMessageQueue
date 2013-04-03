# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from Mongo.pyMongoConnection import enqueue

@require_POST
@csrf_exempt
def update(request):
    ''' TODO: not handling csrf protection for now'''
    msg = request.POST['msg']
    print(msg)
    # import mongodb and add this to the db which is treated as a queue
    docId = enqueue(msg, 'log', 'messages')
    print(docId)
    return HttpResponse("Hello, world. You're at the producer with msg inserted into mongo with ID:." + docId.__str__())


    
    
    
