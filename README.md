# Flight Ticket Booking Web Application

This is a web application for booking flight tickets, developed using Django, HTML, CSS, JavaScript, and Bootstrap. The application supports two types of users: regular users and admins, each with their own set of functionalities.

## Table of Contents

- [Features](#features)
  - [User Features](#user-features)
  - [Admin Features](#admin-features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)


## Features

### User Features

- **Login:** Users can log in to their accounts.
- **Sign Up:** New users can create an account.
- **Search Flights:** Users can search for flights based on date and time.
- **Book Tickets:** Users can book tickets for flights, with a default seat count of 60 per flight.
- **My Bookings:** Users can view a list of all their bookings.
- **Logout:** Users can log out of their accounts.

### Admin Features

- **Login:** Admins have a separate login page.
- **Add Flights:** Admins can add new flights to the system.
- **Remove Flights:** Admins can remove existing flights.
- **View Bookings:** Admins can view all bookings based on flight number and time.
- **Django Admin Dashboard:** Admin functionalities are managed through the Django admin dashboard.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/abhayg951/flight_booking.git
   cd flight-booking-app

2. Create and activate a virtual environment:
    
    #### Windows
    python -m venv venv
    venv\Scripts\activate

    #### Linux and macOS
    python3 -m venv venv
    source venv/bin/activate

3. Install the required packages:

    pip install -r requirements.txt

4. Apply the migrations:

    python manage.py migrate

5. Create a superuser for admin access:

    python manage.py createsuperuser

6. Run the development server:

    python manage.py runserver

7. Usage

    Open your web browser and go to http://127.0.0.1:8000/.
    For admin functionalities, log in with the admin credentials on the Django admin dashboard at http://127.0.0.1:8000/admin:
    For user functionalities, sign up for a new user account or log in with an existing user account.

8. Technologies Used

    Django
    HTML
    Bootstrap
