from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wsm',views.WS,name='wsm'),
    path('entropy',views.entropyMethod,name='entropy'),
    path('topsis',views.topsisMethod,name='topsis'),
    path('waspass',views.waspassMethod,name='waspass'),
    path('promethee',views.prometheeMethod,name='promethee'),
    path('charts',views.charts,name='charts')

]