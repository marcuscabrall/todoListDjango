# Generated by Django 5.1.3 on 2024-11-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0005_alter_todo_created_at_alter_todo_deadline_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="todo",
            name="finished_at",
            field=models.DateField(blank=True, null=True),
        ),
    ]
