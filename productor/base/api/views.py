from django.http import JsonResponse
from ..models import Reseña, Planes


def routes(request):
    routes = [
        'GET /api/reseña',
        'GET /api/comment/:id'
    ]
    return JsonResponse(routes, safe=False)

def reseña(request):
    reseñas = Reseña.objects.all()
    reseña_dict = []
    for p in reseñas:
        reseña_dict.append({
            'name': p.first_name,
            'comment': p.comment,
            'id': p.id
        })
    return JsonResponse(reseña_dict, safe=False)

def comment(request, id):
        comment = Reseña.objects.get(id=id)
        comment_dict = {
            'name': comment.first_name,
            'comment': comment.comment,
            'id': comment.id
        }
        return JsonResponse(comment_dict, safe=False)


def planes(request):
    planes=Planes.objects.all()
    planes_dict= []
    for p in planes:
        planes_dict.append({
            'title':p.title,
            'info': p.info,
            'price': p.price,
            'id': p.id
        })
    return JsonResponse(planes_dict, safe=False)

def plan(request, id):
        plan = Planes.objects.get(id=id)
        plan_dict = {
            'title': plan.title,
            'info': plan.info,
            'price': plan.price,
            'id': plan.id
        }
        return JsonResponse(plan_dict, safe=False)
