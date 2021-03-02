from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from candy.views import detail, home
from django.contrib.auth.models import User
import pytest

@pytest.mark.django_db
class TestViews:

    def test_detail_views(self):
       
        path = reverse('detail',kwargs={'name':'karmelek'})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = detail(request,'karmelek')
        assert response.status_code == 200 

    def test_detail_views(self):
       
        path = reverse('detail',kwargs={'name':111})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = detail(request,1111)
        assert response.status_code == 200

    def test_home(self):
        path = reverse('home')
        request = RequestFactory().get(path)
        response = home(request)
        assert response.status_code == 200 

