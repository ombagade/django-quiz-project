
from django.shortcuts import render, redirect
from django.contrib import messages


def submit(request):
    if request.method == 'POST':
        answers = request.POST.dict()

        request.session['submitted_answers'] = answers
        messages.success(request, 'Your exam has been submitted successfully!')

        return redirect('show_exam_result')

    return render(request, 'submit.html')


def show_exam_result(request):
    answers = request.session.get('submitted_answers', {})

    context = {
        'answers': answers,
        'message': 'Your exam submission is successful.',
    }

    return render(request, 'show_exam_result.html', context)
