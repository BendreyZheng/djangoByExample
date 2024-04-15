from django.shortcuts import render, get_object_or_404
from .models import JournalProfile
from django.http import Http404

# Create your views here.
def journal_list(req):
    profiles = JournalProfile.open.all()
    return render(req,
                'journal/profile/list.html',
                {'profiles': profiles})

def profile_detail(req, id):
    # try:
    #     profile = JournalProfile.open.get(id=id)
    # except JournalProfile.DoesNotExist:
    #     raise Http404("No Journal Found.")
    
    profile = get_object_or_404(JournalProfile,
                                id=id,
                                status=JournalProfile.Status.OPEN)
    
    return render(req,
                  'journal/profile/detail.html',
                  {'profile': profile})



