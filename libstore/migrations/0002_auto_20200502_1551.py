# Generated by Django 2.2 on 2020-05-02 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library_manager',
            name='review',
        ),
        migrations.RemoveField(
            model_name='library_manager',
            name='title',
        ),
        migrations.AddField(
            model_name='library_manager',
            name='img',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='library_manager',
            name='overview',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='library_manager',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='library_manager',
            name='stored_file',
            field=models.FileField(blank=True, default='default.pdf', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='library_manager',
            name='topic_title',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='library_manager',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='library_manager',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
