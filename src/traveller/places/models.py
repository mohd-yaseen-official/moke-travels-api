from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    location = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='places/images/')

    category = models.ForeignKey('places.Category', on_delete=models.CASCADE)

    likes = models.ManyToManyField('auth.User', related_name='liked_posts', blank=True)

    class Meta:
        db_table = 'traveller_places'
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
    
    def __str__(self):
        return self.name
    
    def total_likes(self):
        return self.likes.count()
    

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories/images/')

    class Meta:
        db_table = 'traveller_categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    place = models.ForeignKey('places.Place', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/images/')

    class Meta:
        db_table = 'traveller_gallery'
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
    
    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    place = models.ForeignKey('places.Place', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'traveller_comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment
    

class Reply(models.Model):
    comment = models.ForeignKey('places.Comment', on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'traveller_replies'
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'

    def __str__(self):
        return self.reply