# Generated by Django 5.1.3 on 2024-11-19 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0002_alter_todo_deadline_alter_todo_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="description",
            field=models.CharField(help_text="Enter a description", max_length=255),
        ),
    ]
