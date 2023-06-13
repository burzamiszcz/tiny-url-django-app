from django.db import models
import hashlib

# Create your models here.
class Urls(models.Model):
    main_url = models.URLField()
    tiny_url = models.CharField(max_length=10, unique=True, blank=True)
    
    def save(self):
        if not self.tiny_url:
            hash_object = hashlib.sha256(self.main_url.encode('utf-8'))
            tiny_hash = hash_object.hexdigest()[:10]
            self.tiny_url = tiny_hash
        super().save()
    
    def __str__(self) -> str:
        return self.main_url
