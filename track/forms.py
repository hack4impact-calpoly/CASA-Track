from django import forms
from .models import TrackingForm


class TrackingFormForm(forms.ModelForm):
    class Meta:
        model = TrackingForm
        fields = ('advocate', 'advocate_email', 'supervisor', 'child_name', 'month', 'hours_spent', 'hours_education',
                  'hours_on_case', 'the_voice','continuing_edu', 'miles_driven', 'face_advocate_sv_hours',
                  'phone_advocate_sv', 'casa_volunteering', 'other_volunteering', 'esignature', 'signature_date', )

class PartialTrackingFormForm(forms.ModelForm):
    class Meta:
        model = TrackingForm
        fields = ('supervisor_signature', 'supervisor_signature_date')


                  
