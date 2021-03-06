from django.conf.urls import include,patterns,url

urlpatterns = patterns('auth_app.views',
    url(r'^$', 'landingPage', name = 'landing_page'),
    url(r'^sign-up/$', 'SignUp', name = 'SignUp'),
    #url(r'^sign-up/signupmail/$','signupmail',name='signupmail'),
    url(r'^sign-in/$', 'SignIn', name = 'sign_in'),
    url(r'^dashboard/$','dashboard',name='dashboard'),
    url(r'^myprofile/$','myprofile',name='myprofile'),
    url(r'^auth/BorrowersList', 'BorrowersList',name='BorrowersList'),
    url(r'^list/$', 'list', name='list'),
    url(r'^sign-out/$', 'SignOut', name = 'sign_out'),
    url(r'^auth/$','auth_view',name='auth'),
    url(r'^auth/loggedin', 'loggedin',name='loggedin'),
    url(r'^single/(?P<postId>\d+)/$', 'single', name='single'),
    url(r'^invest/(?P<post>\d+)$', 'Invest', name='Invest'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^sendMessage/$', 'sendMessage', name='sendMessage'),
  

    
)
