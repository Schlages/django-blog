from django.contrib import admin

from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):  # or admin.StackedInline
    model = (
        Category.posts.through
    )  # Use the through table for the ManyToMany relationship
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


# Customize the Category admin
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
