from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from .serializers import RegisterSerializer, ExpenseSerializer
from .models import Expense

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 1. Isolate data: Only return expenses belonging to the authenticated user
        queryset = Expense.objects.filter(user=self.request.user)
        
        # 2. Extract query parameters from the URL
        timeframe = self.request.query_params.get('timeframe', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        today = timezone.now().date()

        # 3. Apply timeframe filters if requested
        if timeframe == 'past_week':
            queryset = queryset.filter(date__gte=today - timedelta(days=7))
        elif timeframe == 'past_month':
            queryset = queryset.filter(date__gte=today - timedelta(days=30))
        elif timeframe == 'last_3_months':
            queryset = queryset.filter(date__gte=today - timedelta(days=90))
            
        # 4. Apply custom date range if requested
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])
            
        return queryset