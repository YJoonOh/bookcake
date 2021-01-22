from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),  
    path('home/', views.selectCategory, name="home"),
    path('result/<int:cat_id>', views.result, name=""),
    # path('create/', views.yourTip, name="create"),
    # path('canshares/', views.canShare, name="canshare"),
    # path('cannotshares/', views.cannotShare, name="cannotshare")
]
