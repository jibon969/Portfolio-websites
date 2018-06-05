


from django.shortcuts import render

from about.admin import About, Experience,Education, Skill, Interest,  Award

# Create your views here.


def about(request):

    about       = About.objects.all()
    experience  = Experience.objects.all()
    education   = Education.objects.all()
    skill       = Skill.objects.all()
    interest    = Interest.objects.all()
    award       = Award.objects.all()

    context = {

        'abouts'        : about,
        'experiences'   : experience,
        'educations'    : education,
        'skills'        : skill,
        'interests'     : interest,
        'awards'        : award,

    }
    return render(request, 'index.html', context)
