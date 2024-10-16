from django.urls import path
from .views import home, contact, services, reserve, logIn, register, add, list, modify, delete, add_service, delete_service, subtract_service, clean_cart, pay
                

#Para subir imagenes 
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('schedule/', reserve, name='reserve'),
    path('pay/', pay, name='pay'),
    path('signin/', logIn, name='login'),
    path('signup/', register, name='register'),
    path('add/', add, name="add"),   
    path('list/', list, name="list"),   
    path('modify/<id>/', modify, name="modify"),   
    path('delete/<id>/', delete, name="delete"),
    path('add/<int:service_id>/', add_service, name="add_service"),
    path('delete/<int:service_id>/', delete_service, name="delete_service"),
    path('substract/<int:service_id>/', subtract_service, name="subtract_service"),
    path('clean/', clean_cart, name="clean_cart"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
