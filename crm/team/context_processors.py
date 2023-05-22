from .models import Team


def active_team(request):
    if request.user.is_authenticated:
        if request.user.userprofile.active_team:
            active_team = request.user.userprofile.active_team
        else:
            active_team = Team.objects.filter(created_by=request.user).first()
    else:
        active_team = None