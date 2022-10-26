from django.shortcuts import redirect, render
from .models import *
from django.views import generic
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib.humanize.templatetags.humanize import naturalday
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User    = get_user_model()

# Create your views here.

class MembersView(generic.TemplateView):
    template_name       = "breakthrough/members.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/auth/login/')
        return super(MembersView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):

        context = super(MembersView, self).get_context_data(**kwargs)
        cur_member               = Member.objects.get(user__id=self.request.user.id)
        context['cur_member']    = cur_member
        context['members']       = Member.objects.all().order_by('-pk')
        context['color_group']   = Member.objects.filter(color=cur_member.color).order_by('-pk')
        
        
        return context