# Generated by Django 4.1.1 on 2022-09-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_book_readers_alter_book_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'ok'), (2, 'fine'), (3, 'goog'), (4, 'amazing'), (5, 'incredible')], null=True),
        ),
    ]
