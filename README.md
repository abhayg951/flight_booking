# Flight Ticket Booking Web Application

This is a web application for booking flight tickets, developed using Django, HTML, CSS, JavaScript, and Bootstrap. The application supports two types of users: regular users and admins, each with their own set of functionalities.

## Table of Contents

- [Features](#features)
  - [User Features](#user-features)
  - [Admin Features](#admin-features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [License](#license)

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
    ### Windows
   ```sh
        python -m venv venv
        venv\Scripts\activate
