# -*- coding: utf-8 -*-
from django.conf.urls import url
from dbscan_w2v import views
urlpatterns = [
	url(r'^dbsc$', views.dbsc),
]