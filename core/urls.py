from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search-flights/', views.search_flights, name='search_flights'),
    path('book-flight/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]
