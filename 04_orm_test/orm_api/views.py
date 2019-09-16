from django.shortcuts import render, redirect 
from django.http import HttpResponse, JsonResponse
from orm_api.models import Branch, Employee


def index(request):
    branches = Branch.objects.all()
    totals = {}
    for branch in branches:
        totals[branch.city] = branch.payroll()
    return JsonResponse({"Total Payouts by Location": totals})
