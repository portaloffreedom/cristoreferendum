from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from whoiscristo.models import Choice, Vote
from whoiscristo.pollsmanager import get_current_poll


def index(request):
    return render(request, 'whoiscristo/index.html')


@login_required
def visualize_last_winner(request):
    last_week_poll = get_current_poll()
    from whoiscristo.models import Vote, Choice
    choices = Choice.objects.filter(poll=last_week_poll.id)
    message = ""
    for choice in choices:
        choice.votes = Vote.objects.filter(choice=choice.id).count()
        message += "votes for {} and reason \"{}\": {}<br>".format(choice.user, choice.reason, choice.votes)
    return HttpResponse("Last Week Poll Winner {}<br>{}".format(choices.count(), message))


@login_required
def create_new_choice(request):
    if request.method == 'POST':
        user_id = request.POST.get('user', None)
        reason_text = request.POST.get('reason', None)
        if user_id is not None and reason_text is not None:
            user = User.objects.get(id=user_id)

            choice = Choice.objects.create(
                poll=get_current_poll(),
                user=user,
                reason=reason_text,
            )

            return HttpResponse("user: {}<br>reason: {}".format(
                choice.user,
                choice.reason
            ))

    users = User.objects.all()
    current_poll = get_current_poll()
    context = {
        'users': users,
        'current_poll': current_poll,
    }
    return render(request, 'whoiscristo/create_vote.html', context)


@login_required
def vote_current_poll(request):
    if request.method == 'POST':
        choice_id = request.POST.get('choice', None)
        if choice_id is not None:
            choice = Choice.objects.get(id=choice_id)
            (vote, created) = Vote.objects.get_or_create(voter=request.user, poll=choice.poll)
            vote.choice = choice
            vote.date = timezone.now()
            vote.save()

            return HttpResponse("your vote: {} - {}".format(choice.user, choice.reason))

    current_poll = get_current_poll()
    choices = Choice.objects.filter(poll=current_poll.id)
    context = {
        'choices': choices,
    }
    return render(request, 'whoiscristo/vote.html', context)
