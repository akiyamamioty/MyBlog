from django.db import models
from django.contrib import admin
# Create your models here.

class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    timestamp = models.DateTimeField()
    body_markdown = models.TextField('Entry body', help_text='Use Markdown syntax.')
    body = models.TextField(blank=True, null=True)
    
    def save(self):
        import markdown
        self.body = markdown.markdown(self.body_markdown)
        super(BlogsPost, self).save()
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp','body',)

admin.site.register(BlogsPost,BlogPostAdmin)
'''
class BlogsPost(models.Model):
    title = models.CharField('Title', max_length=250)
    timestamp = models.DateTimeField('Date published')
    body_markdown = models.TextField('Entry body', help_text='Use Markdown syntax.')
    body = models.TextField('Entry body as HTML', blank=True, null=True)

    class Admin:
        fields = (
            (None, {'fields': ('title', 'timestamp', 'body_markdown')}),
            )

    def save(self):
        import markdown
        self.body = markdown.markdown(self.body_markdown)
        super(BlogsPost, self).save() # Call the "real" save() method.
admin.site.register(BlogsPost)
'''