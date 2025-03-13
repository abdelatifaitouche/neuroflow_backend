# Generated by Django 4.2.19 on 2025-03-13 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procedureflow', '0008_delete_process'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teamflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedureflow.procedure')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
