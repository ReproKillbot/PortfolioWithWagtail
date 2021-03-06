# Generated by Django 3.0.5 on 2020-04-28 01:05

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Escort', 'Escort'), ('Commission', 'Commission'), ('On The Road', 'On The Road'), ('Intrigue', 'Intrigue'), ('Rumor', 'Rumor')], max_length=60)),
                ('description', models.CharField(max_length=124)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestBlogRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('blog', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quest_blog_relationship', to='base_pages.BlogPage')),
                ('quest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='quests.Quest')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
