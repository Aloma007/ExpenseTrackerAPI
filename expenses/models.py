from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    class Category(models.TextChoices):
        GROCERIES = 'Groceries', 'Groceries'
        LEISURE = 'Leisure', 'Leisure'
        ELECTRONICS = 'Electronics', 'Electronics'
        UTILITIES = 'Utilities', 'Utilities'
        CLOTHING = 'Clothing', 'Clothing'
        HEALTH = 'Health', 'Health'
        OTHERS = 'Others', 'Others'

    # The foreign key links the expense to the specific user who created it
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHERS)
    description = models.TextField(blank=True)
    date = models.DateField()
    
    # Automatically tracks when record is created/updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - ${self.amount}"