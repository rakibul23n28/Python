# Generated by Django 4.2.1 on 2023-07-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_alter_conversation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
