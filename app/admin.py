from django.contrib import admin
from .models import Userpro, UserSubmission, UserScore, Event, QuestionForEvent

# Register your models here.
admin.site.site_header = 'Top Ranker Adminstration'
admin.site.register(Userpro)
admin.site.register(UserSubmission)
admin.site.register(UserScore)
admin.site.register(Event)
admin.site.register(QuestionForEvent)
