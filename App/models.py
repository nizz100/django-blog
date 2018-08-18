from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name='博客标题')
    category = models.CharField(max_length=20, blank=True, verbose_name='博客类型')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True)
    content = UEditorField(null=True, blank=True, verbose_name='博文',imagePath="media/blog/images/",
                                  toolbars='besttome', filePath='media/blog/files/')

    class Meta:
        ordering = ['-pub_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title