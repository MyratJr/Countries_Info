from django.contrib import admin
from .models import Places, signup, News, PropertyImage, SlideImage, HomeSlide

# ADMIN PAROL{MYRAT}{MYRAT}

admin.site.register(signup)
admin.site.register(News)




class PropertyImageInline(admin.StackedInline):
    model = PropertyImage

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline ]

    class Meta:
        model=Places

admin.site.register(Places,PropertyAdmin)
class PropertyImageInline(admin.ModelAdmin):
    pass

class ici(admin.StackedInline):
    model = SlideImage

class HomeAdmin(admin.ModelAdmin):
    inlines = [ici]
    class Meta:
        model=HomeSlide
admin.site.register(HomeSlide,HomeAdmin)
class ici(admin.ModelAdmin):
    pass


