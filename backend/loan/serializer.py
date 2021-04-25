from rest_framework import serializers
from loan.models import LoanRemaining,LoanModel

class LoanRemainingSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoanRemaining
        fields=('__all__')

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoanModel
        fields=('__all__')