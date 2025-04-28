from django.contrib import admin
from TestModel.models import Test, Contact, Tag, Book, test2, test3


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


class temp(admin.ModelAdmin):
    fields = ('title', 'price', 'publish', 'pub_date')
    # Book.objects.create(title='sex')
    # Test.objects.create(title='sex')


class dm1(admin.ModelAdmin):
    fields = ('t1', 't2')


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag, test2, Book, test3])

