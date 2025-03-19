from django.contrib import admin
from .models import Tour, TourImage, Booking, CustomUser
from django.contrib.auth.admin import UserAdmin

class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1  # يسمح بإضافة صور إضافية عند إنشاء جولة جديدة

class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'date', 'time', 'guide_name')
    search_fields = ('title', 'guide_name')
    inlines = [TourImageInline]
    list_filter = ('date', 'price')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'tour', 'num_people', 'created_at')
    search_fields = ('full_name', 'tour__title')
    list_filter = ('created_at',)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_tour_guide',)}),
    )

admin.site.register(Tour, TourAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TourImage)

# إعدادات لوحة التحكم
admin.site.site_header = "لوحة تحكم الرحلات السياحية"
admin.site.site_title = "إدارة الموقع"
admin.site.index_title = "مرحبًا بك في لوحة الإدارة"
