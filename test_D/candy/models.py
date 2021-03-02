from django.db import models
from django.urls import reverse


# Model Djaneiro
class Candy(models.Model):
    """Model definition for Candy."""
    name = models.CharField(max_length=50, unique = True) #mchar 
    color = models.CharField(max_length=50) #mchar
    quantity = models.PositiveIntegerField()



    class Meta:
        """Meta definition for Candy."""
        verbose_name = 'Candy'
        verbose_name_plural = 'Candies'

    def __str__(self):
        """Unicode representation of Candy."""
        return self.name

    def save(self):
        super(Candy,self).save()
        print("OK done")

    def get_absolute_url(self):
        """Return absolute url for Candy."""
        return reverse('detail',args=[self.name])
    
    @property
    def avaiable(self):
        if self.quantity > 0:
            return True
        else:
            return False

    # TODO: Define custom methods here
