# Generated by Django 3.1.2 on 2020-11-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20201108_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='doc_up',
        ),
        migrations.AlterField(
            model_name='document',
            name='document_text',
            field=models.TextField(),
        ),
    ]
