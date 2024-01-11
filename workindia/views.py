from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Candidates, Jobs, Logs
from .serializers import CandidateSerializer, JobSerializer, LogSerializer
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['GET'])
def get_jobs(request, candidate_id):
    mycandidate = Candidates.objects.filter(candidate_id=candidate_id)[0]
    # print(mycandidate.location)
    result = Jobs.objects.filter(location=mycandidate.location, job_title=mycandidate.domain).values()
    to_validate = []
    for res in result:
        to_validate.append(res)
    serializer = JobSerializer(data=to_validate, many=True)
    if serializer.is_valid():
        validated = []
        for job in serializer.data:
            tmp = {
                'id': job.get('job_id'),
                'job_title': job.get('job_title'),
                'company_name': job.get('company_name'),
                'salary': job.get('salary'),
                'time': {
                    'start_time': job.get('start_time'),
                    'end_time': job.get('end_time')
                },
                'working_days': {
                    'start_day': job.get('start_day'),
                    'end_day': job.get('end_day')
                },
                'location': job.get('location'),
                'contact_person': job.get('contact_person'),
            }
            validated.append(tmp)
        # print(serializer.data[0]['job_id'])
        return Response({'status': 'success', 'data':validated}, status=status.HTTP_200_OK)
    else:
        print(serializer.errors)
        return Response({'status': 'failure'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def store_action(request, candidate_id):
    data = JSONParser().parse(request)
    data['candidate_id'] = candidate_id
    serializer = LogSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        # print(serializer.data)
        if data['action'].lower() == 'call':
            result = Jobs.objects.filter(job_id=data['job_id']).values()[0]
            # print(result['contact_phno'])
            return Response({"status": "success", "phno": result['contact_phno']}, status=status.HTTP_200_OK)
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    return Response({"status": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)