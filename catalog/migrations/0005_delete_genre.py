# Generated by Django 3.2.9 on 2021-11-23 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_book_genre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
