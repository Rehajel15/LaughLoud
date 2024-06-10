from django.contrib import admin
from .models import Joke, Notification, ReportedJoke

class JokeAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at',)
    search_fields = ['id', 'created_at', 'joke', 'category', 'from_user']


class ReportedJokeAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'joke_id', 'ReportCategory', 'ReportTextField', 'joke', 'from_user')
    search_fields = ['id', 'joke_id', 'ReportCategory', 'ReportTextField', 'joke', 'from_user']

class NotificationAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'sended_on')
    search_fields = ['id', 'sended_on', 'header', 'content', 'for_user']


# Register your models here.
admin.site.register(Joke, JokeAdmin)
admin.site.register(ReportedJoke, ReportedJokeAdmin)
admin.site.register(Notification, NotificationAdmin)


