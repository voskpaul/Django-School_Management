# Generated by Django 3.0.5 on 2020-05-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbulkupload',
            name='csv_file',
            field=models.FileField(upload_to='students/bulkupload/'),
        ),
    ]