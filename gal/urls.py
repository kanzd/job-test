from django.urls import path
from . import views

app_name="gal"
urlpatterns = [
    path("",views.rendere),
    path("upload/",views.getUpload,name="upload"),
    path("images/<int:page>",views.base,name="images"),
    path("status/",views.upload,name="status"),
    path("search/<slug:tag>/<int:page>",views.search,name="search")
   
]