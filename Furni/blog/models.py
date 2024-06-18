from django.db import models

class Date(models.Model):
    date = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.date}"


class Month(models.TextChoices):
    january = ("Jan", "january")
    february = ("Feb", "february")
    march = ("Mar", "march")
    april = ("Apr", "april")
    may = ("May", "may")
    june = ("June", "june")
    july = ("July", "july")
    august = ("Aug", "august")
    september = ("Sep", "september")
    october = ("Oct", "october")
    november = ("Nov", "november")
    december = ("Dec", "december")

class Year(models.Model):
    year = models.PositiveBigIntegerField(default=2024)

    def __str__(self):
        return f"{self.year}"


class Creator(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/blog/post/")
    description = models.TextField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(verbose_name="Slug", max_length=255)
    image = models.ImageField(upload_to="media/blog/post/")
    text = models.TextField()
    views = models.PositiveBigIntegerField(default=0)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    month = models.CharField(max_length=100, choices=Month.choices, default=Month.january)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.title
