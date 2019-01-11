# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from account.forms import UserForm


def home(request):
    return render(request, 'home.html')


def profile_update(request):
    data = dict()
    user = request.user

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['html_user_profile'] = render_to_string('user_profile.html', {
                'user': user
            })
        else:
            data['form_is_valid'] = False
    else:
        form = UserForm(instance=user)

    context = {'form': form}
    data['html_form'] = render_to_string('partial_Edit.html', context, request=request)
    return JsonResponse(data)
