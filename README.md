**Rent Near Website & Application**

*Overview*

Imagine a motorcycle taxi driver, working tirelessly through busy city streets, dreaming of a comfortable and affordable place to live near their workplace. They need a dormitory with complete furniture—beds, tables, air conditioning—at a price that fits their budget. Yet, their search is met with frustration: available dorms are either too expensive or lack the essential amenities they need. Inspired by this struggle, we created Rent Near Application, a web application designed to help motorcycle taxi drivers, students, and people of all ages and backgrounds find affordable, well-furnished dormitories close to their desired locations. Our platform simplifies the search for quality housing, ensuring everyone can find a place that feels like home without breaking the bank.

===

*Features*

- User Roles:
1. Tenants: Browse rooms, make bookings, leave reviews, and specify preferences.
2. Landlords: Manage room listings, including price, amenities, location, and images.
- Room Management: Create and edit room listings with details like dorm name, room name, price, location, and amenities (e.g., beds, air conditioners, tables). Supports image uploads for room visualization.
- Booking System: Book rooms with check-in/check-out dates, track booking status (pending, confirmed, canceled), and manage room availability automatically.
- Reviews: Tenants can rate rooms (1-5 stars) and provide feedback on comfort and cleanliness.
- Custom User Authentication: Extends Django's AbstractUser with roles (Tenant or Landlord) and additional fields like phone number.

===

*Technologies Used*

- Backend: Django 4.x, Python 3.13
- Database: SQLite (default, configurable to others like PostgreSQL)
- Frontend: Django templates (extendable with static files like CSS, JavaScript, and images)
- Static Files: Supports images (e.g., room images, logo.svg) and other assets
- Image Processing: Pillow for handling image uploads

===

*Installation*

- Prerequisites
 - Python 3.13 or higher
 - pip (Python package manager)
 - Virtualenv (recommended)
 - Git
 - Pillow (for image uploads in the Room model)
- Setup Instructions

1. Clone the Repository:

git clone https://github.com/lynylany/dsi202_2025.git
cd myproject

2. Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:

pip install -r requirements.txt

Note: Ensure requirements.txt includes:

django>=4.0
python-dateutil>=2.8
pillow>=9.0


4. Apply Migrations:

python manage.py makemigrations
python manage.py migrate


5. Create a Superuser (for admin access):

python manage.py createsuperuser


6. Collect Static Files (if needed):

python manage.py collectstatic


7. Run the Development Server:

python manage.py runserver

Access the application at http://localhost:8000.

===

*Project Structure*

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

===

*Usage*

- Admin Panel: Access at /admin to manage users, rooms, bookings, and reviews.
- Tenant Features:
 - Browse available rooms with details and images.
 - Book a room by providing check-in/check-out dates or guest details (full name, phone, email).
 - Leave reviews with ratings and comments on comfort and cleanliness.
- Landlord Features:
 - Add/edit room listings with details like price, amenities, location, and upload images (e.g., room photos).
 - View and manage bookings, including confirming or canceling.
- Static Files: Place images (e.g., logo.svg, room images) in myapp/static/images/ and reference them in templates using {% load static %} and {% static 'images/logo.svg' %}.

===

*Database Models*

- CustomUser: Extends Django's AbstractUser with phone and role (Tenant or Landlord).
- Tenant: Stores tenant-specific data like budget and preferences.
- Landlord: Stores landlord details like dorm_name, address, and bank information.
- Room: Represents a room with details like dorm_name, room_name, price, location, and amenities (e.g., bed_count, aircon_count). Supports image uploads.
- Booking: Manages room bookings with status and date validation.
- Review: Allows tenants to rate and comment on rooms.

===

*Troubleshooting*

1. ImportError for CustomSignupForm:
- Check myapp/allauth_forms.py for CustomSignupForm. Example:
  
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        return user

- If not used, remove the import from myapp/views.py:
Remove: from myapp.allauth_forms import CustomSignupForm

2. Migration Issues:
   
- If prompted about renaming fields (e.g., room.name to room.dorm_name), answer y if the field was renamed, or N if it's a new field.
- For non-nullable fields without defaults (e.g., dorm_name, room_name), ensure default is set in models.py (e.g., default='Unknown').
  
3. Static Files: Ensure STATICFILES_DIRS is configured in settings.py:

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

Run collectstatic for production.

4. Image Uploads: Install Pillow (pip install pillow) foe ImageField in the Room model.

===

*Contributing*

1. Fork the repository.
2. Create a feature branch (git checkout -b feature/YourFeature).
3. Commit changes (git commit -m 'Add YourFeature').
4. Push to the branch (git push origin feature/YourFeature).
5. Open a pull request.

===

*License*

This project is licensed under the MIT License.

===

*Contact*

For issues or suggestions, please open an issue on the repository (https://github.com/lynylany/dsi202_2025) or contact the project maintainer.
