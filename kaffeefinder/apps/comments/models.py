from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    cafe = models.ForeignKey("cafes.Cafe", on_delete=models.CASCADE, verbose_name="کافی شاپ")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    content = models.CharField(max_length=2048, verbose_name="متن نظر")
    is_confirmed = models.BooleanField(default=False, verbose_name="تایید شده")
    timestamp = models.DateTimeField(auto_now_add=True)
    avg_rating = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="reviews/photos/%Y/%M", verbose_name="عکس")
    
    class Meta:
        verbose_name_plural = "نظرات کاربران"

    def __str__(self):
        return f"نظر{self.cafe.title}" 

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    cafe = models.ForeignKey("cafes.Cafe", on_delete=models.CASCADE)
    point = models.IntegerField(verbose_name="امتیاز")

    class Meta:
        verbose_name_plural = "امتیازها"
        unique_together = [["user", "cafe"]]

    def __str__(self):
        return f"نظر {self.user.username} برای {self.cafe}"