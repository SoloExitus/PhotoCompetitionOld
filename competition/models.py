from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return f'user:{self.user.username} comment'


class PhotoPost(models.Model):
    APPROVED = 3
    AWAIT = 2
    REJECTED = 1
    REMOVED = 0

    PostStatusChoices = (
        (APPROVED, 'approved'),
        (AWAIT, 'await'),
        (REJECTED, 'rejected'),
        (REMOVED, 'removed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(blank=True)
    status = models.PositiveIntegerField(choices=PostStatusChoices, default=AWAIT)
    published_date = models.DateTimeField(null=True)
    remove_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='photo/')

    comments = GenericRelation(Comment, related_query_name='post')

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    post = models.ForeignKey(PhotoPost, on_delete=models.CASCADE, related_name='whoLike')

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'user:{self.user.username} like post:{self.post.title}'

