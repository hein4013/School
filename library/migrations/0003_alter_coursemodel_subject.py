# Generated by Django 3.2.23 on 2024-02-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_coursemodel_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
