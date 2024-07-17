from django.urls import path
from .views import*
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('add',TodoAddView.as_view(),name="add"),
    path('list',TodoListView.as_view(),name="list"),
    path('tdel/<int:id>',TododeleteView.as_view(),name="tdelt"),
    path('edit/<int:id>',TodoEditView.as_view(),name="edit")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)