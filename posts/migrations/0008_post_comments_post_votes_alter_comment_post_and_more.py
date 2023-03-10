# Generated by Django 4.1.7 on 2023-02-20 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_post_votes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='posts_comments', to='posts.comment'),
        ),
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='posts_votes', to='posts.vote'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_comments', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_votes', to='posts.post'),
        ),
    ]
