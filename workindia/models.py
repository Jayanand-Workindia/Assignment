from django.db import models

# Create your models here.
class Candidates(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)

    class Meta:
        db_table = 'candidates'

    def __str__(self):
        return str(self.candidate_id)
    
class Jobs(models.Model):
    job_id = models.CharField(max_length=5, primary_key=True)
    job_title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    start_time = models.CharField(max_length=17)
    end_time = models.CharField(max_length=17)
    start_day = models.CharField(max_length=10)
    end_day = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    contact_phno = models.CharField(max_length=10)

    class Meta:
        db_table = 'jobs'

    def __str__(self):
        return self.job_id
    
class Logs(models.Model):
    candidate_id = models.IntegerField()
    job_id = models.CharField(max_length=5)
    action = models.CharField(max_length=20)

    class Meta:
        db_table = 'logs'
        
    def __str__(self):
        return self.candidate_id + ': ' + self.job_id + ' -> ' + self.action