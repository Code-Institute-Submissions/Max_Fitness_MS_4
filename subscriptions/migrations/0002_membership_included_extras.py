# Generated by Django 3.1.3 on 2020-12-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='included_extras',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
    ]