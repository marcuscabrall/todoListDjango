# Generated by Django 5.1.3 on 2024-11-19 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0003_alter_todo_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
