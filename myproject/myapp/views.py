from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tenant, Landlord, Room, Review, Booking, Admin
from django.db.models import Q  # For complex queries

# Home Page (FBV)
def home(request):
    featured_rooms = Room.objects.filter(is_featured=True, available=True)[:8]  # เอา 8 ห้อง
    return render(request, 'home.html', {'featured_rooms': featured_rooms})

def search_results(request):
    query = request.GET.get('q')
    # ดึงข้อมูลจาก model ตาม query
    return render(request, 'search_results.html', {'query': query})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'room': room})