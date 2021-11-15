from django.db import models

# Create your models here.
class CustomerAccount(models.Model):
    #fields

    first_name = models.CharField(max_length=20, help_text='Enter Customer First Name:')
    last_name = models.CharField(max_length=20, help_text='Enter Customer Last Name')
    phone_number = models.CharField(max_length=6, help_text='Enter Customer Phone Number')
    address = models.CharField(max_length=50, help_text='Enter Customer Address')

    #Metadata
    class Metadata:
        ordering = ['first_name']
    
    #Methods
    def get_absolute_urls(self):
        return reverse('CustomerAccount', args=[str(self.id)])
    
    def __str__(self):
        return self.first_name

class CustomerOrder(models.Model):

    #fields
    item = models.CharField(max_length=25, help_text= 'Enter item:')
    order = models.ManyToManyField(CustomerAccount)

    #MetaData
    class MetaData:
        ordering = ['order']

    #Methods
    def get_absolute_urls(self):
        return reverse('CustomerOrder', args=[str(self.id)])
    
    def __str__(self):
        return self.order

class CustomerOrderItem(models.Model):

    #fields
    item_name = models.CharField(max_length=50)
    order_name = models.ManyToManyField(CustomerOrder)

    #Metadata
    class MetaData:
        ordering = ['item-name']

    #Methods
    def get_absolute_urls(self):
        return reverse('CustomerOrderItem', args=str[(self.id)])
    
    def __str__(self):
        return self.item_name




    
