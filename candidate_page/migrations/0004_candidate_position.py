# Generated by Django 3.2.3 on 2021-06-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_page', '0003_rename_hunter_candidate_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
