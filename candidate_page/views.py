from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Candidate, Position, Vresults
from django.utils import timezone
from .forms import CreateNewCandidate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.urls import reverse
from django.template import loader
import datetime

User = get_user_model()

# Create your views here.
def main(request):
    return render(request, 'voter_account/main.html')


@login_required(login_url='/voter_account/signup')
def home(request):
    candidates = Candidate.objects
    return render(request, 'candidate_page/home.html', {'candidates': candidates})


@login_required(login_url='/voter_account/signup')
def create(request):
    reglimit = datetime.date(2021, 7, 10)
    tday = datetime.date.today()
    if tday >= reglimit:
        messages.warning(request, 'Sorry, the registration period has ended!')
        return redirect('regend')
    else:
        form = CreateNewCandidate()
        if Candidate.objects.filter(account=request.user).exists():
            messages.warning(request, 'You have already registered for a position!')
            return render(request, 'candidate_page/create.html', {'form':form})
        else:
            if request.method == 'POST':
                form = CreateNewCandidate(request.POST or None, request.FILES or None)
                if form.is_valid():
                     instance = form.save(commit=False)
                     instance.account = request.user
                     instance.save()
                     messages.success(request, 'You have successfully registered as a candidate!')
                     return redirect('/candidate_page/' + str(instance.id))
                else:
                     return render(request, 'candidate_page/create.html', {'form':form, 'error': 'All fields are required'})

            else:
                 form = CreateNewCandidate()
            return render(request, 'candidate_page/create.html', {'form':form})


@login_required(login_url='/voter_account/signup')
def detail(request, instance_id):
    candidate = get_object_or_404(Candidate, pk=instance_id)
    return render(request, 'candidate_page/detail.html', {'candidate': candidate})


@login_required(login_url='/voter_account/signup')
def candidates(request):
    candidates = Candidate.objects
    return render(request, 'candidate_page/candidate.html', {'candidates': candidates})


@login_required(login_url='/voter_account/signup')
def regend(request):
    return render(request, 'candidate_page/regend.html')


@login_required(login_url='/voter_account/signup')
def votepage(request):
    votestart = datetime.date(2020, 7, 21 )
    voteend = datetime.date(2021, 7, 28 )
    tday = datetime.date.today()
    if tday >= votestart and tday <=voteend:
        position_list = Position.objects
        return render(request, 'candidate_page/votepage.html', {'position_list':position_list})
    elif tday <= votestart:
        messages.warning(request, 'Sorry, voting will start on 2021/07/18 !')
        return redirect('regend')
    else:
        messages.warning(request, 'Sorry, the voting period has ended !')
        return redirect('regend')


@login_required(login_url='/voter_account/signup')
def votedetail(request, position_id):
    try:
        position = Position.objects.get(pk=position_id)
    except Position.DoesNotExist:
        raise Http404('Position does not exist')
    return render(request, 'candidate_page/votedetail.html', {'position':position})


@login_required(login_url='/voter_account/signup')
def vote(request, position_id):
    sposition = get_object_or_404(Position, pk=position_id)
    if request.method == "POST":
        voter = Vresults.objects.get_or_create(account=request.user, position=sposition)[0]
        if voter.status == False:
            try:
                selected_candidate = sposition.candidate_set.get(pk=request.POST['candidate'])
            except (KeyError, Candidate.DoesNotExist):
                messages.warning(request, 'You did not select a candidate')
                return render(request, 'candidate_page/votedetail.html', {'position':sposition})
            else:
                selected_candidate.total_vote += 1
                selected_candidate.save()
                voter.status = True
                voter.save()
                return HttpResponseRedirect(reverse('detailresults', args=(position_id,)))
        else:
            messages.warning(request, 'You already voted for this position!')
            return render(request, 'candidate_page/votedetail.html', {'position':sposition})
    else:
        return render(request, 'candidate_page/votedetail.html', {'position':sposition})


@login_required(login_url='/voter_account/signup')
def detailresults(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    return render(request, 'candidate_page/detailresults.html', {'position': position})


@login_required(login_url='/voter_account/signup')
def results(request):
    candidates = Candidate.objects.all().order_by('position','-total_vote')
    return render(request, 'candidate_page/results.html', {'candidates': candidates})
