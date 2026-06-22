from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.home,              name='home'),
    path('listings/',               views.listing_list,      name='listing_list'),
    path('listings/<int:pk>/',      views.listing_detail,    name='listing_detail'),
    path('listings/new/',           views.listing_create,    name='listing_create'),
    path('listings/<int:pk>/edit/', views.listing_edit,      name='listing_edit'),
    path('listings/<int:pk>/delete/', views.listing_delete,  name='listing_delete'),
    path('my-listings/',            views.my_listings,       name='my_listings'),
    path('my-messages/',            views.my_messages,       name='my_messages'),
]
