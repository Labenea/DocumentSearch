# Generated by Django 3.1.2 on 2020-11-16 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_document_doc_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]
