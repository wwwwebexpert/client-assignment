from django.urls import path
from .views import *

urlpatterns = [
				path('add', add),  
			    path('clients',clients),  
			    path('edit/<int:id>', edit),  
			    path('update/<int:id>', update)			
]