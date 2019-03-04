from django.urls import path

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
    )

app_name='stock'

urlpatterns = [
    path('', Home.as_view(), name='post-list'),
    path('customer/', CustomerList.as_view(), name='customer-list'),
    path('create/', ItemCreateView.as_view(), name='post-create'),
    path('create-brand/', BrandCreateView.as_view(), name='brand-create'),
    path('create-category/', CategoryCreateView.as_view(), name='category-create'),
    path('create-office/', OfficeCreateView.as_view(), name='office-create'),
    path('create-course/', CourseCreateView.as_view(), name='course-create'),
    path('create-customer/', CustomerCreateView.as_view(), name='course-customer'),
    path('release/', ReleaseCreateView.as_view(), name='release'),
    path('item/<str:number>', ItemDetailView.as_view(), name='item-detail'),
    path('customer/<str:id_number>', CustomerDetailView.as_view(), name='customer-detail'),
    # path('course', Courselist, name='course-list'),e
    # path('choice', choice_list, name='choice-list'),
    # path('personal-information', personal_information_list, name='personal-information-list'),
    # path('question', question_list, name='question-list'),
    # path('course/<str:pk>', course_detail, name='course-detail'),
    # path('choice/<str:pk>', choice_detail, name='choice-detail'),
    # path('personal-information/<str:pk>', personal_information_detail, name='personal-information-detail'),
    # path('question/<str:pk>', question_detail, name='question-detail')
]