from django.db import models


class Menu(models.Model):
    title = models.CharField(verbose_name="Название меню", max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, 
                               blank=True, null=True, related_name="children",
                               verbose_name="Меню-родитель")

    def __str__(self):         
        '''Отображение меню в формате menu -> submenu'''                  
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' > '.join(full_path[::-1]) 
    
    def save(self, *args, **kwrags):
        self.title = self.title.capitalize()
        return super().save(self, *args, **kwrags)
    