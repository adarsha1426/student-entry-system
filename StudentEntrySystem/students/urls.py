from django.urls import path,include

from  . import views

urlpatterns = [
    path('add/',views.add_student,name='add_student'),
    path('update/<int:student_id>/',views.update_student,name='update_student'),
    path('view/',views.view_student,name='view_student'),
    path('delete/<int:student_id>',views.delete_student,name='delete_student'),

    #for django-rest-framework api view
    path('api/student/',views.student_list,name='add'),
    path('api/student_update/<int:id>/',views.student_update_api_view,name='update'),
    path('api/student_delete/<int:id>/',views.student_delete_api_view,name="delete"),
]
