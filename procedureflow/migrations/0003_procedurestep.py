# Generated by Django 4.2.19 on 2025-03-03 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('procedureflow', '0002_procedure_status_procedure_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcedureStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('is_validated', models.BooleanField(default=False)),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='procedureflow.procedure')),
                ('validator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='validated_steps', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='written_steps', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['step_number'],
            },
        ),
    ]
