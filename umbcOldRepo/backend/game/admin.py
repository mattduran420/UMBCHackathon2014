from django.contrib import admin
from game.models import *

admin.site.register(Question)
admin.site.register(Game)
admin.site.register(GameEndResult)
admin.site.register(QuestionUnitTest)