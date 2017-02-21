# -*- coding: utf-8 -*-
from django.conf.urls import url
from JiebaApi import views
urlpatterns = [
	url(r'^jiebacut$', views.jiebacut),
	url(r'^jiebapos$', views.jiebapos),
]