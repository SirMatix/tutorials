# Generated by Django 2.2.6 on 2020-01-20 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_remove_tutoriallanguage_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcategory',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='tutorials.TutorialLanguage', verbose_name='Language'),
        ),
    ]