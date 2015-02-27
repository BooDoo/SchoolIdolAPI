from django.utils.translation import ugettext_lazy as _

LANGUAGE_CHOICES = (
    ('JP', _('Japanese')),
    ('EN', _('English')),
    ('KR', _('Korean')),
    ('CN', _('Chinese')),
    ('TW', _('Taiwanese')),
)
LANGUAGE_DICT = dict(LANGUAGE_CHOICES)

def languageToString(val):
    return LANGUAGE_DICT[val]
