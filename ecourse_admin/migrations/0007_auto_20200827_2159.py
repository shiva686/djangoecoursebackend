# Generated by Django 3.0.8 on 2020-08-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecourse_admin', '0006_courses_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='courses',
            name='videos',
            field=models.TextField(),
        ),
    ]
