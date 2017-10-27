from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^main$', views.main),                                                         # renders main  
    url(r'^logout$', views.logout),                                                         # renders main  
    url(r'^render_item_build$', views.render_item_build),                               # renders page to build item 
    url(r'^add_item$', views.add_item),                                                 # creates item, in this stage it should only be linked to one key "Creator" 
    url(r'^delete_item/(?P<item_id>\d+)$', views.delete_item),                                                 # creates item, in this stage it should only be linked to one key "Creator" 
    url(r'^display_item/(?P<item_id>\d+)$', views.display_item),                                                 # creates item, in this stage it should only be linked to one key "Creator" 
    url(r'^add_to_wishlist/(?P<item_id>\d+)$', views.add_to_wishlist),                                                 # creates item, in this stage it should only be linked to one key "Creator" 
]