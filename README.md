Dormitory Booking System
Overview
Imagine a motorcycle taxi driver, working tirelessly through busy city streets, dreaming of a comfortable and affordable place to live near their workplace. They need a dormitory with complete furniture—beds, tables, air conditioning—at a price that fits their budget. Yet, their search is met with frustration: available dorms are either too expensive or lack the essential amenities they need. Inspired by this struggle, we created the Dormitory Booking System, a web application designed to help motorcycle taxi drivers, students, and people of all ages and backgrounds find affordable, well-furnished dormitories close to their desired locations. Our platform simplifies the search for quality housing, ensuring everyone can find a place that feels like home without breaking the bank.
Features

User Roles:
Tenants: Browse rooms, make bookings, and leave reviews.
Landlords: Manage room listings, including details like price, amenities, and availability.


Room Management: Rooms are associated with landlords, with details such as name, price, location, and amenities (e.g., bed, aircon, table counts).
Booking System: Supports booking with check-in/check-out dates, status tracking (pending, confirmed, canceled), and availability management.
Reviews: Tenants can rate and comment on rooms based on comfort and cleanliness.
Custom User Authentication: Extends Django's AbstractUser with roles and additional fields like phone number.

Technologies Used

Backend: Django 4.x, Python 3.13
Database: SQLite (default, configurable to others like PostgreSQL)
Frontend: Django templates (extendable with static files like CSS, JavaScript, and images)
Static Files: Supports images (e.g., room images, logo.svg)

Installation
Prerequisites

Python 3.13 or higher
pip (Python package manager)
Virtualenv (recommended)
Git

Setup Instructions

Clone the Repository:
git clone <repository-url>
cd myproject


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

Note: Ensure requirements.txt includes django, python-dateutil, and other necessary packages. Example:
django>=4.0
python-dateutil>=2.8
pillow>=9.0


Apply Migrations:
python manage.py makemigrations
python manage.py migrate


Create a Superuser (for admin access):
python manage.py createsuperuser


Collect Static Files (if needed):
python manage.py collectstatic


Run the Development Server:
python manage.py runserver

Access the application at http://localhost:8000.


Project Structure
myproject/
├── myapp/
│   ├── migrations/
│   ├── static/
│   │   └── images/
│   │       └── logo.svg
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── allauth_forms.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
├── manage.py
└── README.md

Usage

Admin Panel: Access at /admin to manage users, rooms, bookings, and reviews.
Tenant Features:
Browse available rooms.
Book a room by providing check-in/check-out dates or guest details.
Leave reviews for booked rooms.


Landlord Features:
Add/edit room listings with details like price, amenities, and images.
View and manage bookings.


Static Files: Place images (e.g., logo.svg) in myapp/static/images/ and reference them in templates using {% static 'images/logo.svg' %}.

Database Models

CustomUser: Extends Django's AbstractUser with phone and role (Tenant or Landlord).
Tenant: Stores tenant-specific data like budget and preferences.
Landlord: Stores landlord details like dorm name, address, and bank information.
Room: Represents a room with details like dorm_name, room_name, price, and amenities.
Booking: Manages room bookings with status and date validation.
Review: Allows tenants to rate and comment on rooms.

Troubleshooting

ImportError for CustomSignupForm:
Ensure myapp/allauth_forms.py contains CustomSignupForm or remove the import from views.py.


Migration Issues:
If prompted about renaming fields (e.g., room.name to room.dorm_name), answer y if applicable.
For non-nullable fields without defaults, add default in models.py (e.g., default='Unknown').


Static Files: Ensure STATICFILES_DIRS is configured in settings.py and run collectstatic for production.

Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit changes (git commit -m 'Add YourFeature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.

License
This project is licensed under the MIT License.
Contact
For issues or suggestions, please open an issue on the repository or contact the project maintainer.
