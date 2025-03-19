from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Tour, Booking

# نموذج تسجيل المرشد السياحي
class TourGuideRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

# نموذج حجز جولة سياحية
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('tour', 'number_of_people')  # ✅ متوافق الآن مع models.py
        num_people = forms.IntegerField(label="عدد الأشخاص", min_value=1, initial=1)

    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone_number', 'num_people']

# نموذج إضافة وتعديل الجولات السياحية
class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('title', 'description', 'price', 'date', 'time', 'image', 'tour_guide', 'location')  # ✅ الحقول متطابقة مع models.py
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # ✅ تخصيص عرض الحقل
            'time': forms.TimeInput(attrs={'type': 'time'}),  # ✅ تخصيص عرض الحقل
        }