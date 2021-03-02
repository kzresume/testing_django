from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:

    def test_avaible(self):
        product = mixer.blend('candy.Candy') 
        assert product.avaiable == True