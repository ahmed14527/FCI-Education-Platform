# Generated by Django 4.2.1 on 2024-01-30 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MCQQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='Queiz.mcqassignment')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Option', models.CharField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='Queiz.mcqquestion')),
            ],
        ),
        migrations.CreateModel(
            name='MCQSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='Queiz.mcqassignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MCQAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='Queiz.mcqquestion')),
                ('selected_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Queiz.option')),
            ],
        ),
        migrations.CreateModel(
            name='CorrectAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Queiz.option')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer', to='Queiz.mcqquestion')),
            ],
        ),
    ]