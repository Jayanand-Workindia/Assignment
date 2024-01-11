from rest_framework import serializers
from .models import Candidates, Jobs, Logs

class CandidateSerializer(serializers.ModelSerializer):
    candidate_id = serializers.IntegerField(required=True)
    location = serializers.CharField(required=True, max_length=50)
    domain = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = Candidates
        fields = ('__all__')

class JobSerializer(serializers.ModelSerializer):
    job_id = serializers.CharField(required=True, max_length=5)
    job_title = serializers.CharField(required=True, max_length=50)
    company_name = serializers.CharField(required=True, max_length=50)
    salary = serializers.CharField(required=True, max_length=50)
    start_time = serializers.CharField(required=True, max_length=17)
    end_time = serializers.CharField(required=True, max_length=17)
    start_day = serializers.CharField(required=True, max_length=10)
    end_day = serializers.CharField(required=True, max_length=10)
    location = serializers.CharField(required=True, max_length=50)
    contact_person = serializers.CharField(required=True, max_length=50)
    contact_phno = serializers.CharField(required=True, max_length=10)

    class Meta:
        model = Jobs
        fields = ('__all__')

class LogSerializer(serializers.ModelSerializer):
    candidate_id = serializers.IntegerField(required=True)
    job_id = serializers.CharField(required=True, max_length=5)
    action = serializers.CharField(required=True, max_length=20)

    def create(self, validated_data):
        return Logs.objects.create(**validated_data)
    
    class Meta:
        model = Logs
        fields = ('__all__')