# Generated by Django 4.0.1 on 2022-01-29 04:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID for the event', unique=True)),
                ('log_level', models.CharField(choices=[('DEBUG', 'Debug'), ('INFO', 'Info'), ('WARNING', 'Warning'), ('ERROR', 'Error'), ('CRITICAL', 'Critical')], help_text='Log level of the event', max_length=50)),
                ('service_id', models.CharField(help_text='An ID for the service that is generating the event', max_length=255)),
                ('instance_id', models.CharField(blank=True, help_text='Unique ID for the service instance incase the service is distributed', max_length=255)),
                ('service_name', models.CharField(help_text='The name of the service that is generating the event', max_length=255)),
                ('service_info', models.CharField(help_text='Additional information about the service that is generating the event', max_length=255)),
                ('request_id', models.CharField(help_text='An ID for the request that is generating the event. Usually passed around to track events related to a request', max_length=255)),
                ('event_action', models.CharField(choices=[('CREATE', 'Create'), ('UPDATE', 'Update'), ('DELETE', 'Delete'), ('RETRIEVE', 'Retrieve'), ('OTHER', 'Other')], help_text='The type of event that is being generated', max_length=255)),
                ('event_data', models.JSONField(default=dict, help_text='Data generated from the service or passed to it from a request')),
                ('event_metadata', models.JSONField(default=dict, help_text='Additional metadata about the event')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
