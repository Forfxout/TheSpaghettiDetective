# Generated by Django 2.1.11 on 2020-03-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_gcodefile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slack_access_token',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
