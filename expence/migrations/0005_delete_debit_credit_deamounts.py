# Generated by Django 4.1.4 on 2023-02-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expence', '0004_remove_credit_user_remove_debit_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Debit',
        ),
        migrations.AddField(
            model_name='credit',
            name='deamounts',
            field=models.FloatField(default=0),
        ),
    ]
