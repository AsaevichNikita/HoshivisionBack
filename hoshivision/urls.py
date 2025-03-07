from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Настройка Swagger документации
schema_view = get_schema_view(
    openapi.Info(
        title="Hoshivision API",  # Замените на название вашего API
        default_version='v1',
        description="API documentation for Hoshivision",  # Описание вашего API
        terms_of_service="https://www.google.com/policies/terms/",  # Условия использования
        contact=openapi.Contact(email="contact@hoshivision.local"),  # Контактный email
        license=openapi.License(name="BSD License"),  # Лицензия
    ),
    public=True,  # Документация доступна всем
    permission_classes=(permissions.AllowAny,),  # Разрешить доступ без аутентификации
)

urlpatterns = [
    # Документация Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Документация ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Основные маршруты
    path('game/', include('games.urls')),  # Маршруты для игр
    path('analysis/', include('analysis.urls')),  # Маршруты для анализа
    path('admin/', admin.site.urls),  # Админка Django
    path('profile/', include('user.urls')),  # Маршруты для профилей пользователей
]

