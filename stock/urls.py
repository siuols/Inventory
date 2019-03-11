from django.urls import path

from . import views

from .views import (
        BrandCreateView,
        CategoryCreateView,
        CourseCreateView,
        CustomerCreateView,
        CustomerList,
        CustomerDetailView,
        ItemCreateView,
        Home,
        OfficeCreateView,
        ItemDetailView,
        ReleaseCreateView,
        RecieveCreateView,
        item_edit,
        Pdf,
        PdfRelease,       
        PdfReleaseDaily,
        PdfReleaseWeekly,
        PdfReleaseMonthly,

        PdfRecieve,
        PdfReceiveDaily,
        PdfReceiveWeekly,
        PdfReceiveMonthly
        
    )

app_name='stock'

urlpatterns = [
    path('', Home.as_view(), name='post-list'),
    path('customer/', CustomerList.as_view(), name='customer-list'),
    path('customer/<str:id_number>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('item/<str:number>/', views.item_edit, name='item-edit'),
    path('item/detail/<str:number>/', ItemDetailView.as_view(), name='item-detail'),

    path('recieve/', RecieveCreateView.as_view(), name='recieve-create'),
    path('create/', ItemCreateView.as_view(), name='post-create'),
    path('create-brand/', BrandCreateView.as_view(), name='brand-create'),
    path('create-category/', CategoryCreateView.as_view(), name='category-create'),
    path('create-office/', OfficeCreateView.as_view(), name='office-create'),
    path('create-course/', CourseCreateView.as_view(), name='course-create'),
    path('create-customer/', CustomerCreateView.as_view(), name='course-customer'),
    path('release/', ReleaseCreateView.as_view(), name='release'),
    path('report/', Pdf.as_view(), name='pdf'),
    path('report/recieve', PdfRecieve.as_view(), name='pdf-recieve'),
    path('report/release', PdfRelease.as_view(), name='pdf-release'),

    path('report/release-daily', PdfReleaseDaily.as_view(), name='pdf-release-daily'),
    path('report/release-weekly', PdfReleaseWeekly.as_view(), name='pdf-release-weekly'),
    path('report/release-monthly', PdfReleaseMonthly.as_view(), name='pdf-release-monthly'),

    path('report/receive-daily', PdfReceiveDaily.as_view(), name='pdf-receive-daily'),
    path('report/receive-weekly', PdfReceiveWeekly.as_view(), name='pdf-receive-weekly'),
    path('report/receive-monthly', PdfReceiveMonthly.as_view(), name='pdf-receive-monthly'),
]