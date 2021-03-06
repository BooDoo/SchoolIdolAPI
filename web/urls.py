from django.conf.urls import include, patterns, url
from web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^cards[/]+$', views.cards, name='cards'),
    url(r'^card[s]?/(?P<card>\d+)[/]$', views.cards, name='cards'),

    url(r'^create[/]+$', views.create, name='create'),
    url(r'^edit[/]+$', views.edit, name='edit'),
    url(r'^login[/]+$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^setaccountonlogin[/]+$', views.setaccountonlogin, name='setaccountonlogin'),
    url(r'^logout[/]+$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^addaccount[/]+$', views.addaccount, name='addaccount'),
    url(r'^editaccount/(?P<account>\d+)[/]+$', views.editaccount, name='editaccount'),
    url(r'^user[s]?/(?P<username>[\w.@+-]+)[/]+$', views.profile, name='profile'),
    url(r'^users[/]+$', views.users, name='users'),
    url(r'^events[/]+$', views.events, name='events'),
    url(r'^event[s]?/(?P<event>[^/]+)[/]+$', views.event, name='event'),
    url(r'^idols[/]+$', views.idols, name='idols'),
    url(r'^activities[/]+$', views.activities, name='activities'),
    url(r'^twitter[/]+$', views.twitter, name='twitter'),
    url(r'^map[/]+$', views.mapview, name='map'),

    url(r'^ajax/modal/(?P<hash>\w+)[/]+$', views.ajaxmodal, name='ajaxmodal'),
    url(r'^ajax/addcard[/]+$', views.ajaxaddcard, name='ajaxaddcard'),
    url(r'^ajax/editcard/(?P<ownedcard>\d+)[/]+$', views.ajaxeditcard, name='ajaxeditcard'),
    url(r'^ajax/deletecard/(?P<ownedcard>\d+)[/]+$', views.ajaxdeletecard, name='ajaxdeletecard'),
    url(r'^ajax/cards[/]+$', views.ajaxcards, name='ajaxcards'),
    url(r'^ajax/users[/]+$', views.ajaxusers, name='ajaxusers'),
    url(r'^ajax/ownedcards/(?P<account>\d+)/(?P<stored>\w+)[/]+$', views.ajaxownedcards, name='ajaxownedcards'),
    url(r'^ajax/follow/(?P<username>[\w.@+-]+)[/]+$', views.ajaxfollow, name='ajaxfollow'),
    url(r'^ajax/followers/(?P<username>[\w.@+-]+)[/]+$', views.ajaxfollowers, name='ajaxfollowers'),
    url(r'^ajax/following/(?P<username>[\w.@+-]+)[/]+$', views.ajaxfollowing, name='ajaxfollowing'),
    url(r'^ajax/activities[/]+$', views.ajaxactivities, name='ajaxactivities'),
    url(r'^ajax/feed[/]+$', views.ajaxfeed, name='ajaxfeed'),
    url(r'^ajax/eventparticipations/(?P<account>\d+)[/]+$', views.ajaxeventparticipations, name='ajaxeventparticipations'),

    url(r'^avatar/twitter/(?P<username>[\w.@+-]+)[/]+$', views.avatar_twitter, name='avatar_twitter'),
    url(r'^avatar/facebook/(?P<username>[\w.@+-]+)[/]+$', views.avatar_facebook, name='avatar_facebook'),

    url(r'^i18n/', include('django.conf.urls.i18n')),
)
