from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('signup',signup,name='signup'),
    path('emplogin',emplogin,name='emplogin'),
    path('admlogin',admlogin,name='admlogin'),
    path('adminhome',adminhome,name='adminhome'),
    path('changepassadmin',changepassadmin,name='changepassadmin'),
    path('allemployee',allemployee,name='allemployee'),
    path('deleteemp/<int:pid>',deleteemp,name='deleteemp'),
    path('editprofileadm/<int:pid>',editprofileadm,name='editprofileadm'),
    path('editeducationadm/<int:pid>',editeducationadm,name='editeducationadm'),
    path('editexperienceadm/<int:pid>',editexperienceadm,name='editexperienceadm'),







    path('emplogin',emplogin,name='emplogin'),
    path('emphome',emphome,name='emphome'),
    path('emprofile',emprofile,name='emprofile'),
    path('Logout',Logout,name='Logout'),
    path('myexperience',myexperience,name='myexperience'),
    path('editexperience',editexperience,name='editexperience'),
    path('myeducation',myeducation,name='myeducation'),  
    path('editeducation',editeducation,name='editeducation'),
    path('changepass',changepass,name='changepass'),



]
