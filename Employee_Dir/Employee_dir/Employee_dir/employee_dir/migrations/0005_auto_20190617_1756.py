# Generated by Django 2.1 on 2019-06-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_dir', '0004_auto_20190617_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_dir',
            name='Emp_date_of_joining',
            field=models.DateField(null=True, verbose_name='Employee Date of Joining'),
        ),
    ]
