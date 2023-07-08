from django.shortcuts import render, redirect
from .forms import NewUserForm, addnewteam, addnewplayer
from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth import login, authenticate, logout  # add this
from .models import team, player, livematch, match_details
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

global nteam1
global nteam2
global noteam
global matchscore
global current
global details
global players1
global players2
global bat1, bat2, bowl
global s1, s2, b1, b2, bs, w, o


def home(request):
    global noteam
    noteam = 2
    context = {}
    context["dataset"] = livematch.objects.all()
    return render(request, 'home.html', context)


def plyerdetails(request):
    id = request.POST.get('id')
    obj = get_object_or_404(livematch, id=id)
    teamid = obj.team_id
    obj1 = get_object_or_404(team, id=teamid)
    teamid = teamid + 1
    obj2 = get_object_or_404(team, id=teamid)
    players = player.objects.all()
    temp = []
    temp1 = []
    obj3 = get_object_or_404(match_details, match_id=id)
    for p in players:
        if p.team_id == obj1.id:
            temp.append(p)
        elif p.team_id == obj2.id:
            temp1.append(p)
    context = {}
    context['match'] = obj
    context["matchdetails"] = obj3
    context["team1"] = obj1
    context["team2"] = obj2
    context["players1"] = temp
    context["players2"] = temp1

    return render(request, 'details.html', context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("cricket:home")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect("cricket:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("cricket:home")


def addnewmatch(request):
    # global numofteam
    # if numofteam:
    #     context = {}
    #     numofteam = numofteam - 1
    #     form = addnewteam(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #     if numofteam == 0:
    #         form = addnewplayer(request.POST or None)
    #         context['form'] = form
    #         return render(request, "player_name.html", context)
    #     context['form'] = form
    #     return render(request, "create_view.html", context)
    # # context = {}
    # # context["dataset"] = team.objects.all()
    return render(request=request, template_name="team_name_form.html")


def team_name(request):
    global nteam1
    global nteam2
    global noteam
    global matchscore
    global current
    global players1
    global players2
    global bat1, bat2, bowl, s1, b1, s2, b2, o, w, bs
    bat1 = 0
    bat2 = 1
    bowl = 0
    s1 = 0
    b1 = 0
    s2 = 1
    b2 = 1
    bs = 0
    o = 0
    w = 0
    team_name = request.POST.get('team1')
    u = team(teamname=team_name)
    u.save()
    if noteam == 2:
        nteam1 = u
    else:
        nteam2 = u
    noteam = noteam - 1
    player_name = request.POST.get('player1')
    p = player(playername=player_name, team=u)
    p.save()
    players = [p]
    player_name = request.POST.get('player2')
    p1 = player(playername=player_name, team=u)
    players.append(p1)
    p1.save()
    player_name = request.POST.get('player3')
    p1 = player(playername=player_name, team=u)
    players.append(p1)
    p1.save()
    player_name = request.POST.get('player4')
    p1 = player(playername=player_name, team=u)
    players.append(p1)
    p1.save()
    player_name = request.POST.get('player5')
    p1 = player(playername=player_name, team=u)
    players.append(p1)
    p1.save()
    player_name = request.POST.get('player6')
    p1 = player(playername=player_name, team=u)
    players.append(p1)
    p1.save()
    player_name = request.POST.get('player7')
    p1 = player(playername=player_name, team=u)
    players.append(p1)
    p1.save()
    player_name = request.POST.get('player8')
    p1 = player(playername=player_name, team=u)
    players.append(p1)
    p1.save()
    player_name = request.POST.get('player9')
    p1 = player(playername=player_name, team=u)
    players.append(p1)
    p1.save()
    player_name = request.POST.get('player10')
    p1 = player(playername=player_name, team=u)
    players.append(p1)
    p1.save()
    player_name = request.POST.get('player11')
    p1 = player(playername=player_name, team=u)
    players.append(p1)
    p1.save()

    # context["dataset"] = player.objects.all()
    # context["dataset2"] = team.objects.all()
    if noteam == 0:
        players2 = players
        m1 = livematch(team=nteam1, teamname1=nteam1.teamname,
                       teamname2=nteam2.teamname)
        m1.save()
        matchscore = m1
        current = 1
        return render(request, "matchdetail.html")
    else:
        players1 = players
        return render(request=request, template_name="team_name_form.html")


def matchdetail(request):
    global matchscore, details
    over = int(request.POST.get('over'))
    venue = request.POST.get('venue')
    matchdetail = match_details(over=over, venue=venue, match=matchscore)
    matchdetail.save()
    details = matchdetail
    matchscore.balls = over * 6
    context = {}
    context["dataset"] = matchscore
    matchscore = matchscore
    return render(request, "scoring.html", context)


# def addplayer_name(request):
#     global numofteam1
#     if numofplayer:
#         context = {}
#         numofplayer = numofplayer - 1
#         form = addnewplayer(request.POST or None)
#         if form.is_valid():
#             form.save()
#         context['form'] = form
#         return render(request, "player_name.html", context)
#     context = {}
# # add the dictionary during initialization
#     context["dataset"] = player.objects.all()
#     return render(request, "list_view.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    context["dataset"] = player.objects.all()
    context["dataset2"] = team.objects.all()
    return render(request, "list_view.html", context)


def update_score(request):
    global current
    global matchscore, details, players1, players2
    global bat1, bat2, bowl
    global s1, s2, b1, b2, bs, w, o

    context = {}
    context["dataset"] = matchscore
    context["current"] = current

    if 'inning_end' in request.POST:
        bat1 = 0
        s1 = 0
        b1 = 0
        bat2 = 1
        s2 = 1
        b2 = 1
        bowl = 0
        bs = 0
        w = 0
        o = 0
        if current == 1:
            current = 2
            matchscore.balls = details.over * 6
            matchscore.current_ball = 0

            matchscore.save()
            return render(request, "scoring.html", context)
        else:
            if current == 2 and matchscore.score2 > matchscore.score1:
                matchscore.win = 2
                matchscore.save()
                return render(request, "result.html", context)
            elif current == 2 and (matchscore.balls == 0 or matchscore.wicket2 == 10) and matchscore.score2 == matchscore.score1:
                return render(request, "result.html", context)
            elif current == 2 and (matchscore.balls == 0 or matchscore.wicket2 == 10):
                matchscore.win = 1
                matchscore.save()
                return render(request, "result.html", context)
            else:
                return redirect("cricket:home")
    if (matchscore.balls == 0 and current == 1) or (matchscore.wicket1 == 10 and current == 1):
        current = 2
        matchscore.balls = details.over * 6
        matchscore.current_ball = 0
        bat1 = 0
        s1 = 0
        b1 = 0
        bat2 = 1
        s2 = 1
        b2 = 1
        bowl = 0
        bs = 0
        w = 0
        o = 0
        matchscore.save()
    if current == 2 and matchscore.score2 > matchscore.score1:
        matchscore.win = 2
        matchscore.save()
        return render(request, "result.html", context)
    elif current == 2 and (matchscore.balls == 0 or matchscore.wicket2 == 10) and matchscore.score2 == matchscore.score1:
        return render(request, "result.html", context)
    elif current == 2 and (matchscore.balls == 0 or matchscore.wicket2 == 10):
        matchscore.win = 1
        matchscore.save()
        return render(request, "result.html", context)

    if current == 1:
        context["sc1"] = players1[s1].score
        context["sc2"] = players1[s2].score
        context["ball1"] = players1[b1].ball
        context["ball2"] = players1[b2].ball
        context["br"] = players2[bs].brun
        context["wiket"] = players2[w].wicket
        # context["ovr"] = players2[o].overs
        if matchscore.current_ball == 6:
            temp = bat1
            bat1 = bat2
            bat2 = temp
            bowl = (bowl + 1) % 11
            w = (w + 1) % 11
            o = (o + 1) % 11
            bs = (bs + 1) % 11

            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            # players2[o].overs = players2[o].overs + 1
            # context.update({'ovr':players2[o].overs})
        context.update({'sc1': players1[s1].score, 'ball1': players1[b1].ball,
                       'sc2': players1[s2].score, 'ball2': players1[b2].ball})
        context.update(
            {'br': players2[bs].brun, 'wiket': players2[w].wicket, 'ovr': players2[o].overs})
        context["player1"] = players1[bat1].playername
        context["player2"] = players1[bat2].playername
        context["player3"] = players2[bowl].playername
        players1[s1].save()
        players1[s2].save()
        players2[bs].save()
        # if matchscore.balls == 0 or matchscore.wicket1 == 10:
        #     current = 2
        #     return render(request, "scoring.html", context)
        if 'dot' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            players1[b1].ball = players1[b1].ball + 1
            players2[o].overs = players2[o].overs + \
                (matchscore.current_ball/10)
            # context.update({'ball1': players1[b1].ball, 'ovr':players2[o].overs})
            temp = details.over * 6 - matchscore.balls
            matchscore.over1 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'one' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score1 = matchscore.score1 + 1
            temp = bat1
            bat1 = bat2
            bat2 = temp

            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 1
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players1[s1].score, 'ball1': players1[b1].ball,
                           'sc2': players1[s2].score, 'ball2': players1[b2].ball})

            players2[bs].brun = players2[bs].brun + 1
            context.update({'br': players2[bs].brun})
            context.update(
                {'player1': players1[bat1].playername, 'player2': players1[bat2].playername})

            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            temp = details.over * 6 - matchscore.balls
            matchscore.over1 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'two' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score1 = matchscore.score1 + 2
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 2
            context.update(
                {'ball1': players1[b1].ball, 'sc1': players1[s1].score})

            players2[bs].brun = players2[bs].brun + 2
            context.update({'br': players2[bs].brun})

            temp = details.over * 6 - matchscore.balls
            matchscore.over1 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'three' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score1 = matchscore.score1 + 3
            temp = bat1
            bat1 = bat2
            bat2 = temp
            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 3
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players1[s1].score, 'ball1': players1[b1].ball,
                           'sc2': players1[s2].score, 'ball2': players1[b2].ball})

            context.update(
                {'player1': players1[bat1].playername, 'player2': players1[bat2].playername})

            players2[bs].brun = players2[bs].brun + 3
            context.update({'br': players2[bs].brun})

            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            temp = details.over * 6 - matchscore.balls
            matchscore.over1 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'four' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score1 = matchscore.score1 + 4
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 4

            context.update(
                {'ball1': players1[b1].ball, 'sc1': players1[s1].score})

            players2[bs].brun = players2[bs].brun + 4
            context.update({'br': players2[bs].brun})

            temp = details.over * 6 - matchscore.balls
            matchscore.over1 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'five' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score1 = matchscore.score1 + 5
            temp = bat1
            bat1 = bat2
            bat2 = temp

            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 5
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players1[s1].score, 'ball1': players1[b1].ball,
                           'sc2': players1[s2].score, 'ball2': players1[b2].ball})
            context.update(
                {'player1': players1[bat1].playername, 'player2': players1[bat2].playername})

            players2[bs].brun = players2[bs].brun + 5
            context.update({'br': players2[bs].brun})

            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            temp = details.over * 6 - matchscore.balls
            matchscore.over1 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'six' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score1 = matchscore.score1 + 6
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 6

            context.update(
                {'ball1': players1[b1].ball, 'sc1': players1[b1].score})

            players2[bs].brun = players2[bs].brun + 6
            context.update({'br': players2[bs].brun})

            temp = details.over * 6 - matchscore.balls
            matchscore.over1 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'wicket' in request.POST:
            if matchscore.wicket1 == 9:
                current = 2
                bat1 = 0
                s1 = 0
                b1 = 0
                bat2 = 1
                s2 = 1
                b2 = 1
                bowl = 0
                bs = 0
                w = 0
                o = 0

                matchscore.balls = details.over * 6
                matchscore.current_ball = 0
                matchscore.wicket1 = matchscore.wicket1 + 1
            else:
                matchscore.balls = matchscore.balls - 1
                matchscore.current_ball = matchscore.current_ball + 1
                matchscore.wicket1 = matchscore.wicket1 + 1
                temp = bat1
                temp1 = s1
                temp2 = b1
                if bat1 < bat2:
                    temp = bat2
                    bat1 = temp + 1
                    temp1 = s2
                    s1 = temp1 + 1
                    temp2 = b2
                    b1 = temp2 + 1
                else:
                    bat1 = bat1 + 1
                    b1 = b1 + 1
                    s1 = s1 + 1
            context.update({'ball1': players1[b1].ball, 'sc1': players1[s1].score,
                           'ball2': players1[b2].ball, 'sc2': players1[s2].score})
            context.update({'player1': players1[bat1].playername})

            players2[w].wicket = players2[w].wicket + 1
            context.update({'wiket': players2[w].wicket})

            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            temp = details.over * 6 - matchscore.balls
            matchscore.over1 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'wide' in request.POST:
            matchscore.score1 = matchscore.score1 + 1
            matchscore.save()
            players2[bs].brun = players2[bs].brun + 1
            context.update({'br': players2[bs].brun})
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "extra_runs.html")
        elif 'noball' in request.POST:
            matchscore.score1 = matchscore.score1 + 1
            matchscore.save()
            players2[bs].brun = players2[bs].brun + 1
            context.update({'br': players2[bs].brun})
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "extra_runs.html")
        elif 'freehit' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            players1[b1].ball = players1[b1].ball + 1
            # players2[o].overs = players2[o].overs + \
            #     (matchscore.current_ball/10)
            context.update(
                {'ball1': players1[b1].ball, 'ovr': players2[o].overs})
            temp = details.over * 6 - matchscore.balls
            matchscore.over1 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "extra_runs.html")
    else:
        context["sc1"] = players2[s1].score
        context["sc2"] = players2[s2].score
        context["ball1"] = players2[b1].ball
        context["ball2"] = players2[b2].ball
        context["br"] = players1[bs].brun
        context["wiket"] = players1[w].wicket
        context["ovr"] = players1[o].overs
        if matchscore.current_ball == 6:
            temp = bat1
            bat1 = bat2
            bat2 = temp
            bowl = (bowl + 1) % 11
            w = (w + 1) % 11
            o = (o + 1) % 11
            bs = (bs + 1) % 11
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            # players1[o].overs = players1[o].overs + 1
            # context.update({'ovr':players1[o].overs})
        context.update({'sc1': players2[s1].score, 'ball1': players2[b1].ball,
                       'sc2': players2[s2].score, 'ball2': players2[b2].ball})
        context["player1"] = players2[bat1].playername
        context["player2"] = players2[bat2].playername
        context["player3"] = players1[bowl].playername
        players2[s1].save()
        players2[s2].save()
        players1[bs].save()
        if 'dot' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            players2[b1].ball = players2[b1].ball + 1
            # players1[o].overs = players1[o].overs + (matchscore.current_ball/10)
            context.update(
                {'ball1': players2[b1].ball, 'ovr': players1[o].overs})

            players1[bs].brun = players1[bs].brun + 0
            context.update({'br': players1[bs].brun})

            temp = details.over * 6 - matchscore.balls
            matchscore.over2 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2+1
            return render(request, "scoring.html", context)
        elif 'one' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score2 = matchscore.score2 + 1
            temp = bat1
            bat1 = bat2
            bat2 = temp

            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 1
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players2[s1].score, 'ball1': players2[b1].ball,
                           'sc2': players2[s2].score, 'ball2': players2[b2].ball})
            context.update(
                {'player1': players2[bat1].playername, 'player2': players2[bat2].playername})

            players1[bs].brun = players1[bs].brun + 1
            context.update({'br': players1[bs].brun})

            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            temp = details.over * 6 - matchscore.balls
            matchscore.over2 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2+1
            return render(request, "scoring.html", context)
        elif 'two' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score2 = matchscore.score2 + 2
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1

            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 2
            context.update(
                {'ball1': players2[b1].ball, 'sc1': players2[s1].score})

            players1[bs].brun = players1[bs].brun + 2
            context.update({'br': players1[bs].brun})

            temp = details.over * 6 - matchscore.balls
            matchscore.over2 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2+1
            return render(request, "scoring.html", context)
        elif 'three' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score2 = matchscore.score2 + 3
            temp = bat1
            bat1 = bat2
            bat2 = temp

            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 3
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players2[s1].score, 'ball1': players2[b1].ball,
                           'sc2': players2[s2].score, 'ball2': players2[b2].ball})
            context.update(
                {'player1': players2[bat1].playername, 'player2': players2[bat2].playername})

            players1[bs].brun = players1[bs].brun + 3
            context.update({'br': players1[bs].brun})

            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            temp = details.over * 6 - matchscore.balls
            matchscore.over2 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2+1
            return render(request, "scoring.html", context)
        elif 'four' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score2 = matchscore.score2 + 4
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1

            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 4
            context.update(
                {'ball1': players2[b1].ball, 'sc1': players2[s1].score})

            players1[bs].brun = players1[bs].brun + 4
            context.update({'br': players1[bs].brun})

            temp = details.over * 6 - matchscore.balls
            matchscore.over2 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2+1
            return render(request, "scoring.html", context)
        elif 'five' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score2 = matchscore.score2 + 5
            temp = bat1
            bat1 = bat2
            bat2 = temp

            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 5
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players2[s1].score, 'ball1': players2[b1].ball,
                           'sc2': players2[s2].score, 'ball2': players2[b2].ball})
            context.update(
                {'player1': players2[bat1].playername, 'player2': players2[bat2].playername})

            players1[bs].brun = players1[bs].brun + 5
            context.update({'br': players1[bs].brun})

            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            temp = details.over * 6 - matchscore.balls
            matchscore.over2 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2+1
            return render(request, "scoring.html", context)
        elif 'six' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            matchscore.score2 = matchscore.score2 + 6
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1

            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 6
            context.update(
                {'ball1': players2[b1].ball, 'sc1': players2[s1].score})

            players1[bs].brun = players1[bs].brun + 6
            context.update({'br': players1[bs].brun})

            temp = details.over * 6 - matchscore.balls
            matchscore.over2 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1
            return render(request, "scoring.html", context)
        elif 'wicket' in request.POST:
            if matchscore.wicket2 == 9:
                matchscore.balls = matchscore.balls - 1
                matchscore.current_ball = matchscore.current_ball + 1
                matchscore.wicket2 = matchscore.wicket2 + 1
            else:
                matchscore.balls = matchscore.balls - 1
                matchscore.current_ball = matchscore.current_ball + 1
                matchscore.wicket2 = matchscore.wicket2 + 1
                temp = bat1
                temp1 = s1
                temp2 = b1
                if bat1 < bat2:
                    temp = bat2
                    bat1 = temp + 1
                    temp1 = s2
                    s1 = temp1 + 1
                    temp2 = b2
                    b1 = temp2 + 1
                else:
                    bat1 = bat1 + 1
                    b1 = b1 + 1
                    s1 = s1 + 1
            context.update({'ball1': players2[b1].ball, 'sc1': players2[s1].score,
                           'ball2': players2[b2].ball, 'sc2': players2[s2].score})

            context.update({'player1': players2[bat1].playername})
            players1[w].wicket = players1[w].wicket + 1
            context.update({'wiket': players1[w].wicket})
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            temp = details.over * 6 - matchscore.balls
            matchscore.over2 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1
            return render(request, "scoring.html", context)
        elif 'wide' in request.POST:
            matchscore.score2 = matchscore.score2 + 1
            matchscore.save()
            players1[bs].brun = players1[bs].brun + 1
            context.update({'br': players1[bs].brun})
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1
            return render(request, "extra_runs.html")
        elif 'noball' in request.POST:
            matchscore.score2 = matchscore.score2 + 1
            matchscore.save()
            players1[bs].brun = players1[bs].brun + 1
            context.update({'br': players1[bs].brun})
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1
            return render(request, "extra_runs.html")
        elif 'freehit' in request.POST:
            matchscore.balls = matchscore.balls - 1
            matchscore.current_ball = matchscore.current_ball + 1
            if matchscore.current_ball == 7:
                matchscore.current_ball = 1
            players2[b1].ball = players2[b1].ball + 1

            # players1[o].overs = players1[o].overs + (matchscore.current_ball/10)
            context.update(
                {'ball1': players2[b1].ball, 'ovr': players1[o].overs})
            temp = details.over * 6 - matchscore.balls
            matchscore.over2 = int((temp / 6)) + (temp % 6)/10
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1
            return render(request, "extra_runs.html")


