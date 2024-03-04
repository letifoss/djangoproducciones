from django.urls import path
from . import views

urlpatterns = [
    path('', views.routes),
    path('reseña/', views.reseña),
    path('comment/<int:id>/', views.comment),
    path('planes', views.planes),
    path('plan/<int:id>', views.plan)
]