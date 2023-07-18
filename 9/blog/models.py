from django.db import models
from django.utils import timezone 
#from extensions.utils import jalali_converter

#my Managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
                

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name="children",verbose_name="subordinate")
    title=models.CharField(max_length=200,)
    slug=models.SlugField(max_length=100,unique=True)
    status=models.BooleanField(default=True,verbose_name="Will it be displayed for you ?")
    position=models.IntegerField()

    class Meta :
        verbose_name="category"
        verbose_name_plural="categorys"
        ordering=['parent__id','position']

    def __str__(self):
        return self.title 

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES=(
        ('d','Draft'),
        ('p',"Publish"),
    )
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=100,unique=True)
    category=models.ManyToManyField(Category,verbose_name="category",related_name="articles")
    description=models.TextField()
    thumbnail=models.ImageField(upload_to="images")
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1,choices=STATUS_CHOICES)

    def category_published(self):
        return self.category.filter(status=True)



    class Meta :
        verbose_name="article"
        verbose_name_plural="articles"
        ordering=['-publish']



    def __str__(self):
        return self.title

    #def jpublish (self):
    #    return jalali_converter(self.publish)
    #jpublish.short_description = "زمان انتشار "

    objects= ArticleManager() 

class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name="comments")
    name=models.CharField(max_length=100)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)

    class Meta:
        ordering=('created',)

    def __str__(self):
        return "Comment by{0} on {1}".format (self.name,self.article)



    

