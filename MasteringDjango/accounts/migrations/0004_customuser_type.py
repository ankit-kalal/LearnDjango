# Generated by Django 4.1 on 2022-08-05 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_groups_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('Seller', 'SELLER'), ('Customer', 'CUSTOMER')], default='Customer', max_length=255, verbose_name='Type'),
        ),
    ]