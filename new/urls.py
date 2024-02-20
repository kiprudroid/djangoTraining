from django.contrib import admin
from django.urls import path
from new import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about, name='about'),
    path('post/',views.post, name='post'),
    path('form/',views.form )

]
