# Generated by Django 3.1.2 on 2020-11-08 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_document_doc_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_text',
            field=models.TextField(null=True),
        ),
    ]
