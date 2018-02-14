from django import forms
from .models import Order, Item, Item_Category

# store = models.CharField(max_length=100)
# extra = models.TextField()
# coffee_bean = models.IntegerField(default=0)
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
