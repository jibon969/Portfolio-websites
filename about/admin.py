from django.contrib import admin
from about.models import About, Experience,Education, Skill, Interest, Award

# Register your models here.


class About_Admin(admin.ModelAdmin):

    list_display = ["firstName", "lastName", "email"]

admin.site.register(About, About_Admin)


class Experience_Admin(admin.ModelAdmin):

    list_display = ["title", "year"]

admin.site.register(Experience, Experience_Admin)



class Education_Admin(admin.ModelAdmin):

    list_display = ["name", "dept"]

admin.site.register(Education, Education_Admin)



class Skill_Admin(admin.ModelAdmin):

    list_display = ["mySkill"]

admin.site.register(Skill, Skill_Admin)



class Interest_Admin(admin.ModelAdmin):

    list_display = ["myInterest"]

admin.site.register(Interest, Interest_Admin)


class  Award_Admin(admin.ModelAdmin):

    list_display = ["myAward"]

admin.site.register(Award,  Award_Admin)