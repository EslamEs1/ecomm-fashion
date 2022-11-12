from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings


# Start Blog
class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='blog/%Y/%m/%d', verbose_name='image')
    description = models.TextField(max_length=15000)
    slug = models.SlugField(max_length=80, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.slug])

    def __str__(self):
        return self.author.username + self.title
