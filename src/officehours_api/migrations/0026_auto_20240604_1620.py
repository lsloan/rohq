# Generated by Django 3.2.25 on 2024-06-04 20:20

import django.contrib.postgres.fields
from django.db import migrations, models
import officehours_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('officehours_api', '0025_meeting_start_logs_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingStartLogsView',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('queue', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('attendees', models.JSONField()),
                ('assignee', models.JSONField()),
                ('backend_metadata', models.JSONField()),
                ('backend_type', models.TextField()),
                ('agenda', models.TextField()),
                ('view', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'meeting_start_logs',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='attendee',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='backend_type',
            field=models.CharField(choices=[['inperson', 'In Person']], default=officehours_api.models.get_default_backend, max_length=20),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='queue',
            name='allowed_backends',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[['inperson', 'In Person']], max_length=20), default=officehours_api.models.get_default_allowed_backends, size=None),
        ),
        migrations.AlterField(
            model_name='queue',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
    ]
