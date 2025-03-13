# Generated by Django 4.2.19 on 2025-03-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamflow', '0002_process_delete_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='status',
            field=models.CharField(choices=[('Launched', 'Launched'), ('Halted', 'Halted'), ('Ended', 'Ended'), ('Aborted', 'Aborted')], default='Launched', max_length=20),
        ),
    ]
