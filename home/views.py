from django.shortcuts import render, redirect
from .models import Questions, CustomerFeedback, CustomerResponse, Options

def surveys(request):

    feedback = CustomerFeedback.objects.all()
    return render(request, 'surveys.html', {'feedbacks': feedback})

def survey_view(request, id):
    try:
        feedback = CustomerFeedback.objects.get(id=id)
        questions = feedback.question.all()
    except CustomerFeedback.DoesNotExist:
        return render(request, '404.html')  # Or a more specific error page

    if request.method == 'POST':
        for question in questions:
            response_text = request.POST.get(f"response_{question.id}")
            selected_option_ids = request.POST.getlist(f"options_{question.id}")

            response = CustomerResponse.objects.create(
                feedback=feedback,
                question=question,
                response_text=response_text if question.question_type in ["Text", "BigText"] else None
            )
            
            if selected_option_ids:
                selected_options = Options.objects.filter(id__in=selected_option_ids)
                response.selected_option.set(selected_options)
        
        return redirect('thank_you', id=feedback.id)
    
    return render(request, 'survey.html', {'questions': questions, 'feedback': feedback})


def thank_you(request, id):
    return render(request, 'thank_you.html', {'id': id})

def survey_results(request, id):
    try:
        feedback = CustomerFeedback.objects.get(id=id)
        questions = feedback.question.all()
    except CustomerFeedback.DoesNotExist:
        return render(request, '404.html')  # Or a more specific error page

    data = []
    for question in questions:
        responses = CustomerResponse.objects.filter(question=question, feedback=feedback)
        if question.question_type in ['Radio', 'Checkbox']:
            options = question.option.all()
            option_counts = {option.option_name: responses.filter(selected_option=option).count() for option in options}
            data.append({
                'question': question.question,
                'labels': list(option_counts.keys()),
                'values': list(option_counts.values()),
            })
    
    return render(request, 'results.html', {'data': data, 'feedback': feedback})

def all_results(request):
    feedbacks = CustomerFeedback.objects.all()
    return render(request, 'all_results.html', {'feedbacks': feedbacks})



