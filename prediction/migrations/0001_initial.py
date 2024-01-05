# Generated by Django 3.1.7 on 2021-07-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(default=None, max_length=100)),
                ('file_data', models.FileField(blank=True, null=True, upload_to='uploads/download/')),
            ],
        ),
    ]