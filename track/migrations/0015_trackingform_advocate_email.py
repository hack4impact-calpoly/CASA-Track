# Generated by Django 2.0.5 on 2019-06-19 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0014_auto_20190612_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackingform',
            name='advocate_email',
            field=models.EmailField(default='advocate_email', max_length=254),
            preserve_default=False,
        ),
    ]
