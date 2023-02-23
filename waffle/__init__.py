from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured

from waffle.utils import get_setting
from django.apps import apps as django_apps
from django.contrib.sites.shortcuts import get_current_site

VERSION = (0, 18, 0)
__version__ = '.'.join(map(str, VERSION))
default_app_config = 'waffle.apps.WaffleConfig'


def flag_is_active(request, flag_name):
    current_site = get_current_site(request)
    flag = get_waffle_flag_model().get(name=flag_name, site=current_site)
    return flag.is_active(request)


def switch_is_active(request, switch_name):
    from .models import Switch

    current_site = get_current_site(request)
    switch = Switch.get(name=switch_name, site=current_site)
    return switch.is_active()


def sample_is_active(request, sample_name):
    from .models import Sample

    current_site = get_current_site(request)
    sample = Sample.get(name=sample_name, site=current_site)
    return sample.is_active()


def get_waffle_flag_model():
    """
    Returns the waffle Flag model that is active in this project.
    """
    # Add backwards compatibility by not requiring adding of WAFFLE_FLAG_MODEL
    # for everyone who upgrades.
    # At some point it would be helpful to require this to be defined explicitly,
    # but no for now, to remove pain form upgrading.
    flag_model_name = get_setting('FLAG_MODEL', 'waffle.Flag')

    try:
        return django_apps.get_model(flag_model_name)
    except ValueError:
        raise ImproperlyConfigured("WAFFLE_FLAG_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "WAFFLE_FLAG_MODEL refers to model '{}' that has not been installed".format(
                flag_model_name
            )
        )
