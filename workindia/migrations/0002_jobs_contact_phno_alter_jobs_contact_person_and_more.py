# Generated by Django 5.0.1 on 2024-01-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workindia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='contact_phno',
            field=models.CharField(default=8451817575, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobs',
            name='contact_person',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='end_time',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='start_time',
            field=models.CharField(max_length=17),
        ),
    ]