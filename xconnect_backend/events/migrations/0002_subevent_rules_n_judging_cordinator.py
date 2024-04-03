# Generated by Django 4.2.3 on 2024-03-23 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subevent",
            name="rules_n_judging",
            field=models.TextField(default="das"),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Cordinator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("contact_no", models.IntegerField()),
                (
                    "sub_event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.subevent",
                    ),
                ),
            ],
        ),
    ]