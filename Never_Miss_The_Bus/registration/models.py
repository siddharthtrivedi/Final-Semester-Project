from __future__ import unicode_literals

import datetime
import hashlib
import random
import re

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.db import models, transaction
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now as datetime_now
from django.utils import six

from .users import UserModel, UserModelString

SHA1_RE = re.compile('^[a-f0-9]{40}$')


class RegistrationManager(models.Manager):
    
    def activate_user(self, activation_key, get_profile=False):
        
        if SHA1_RE.search(activation_key):
            try:
                profile = self.get(activation_key=activation_key)
            except self.model.DoesNotExist:
    
    
    
                return False

            if profile.activated:
    
    
    
    
                if profile.user.is_active:
                    return profile.user
                else:
                    return False

            if not profile.activation_key_expired():
                user = profile.user
                user.is_active = True
                profile.activated = True

                with transaction.atomic():
                    user.save()
                    profile.save()

                if get_profile:
                    return profile
                else:
                    return user
        return False

    def create_inactive_user(self, site, new_user=None, send_email=True,
                             request=None, profile_info={}, **user_info):
        
        if new_user is None:
            password = user_info.pop('password')
            new_user = UserModel()(**user_info)
            new_user.set_password(password)
        new_user.is_active = False

        with transaction.atomic():
            new_user.save()
            registration_profile = self.create_profile(new_user, **profile_info)

        if send_email:
            registration_profile.send_activation_email(site, request)

        return new_user

    def create_profile(self, user, **profile_info):
        
        profile = self.model(user=user, **profile_info)

        if 'activation_key' not in profile_info:
            profile.create_new_activation_key(save=False)

        profile.save()

        return profile

    def resend_activation_mail(self, email, site, request=None):
        
        try:
            profile = self.get(user__email=email)
        except ObjectDoesNotExist:
            return False

        if profile.activated or profile.activation_key_expired():
            return False

        profile.create_new_activation_key()
        profile.send_activation_email(site, request)

        return True

    def delete_expired_users(self):
        
        for profile in self.all():
            try:
                if profile.activation_key_expired():
                    user = profile.user
                    if not user.is_active:
                        user.delete()
                        profile.delete()
            except UserModel().DoesNotExist:
                profile.delete()


@python_2_unicode_compatible
class RegistrationProfile(models.Model):
    
    user = models.OneToOneField(
        UserModelString(),
        on_delete=models.CASCADE,
        verbose_name=_('user'),
    )
    activation_key = models.CharField(_('activation key'), max_length=40)
    activated = models.BooleanField(default=False)

    objects = RegistrationManager()

    class Meta:
        verbose_name = _('registration profile')
        verbose_name_plural = _('registration profiles')

    def __str__(self):
        return "Registration information for %s" % self.user

    def create_new_activation_key(self, save=True):
        
        salt = hashlib.sha1(six.text_type(random.random())
                            .encode('ascii')).hexdigest()[:5]
        salt = salt.encode('ascii')
        user_pk = str(self.user.pk)
        if isinstance(user_pk, six.text_type):
            user_pk = user_pk.encode('utf-8')
        self.activation_key = hashlib.sha1(salt + user_pk).hexdigest()
        if save:
            self.save()
        return self.activation_key

    def activation_key_expired(self):
        
        expiration_date = datetime.timedelta(
            days=settings.ACCOUNT_ACTIVATION_DAYS)
        return (self.activated or
                (self.user.date_joined + expiration_date <= datetime_now()))
    activation_key_expired.boolean = True

    def send_activation_email(self, site, request=None):
        
        activation_email_subject = getattr(settings, 'ACTIVATION_EMAIL_SUBJECT',
                                           'registration/activation_email_subject.txt')
        activation_email_body = getattr(settings, 'ACTIVATION_EMAIL_BODY',
                                        'registration/activation_email.txt')
        activation_email_html = getattr(settings, 'ACTIVATION_EMAIL_HTML',
                                        'registration/activation_email.html')

        ctx_dict = {}
        if request is not None:
            ctx_dict = RequestContext(request, ctx_dict)
        ctx_dict.update({
            'user': self.user,
            'activation_key': self.activation_key,
            'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
            'site': site,
        })
        subject = (getattr(settings, 'REGISTRATION_EMAIL_SUBJECT_PREFIX', '') +
                   render_to_string(
                       activation_email_subject, ctx_dict))
        subject = ''.join(subject.splitlines())
        from_email = getattr(settings, 'REGISTRATION_DEFAULT_FROM_EMAIL',
                             settings.DEFAULT_FROM_EMAIL)
        message_txt = render_to_string(activation_email_body,
                                       ctx_dict)

        email_message = EmailMultiAlternatives(subject, message_txt,
                                               from_email, [self.user.email])

        if getattr(settings, 'REGISTRATION_EMAIL_HTML', True):
            try:
                message_html = render_to_string(
                    activation_email_html, ctx_dict)
            except TemplateDoesNotExist:
                pass
            else:
                email_message.attach_alternative(message_html, 'text/html')

        email_message.send()
