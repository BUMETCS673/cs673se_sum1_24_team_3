# code/local_testing_adrian_dnu/myapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from surveys.models import Survey, Response, Question
from .forms import CustomUserCreationForm, LoginForm, ResponseFormSet, modelformset_factory
from django import forms

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('dashboard'))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    user = request.user
    available_surveys = Survey.objects.exclude(response__user=user)
    taken_surveys = Survey.objects.filter(response__user=user).distinct()
    return render(request, 'dashboard.html', {
        'available_surveys': available_surveys,
        'taken_surveys': taken_surveys
    })

@login_required
def take_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = Question.objects.filter(survey=survey)
    ResponseFormSet = modelformset_factory(Response, fields=('answer',), extra=len(questions), widgets={'answer': forms.RadioSelect})

    if request.method == 'POST':
        formset = ResponseFormSet(request.POST)
        if formset.is_valid():
            for form, question in zip(formset, questions):
                response = form.save(commit=False)
                response.user = request.user
                response.survey = survey
                response.question = question
                response.save()
            return redirect('dashboard')
        else:
            print("Formset is not valid:")
            for form in formset:
                print(form.errors)
            print("Posted data:", request.POST)
    else:
        initial_data = [{'answer': None} for _ in questions]
        formset = ResponseFormSet(queryset=Response.objects.none(), initial=initial_data)

    question_formset = zip(questions, formset)

    return render(request, 'take_survey.html', {'survey': survey, 'formset': formset, 'question_formset': question_formset})

@login_required
def view_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = Question.objects.filter(survey=survey)
    responses = Response.objects.filter(user=request.user, survey=survey)
    response_dict = {response.question.id: response.get_answer_display() for response in responses}
    questions_and_responses = [{'question': question, 'answer': response_dict.get(question.id, "No answer")} for question in questions]
    return render(request, 'view_survey.html', {'survey': survey, 'questions_and_responses': questions_and_responses})
