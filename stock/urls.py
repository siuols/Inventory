from django.urls import path

from stock.views import ItemCreateView,Home

app_name='stock'

urlpatterns = [
    path('', Home.as_view(), name='post-list'),
    path('create/', ItemCreateView.as_view(), name='post-create'),
    # path('course', Courselist, name='course-list'),e
    # path('choice', choice_list, name='choice-list'),
    # path('personal-information', personal_information_list, name='personal-information-list'),
    # path('question', question_list, name='question-list'),
    # path('course/<str:pk>', course_detail, name='course-detail'),
    # path('choice/<str:pk>', choice_detail, name='choice-detail'),
    # path('personal-information/<str:pk>', personal_information_detail, name='personal-information-detail'),
    # path('question/<str:pk>', question_detail, name='question-detail')
]