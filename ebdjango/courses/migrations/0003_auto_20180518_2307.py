# Generated by Django 2.0.5 on 2018-05-19 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180518_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectioninfo',
            name='course_info',
        ),
        migrations.AddField(
            model_name='courseinfo',
            name='secitons',
            field=models.ManyToManyField(blank=True, to='courses.SectionInfo'),
        ),
    ]
