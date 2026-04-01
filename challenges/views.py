from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect 

# Create your views here.

# def january(request):
#     return HttpResponse("heyy")

# def february(request):
#     return HttpResponse("im okay")

# def march(request):
#     return HttpResponse("im gonna play the game")
monthly_challenge = {
    "january": "Learn django at least for 20 min a day ",
    "february": "im following duite for this month",
    "march": "This month have to learn tech skills",
    "april": "Learn django at least for 20 min a day",
    "may": "Learn django at least for 20 min a day",
    "april": "Learn django at least for 20 min a day",
    "may":"Eat no meat for entire month",
    "june":"Learn django at least for 20 min a day",
    "july":"This month have to learn tech skills",
    "august":"Eat no meat for entire month",
    "september":"Learn django at least for 20 min a day",
    "october":"This month have to learn tech skills",
    "november":"Eat no meat for entire month",
    "december":"Learn django at least for 20 min a day"
}

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())

    if month > len(months):
        return HttpResponseNotFound("not found")

    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenge/" + redirect_month)


def monthly_challenges(request, month):
    try:
        month_text = monthly_challenge[month]
    except:
        return HttpResponseNotFound("This month is not supported")    
    return HttpResponse(month_text)
    
