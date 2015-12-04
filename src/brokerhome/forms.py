from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import BrokerRating, Locality, City, BrokerLocale
from django.utils.translation import ugettext,ugettext_lazy as _



class RatingForm(ModelForm):

    class Meta:
        model = BrokerRating
        fields = ['rating', 'review']
        widgets = {
            'review': Textarea(attrs={'cols': 60, 'rows': 10}),
            'rating': TextInput(attrs={'class': 'rating', 'id': 'input-21e', 'data-size': 'xs',
                                       'data-show-clear': 'false', 'data-show-caption': 'false'})
        }


class LocalityFilterForm(forms.Form):

	city = forms.ModelChoiceField(
        label=_("City"),
        required=False,
        queryset=City.objects.all(),
    )

class BrokerFilterForm(forms.Form):
	locale = forms.ModelChoiceField(
			label = _("Locality"),
			required=False,
			queryset=Locality.objects.all()

		)

			



