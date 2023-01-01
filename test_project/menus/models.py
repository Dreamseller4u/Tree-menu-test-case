from django.db import models


class MenuTree(models.Model):

    title = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    def __str__(self):
        return self.title


class SubMenu(models.Model):

    title = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    category = models.ForeignKey(
        MenuTree, on_delete=models.CASCADE, blank=False, null=False)
       

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return self.title
