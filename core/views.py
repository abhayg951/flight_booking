from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from .forms import UserLoginForm
from .models import Flight, Booking, User, locations

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        postal_code = request.POST['postal_code']
        address = request.POST['address']
        city = request.POST['city']
        password = request.POST['password']
        password2 = request.POST['confirm_password']
        print(request.POST)
        

        if not name or not email or not postal_code or not address or not city or not password or not password:
            messages.error(request, "All fields are required.")
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address.")
        
        if password!=password2:
            messages.error(request, "Passwords do not match.")
        
        if len(postal_code) > 6 or not postal_code.isdigit():
            messages.success(request, "Invalid postal code.")
        
        try:
            user = User.objects.create_user(
                name = name,
                username=email,
                email=email,
                address=address,
                city=city,
                postal_code = postal_code,
                password = password
            )
            user.save()
            messages.success(request, "User created successfully.")
            return redirect('login')
        except Exception as e:
            messages.error(request, "An error occurred. Please try again.")
            return redirect('signup')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'User logged out.')
    return redirect('login')

@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def search_flights(request):
    flights = None
    is_avail = True
    l = locations.objects.all()
    if request.method == 'GET' and 'date' in request.GET and 'time' in request.GET and 'source' in request.GET and 'destination' in request.GET:
        date = request.GET['date']
        time = request.GET['time']
        source = request.GET['source']
        destination = request.GET['destination']
        flights = Flight.objects.filter(departure_time__date=date, departure_time__time=time, source=source, destination=destination)
        avail_seats = flights.values("available_seats").get()['available_seats']
        if avail_seats <= 0:
            is_avail = False
    return render(request, 'search_flights.html', {'flights': flights, 'locations': l, 'is_avail': is_avail})

@login_required
def book_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    if flight.available_seats > 0:
        Booking.objects.create(user=request.user, flight=flight)
        flight.available_seats -= 1
        flight.save()
        messages.success(request, 'Flight booked successfully!')
    else:
        messages.error(request, 'No available seats!')
    return redirect('my_bookings')

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})
