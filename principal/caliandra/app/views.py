from datetime import datetime, timedelta
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
import random
import json

class InicioView(View):
    def get(self, request):
        return render(request, 'inicio.html')
