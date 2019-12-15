# Generated by Django 2.1.5 on 2019-02-02 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
#import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_seed_data_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicTimelapse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('priority', models.IntegerField(default=1000000)),
                ('video_url', models.CharField(max_length=2000)),
                ('poster_url', models.CharField(max_length=2000)),
                ('creator_name', models.CharField(max_length=500)),
                #('frame_p', jsonfield.fields.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='historicalprinter',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalprinter',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='printercommand',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printercommand',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
