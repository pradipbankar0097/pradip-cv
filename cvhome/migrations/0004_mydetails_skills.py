# Generated by Django 4.0.4 on 2022-06-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvhome', '0003_mydetails_no_of_academic_projects_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydetails',
            name='skills',
            field=models.CharField(default='C/C++,Python,Java,SQL,MongoDB', max_length=1000),
        ),
    ]
