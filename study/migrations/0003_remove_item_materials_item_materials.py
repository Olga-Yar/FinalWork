# Generated by Django 4.2.4 on 2023-09-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_alter_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='materials',
        ),
        migrations.AddField(
            model_name='item',
            name='materials',
            field=models.ManyToManyField(blank=True, null=True, to='study.materials'),
        ),
    ]
