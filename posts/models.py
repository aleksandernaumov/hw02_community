from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Сообщество', max_length=200)
    slug = models.SlugField(
        'Ссылка (slug)', unique=True, max_length=200
    )
    description = models.TextField(
        'Описание', help_text='Краткое описание сообщества'
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts', verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True, null=True, related_name='posts',
        verbose_name='Сообщество'
    )

    def posts_list(group=None):
        posts_list = Post.objects.order_by('-pub_date')
        if group is not None:
            posts_list = posts_list.filter(group=group)
        return posts_list

    def __str__(self):
        return f'{self.author} - {self.pub_date.date()} - {self.text[:20]} ...'
