from django.urls import path
from . import views
from .views import AddSiteDetails,SerachSiteDetails,SiteDetailView,SiteUpdateView

urlpatterns = [
    path('',views.home,name='routerdetails-home'),
    path('routerdetails/',AddSiteDetails.as_view(),name='Add Router Details'),
    path('routerdetails/search',SerachSiteDetails.as_view(),name='Search Router Details'),
    path('routerdetails/site/<int:pk>/',SiteDetailView.as_view(),name='sitedetails'),
    path('routerdetails/<int:pk>/update/',SiteUpdateView.as_view(),name='site_update'),

]