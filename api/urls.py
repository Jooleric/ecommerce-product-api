from django.http import JsonResponse

def api_home(request):
    return JsonResponse({
        "message": "Welcome to the E-commerce Product API 🚀",
        "endpoints": {
            "products": "/api/products/",
            "users": "/api/users/"
        }
    })

urlpatterns = [
    path('', api_home, name='api-home'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('users/', views.UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]
