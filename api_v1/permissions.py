from rest_framework import permissions

class IsVeterinarianOrReadOnly(permissions.BasePermission):
    """
    Разрешение для медицинских карт:
    - Читать и создавать могут только авторизованные пользователи.
    - Изменять и удалять запись может только тот врач, который её создал.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешаем изменение только автору записи (врачу) или суперпользователю
        if request.user.is_superuser:
            return True
        return obj.veterinarian == request.user