# Generated by Django 4.1.7 on 2023-02-20 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_comments_post_votes_alter_comment_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='post_comments', to='posts.comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='post_votes', to='posts.vote'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_votes', to='posts.post'),
        ),
    ]
