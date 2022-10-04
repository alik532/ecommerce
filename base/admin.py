from django.contrib import admin
from base.models import Categorie, Product, Cart, Profile, Comment

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Categorie)
admin.site.register(Profile)
admin.site.register(Comment)