def extrarun(request):
    global matchscore
    global current
    global bat1, bat2, bowl, players1, players2, b1, s1, b2, s2, o, w, bs
    context = {}
    context["dataset"] = matchscore
    context["current"] = current
    context["sc1"] = players1[s1].score
    context["sc2"] = players1[s2].score
    context["ball1"] = players1[b1].ball
    context["ball2"] = players1[b2].ball
    context["br"] = players2[bs].brun
    context["wiket"] = players2[w].wicket
    context["ovr"] = players2[o].overs
    context["player1"] = players1[bat1].playername
    context["player2"] = players1[bat2].playername
    context["player3"] = players2[bowl].playername
    if current == 1:
        context["sc1"] = players1[s1].score
        context["sc2"] = players1[s2].score
        context["ball1"] = players1[b1].ball
        context["ball2"] = players1[b2].ball
        context["br"] = players2[bs].brun
        context["wiket"] = players2[w].wicket
        context["ovr"] = players2[o].overs
        context["player1"] = players1[bat1].playername
        context["player2"] = players1[bat2].playername
        context["player3"] = players2[bowl].playername
        if 'dot' in request.POST:
            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 0

            context.update(
                {'ball1': players1[b1].ball, 'sc1': players1[s1].score})
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'one' in request.POST:
            matchscore.score1 = matchscore.score1 + 1
            temp = bat1
            bat1 = bat2
            bat2 = temp

            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 1
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players1[s1].score, 'ball1': players1[b1].ball,
                           'sc2': players1[s2].score, 'ball2': players1[b2].ball})

            context.update(
                {'player1': players1[bat1].playername, 'player2': players1[bat2].playername})

            players2[bs].brun = players2[bs].brun + 1
            context.update({'br': players2[bs].brun})

            matchscore.save()
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'two' in request.POST:
            matchscore.score1 = matchscore.score1 + 2
            matchscore.save()
            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 2

            context.update(
                {'ball1': players1[b1].ball, 'sc1': players1[s1].score})

            players2[bs].brun = players2[bs].brun + 2
            context.update({'br': players2[bs].brun})
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'three' in request.POST:
            matchscore.score1 = matchscore.score1 + 3
            temp = bat1
            bat1 = bat2
            bat2 = temp

            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 3
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players1[s1].score, 'ball1': players1[b1].ball,
                           'sc2': players1[s2].score, 'ball2': players1[b2].ball})
            context.update(
                {'player1': players1[bat1].playername, 'player2': players1[bat2].playername})
            matchscore.save()
            players2[bs].brun = players2[bs].brun + 3
            context.update({'br': players2[bs].brun})
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'four' in request.POST:
            matchscore.score1 = matchscore.score1 + 4
            matchscore.save()
            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 4

            players2[bs].brun = players2[bs].brun + 4
            context.update({'br': players2[bs].brun})
            context.update(
                {'ball1': players1[b1].ball, 'sc1': players1[s1].score})
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'five' in request.POST:
            matchscore.score1 = matchscore.score1 + 5
            temp = bat1
            bat1 = bat2
            bat2 = temp

            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 5
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players1[s1].score, 'ball1': players1[b1].ball,
                           'sc2': players1[s2].score, 'ball2': players1[b2].ball})
            context.update(
                {'player1': players1[bat1].playername, 'player2': players1[bat2].playername})
            matchscore.save()
            players2[bs].brun = players2[bs].brun + 5
            context.update({'br': players2[bs].brun})
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
        elif 'six' in request.POST:
            matchscore.score1 = matchscore.score1 + 6
            matchscore.save()
            players1[b1].ball = players1[b1].ball + 1
            players1[s1].score = players1[s1].score + 6

            context.update(
                {'ball1': players1[b1].ball, 'sc1': players1[s1].score})
            players2[bs].brun = players2[bs].brun + 6
            context.update({'br': players2[bs].brun})
            players1[s1].save()
            players1[s2].save()
            players2[bs].save()
            return render(request, "scoring.html", context)
    else:
        context["sc1"] = players2[s1].score
        context["sc2"] = players2[s2].score
        context["ball1"] = players2[b1].ball
        context["ball2"] = players2[b2].ball
        context["br"] = players1[bs].brun
        context["wiket"] = players1[w].wicket
        context["ovr"] = players1[o].overs
        context["player1"] = players2[bat1].playername
        context["player2"] = players2[bat2].playername
        context["player3"] = players1[bowl].playername
        if 'dot' in request.POST:
            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 0
            context.update(
                {'ball1': players2[b1].ball, 'sc1': players2[s1].score})
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1
            return render(request, "scoring.html", context)
        elif 'one' in request.POST:
            matchscore.score2 = matchscore.score2 + 1
            temp = bat1
            bat1 = bat2
            bat2 = temp

            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 1
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players2[s1].score, 'ball1': players2[b1].ball,
                           'sc2': players2[s2].score, 'ball2': players2[b2].ball})
            context.update(
                {'player1': players2[bat1].playername, 'player2': players2[bat2].playername})
            players1[bs].brun = players1[bs].brun + 1
            context.update({'br': players1[bs].brun})
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1
            return render(request, "scoring.html", context)
        elif 'two' in request.POST:
            matchscore.score2 = matchscore.score2 + 2
            matchscore.save()
            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 2
            context.update(
                {'ball1': players2[b1].ball, 'sc1': players2[s1].score})
            players1[bs].brun = players1[bs].brun + 2
            context.update({'br': players1[bs].brun})
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1
            return render(request, "scoring.html", context)
        elif 'three' in request.POST:
            matchscore.score2 = matchscore.score2 + 3
            temp = bat1
            bat1 = bat2
            bat2 = temp
            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 3
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players2[s1].score, 'ball1': players2[b1].ball,
                           'sc2': players2[s2].score, 'ball2': players2[b2].ball})
            context.update(
                {'player1': players2[bat1].playername, 'player2': players2[bat2].playername})

            players1[bs].brun = players1[bs].brun + 3
            context.update({'br': players1[bs].brun})

            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1
            return render(request, "scoring.html", context)
        elif 'four' in request.POST:
            matchscore.score2 = matchscore.score2 + 4
            matchscore.save()
            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 4
            context.update(
                {'ball1': players2[b1].ball, 'sc1': players2[s1].score})
            players1[bs].brun = players1[bs].brun + 4
            context.update({'br': players1[bs].brun})
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1

            return render(request, "scoring.html", context)
        elif 'five' in request.POST:
            matchscore.score2 = matchscore.score2 + 5
            temp = bat1
            bat1 = bat2
            bat2 = temp
            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 5
            temp = b1
            b1 = b2
            b2 = temp

            temp = s1
            s1 = s2
            s2 = temp
            context.update({'sc1': players2[s1].score, 'ball1': players2[b1].ball,
                           'sc2': players2[s2].score, 'ball2': players2[b2].ball})
            context.update(
                {'player1': players2[bat1].playername, 'player2': players2[bat2].playername})
            players1[bs].brun = players1[bs].brun + 5
            context.update({'br': players1[bs].brun})
            matchscore.save()
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1

            return render(request, "scoring.html", context)
        elif 'six' in request.POST:
            matchscore.score2 = matchscore.score2 + 6
            matchscore.save()
            players2[b1].ball = players2[b1].ball + 1
            players2[s1].score = players2[s1].score + 6
            context.update(
                {'ball1': players2[b1].ball, 'sc1': players2[s1].score})
            players1[bs].brun = players1[bs].brun + 6
            context.update({'br': players1[bs].brun})
            players2[s1].save()
            players2[s2].save()
            players1[bs].save()
            context["remainingrun"] = matchscore.score1 - matchscore.score2 + 1
            return render(request, "scoring.html", context)
