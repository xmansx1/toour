from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Tour, Booking  # استيراد الموديلات
from .forms import BookingForm  # استيراد نموذج الحجز
from .models import Tour, Booking
from .forms import BookingForm, TourGuideRegistrationForm, TourForm

def home(request):
    """
    الصفحة الرئيسية، تعرض قائمة بالجولات السياحية المتاحة.
    """
    tours = Tour.objects.all()
    return render(request, 'tours/home.html', {'tours': tours})

def tour_list(request):
    """
    عرض قائمة الجولات السياحية.
    """
    tours = Tour.objects.all()
    return render(request, 'tours/tour_list.html', {'tours': tours})

def tour_detail(request, tour_id):
    """
    عرض تفاصيل جولة سياحية معينة.
    """
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tours/tour_detail.html', {'tour': tour})

def book_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)  # احصل على الجولة بناءً على المعرف tour_id
    print(vars(tour))

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour
            booking.save()
            messages.success(request, f"تم استلام طلب حجزك لـ {tour.title} وسنتواصل معك قريبًا! ✅")
            return redirect('book_tour', tour_id=tour.id)
            return redirect('home')  # أو صفحة التأكيد
        
    
    else:
        form = BookingForm()

    return render(request, 'tours/book_tour.html', {'form': form, 'tour': tour})

def register_tour_guide(request):
    """
    تسجيل مرشد سياحي جديد.
    """
    if request.method == "POST":
        form = TourGuideRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم التسجيل كمرشد سياحي بنجاح!")
            return redirect('home')  # توجيه المستخدم إلى الصفحة الرئيسية بعد التسجيل
    else:
        form = TourGuideRegistrationForm()
    
    return render(request, 'tours/register_tour_guide.html', {'form': form})

def add_tour(request):
    """
    إضافة جولة سياحية جديدة.
    """
    if request.method == "POST":
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "تمت إضافة الجولة السياحية بنجاح! ✅")
            return redirect('tour_list')  # تأكد أن `tour_list` موجود في `urls.py`
    else:
        form = TourForm()
    
    return render(request, 'tours/add_tour.html', {'form': form})
