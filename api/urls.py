from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Fubrique API",
      default_version='v1',
      description="Test API",
      terms_of_service="-",
      contact=openapi.Contact(email="admin@ad.min"),
      license=openapi.License(name="-"),
   ),
   public=True,

   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/surveys/modify/<int:survey_id>', views.api_survey_modify),
    path('api/surveys/<int:survey_id>', views.api_survey_detail),
    path('api/questions/<int:question_id>', views.api_question_detail),
    path('api/questions/create/', views.api_questions_create),
    path('api/questions/', views.api_questions),
    path('api/answers/<int:question_id>', views.api_answer_detail),
    path('api/answers/create/', views.api_answers_create),
    path('api/answers/', views.api_answers),
    path('api/surveys/create/', views.api_surveys_create),
    path('api/surveys/', views.api_surveys),
    path('api/user_choice/<int:user_id>', views.api_user_answers),

]
