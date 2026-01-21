from datetime import datetime, timedelta
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.db.models import Sum
import random
import json
from .models import Produto

class InicioView(View):
    def get(self, request):
        return render(request, 'inicio.html')
    
class BlogView(View):
    def get(self, request):
        return render(request, 'blog.html')
    
class ComprasView(View):
    def get(self, request):
        return render(request, 'compras.html')
    # Exemplo simplificado


