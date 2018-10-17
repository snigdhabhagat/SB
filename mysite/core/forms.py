from __future__ import unicode_literals

from django import forms


class SubstationIncidentReport_General(forms.Form):
    substation_name = forms.CharField(max_length=100)
    t_inc_report = forms.TimeField()
    employee_name = forms.CharField(max_length=100)
    employee_id = forms.CharField(max_length=50)
    inc_observation = forms.CharField(max_length=32)  # =obstypes)

    weather_category = forms.CharField(max_length=16)  # =wtypes)
    humidity = forms.IntegerField()
    avg_temp = forms.IntegerField()


class SubstationIncidentReport_PDO(forms.Form):
    devicetypes = ("circuit_breaker", "auto_recloser", "fuse")
    device_type = forms.CharField(max_length=20)  # =devicetypes)
    device_id = forms.CharField(max_length=20)
    protect_type = forms.CharField(max_length=64)
    t_inc = forms.TimeField()
    element_type = forms.CharField(max_length=64)
    element_id = forms.CharField(max_length=64)
    fault_indicator = forms.CharField(max_length=64)
    possible_cause_type = forms.CharField(max_length=64)
    comments = forms.CharField(max_length=8000)


class CustomerIncidentReport_General(forms.Form):
    # slide 7
    consumer_type = forms.CharField(max_length=50)
    consumer_id = forms.CharField(max_length=50)
    consumer_address = forms.CharField(max_length=250)
    t_inc_report = forms.TimeField()
    consumer_inc_type = forms.CharField(max_length=50)

    weather_category = forms.CharField(max_length=16)  # =wtypes)
    humidity = forms.IntegerField()
    avg_temp = forms.IntegerField()


class CustomerIncidentReport_Type1(forms.Form):
    # common in slide 8, 9
    incident_type = forms.CharField(max_length=64)
    t_inc = forms.TimeField()
    phases_affected = forms.CharField(max_length=64)
    damage_observed = forms.CharField(max_length=64)

    device_type = forms.CharField(max_length=64)
    device_operation = forms.CharField(max_length=64)

    # slide 8
    answer = forms.CharField(max_length=8)
    answer_attempt = forms.CharField(max_length=8)
    final_status = forms.CharField(max_length=64)
    answer_response = forms.CharField(max_length=64)


class CustomerIncidentReport_Type2(forms.Form):
    # common in slide 8, 9
    incident_type = forms.CharField(max_length=64)
    t_inc = forms.TimeField()
    phases_affected = forms.CharField(max_length=64)
    damage_observed = forms.CharField(max_length=64)

    device_type = forms.CharField(max_length=64)
    device_operation = forms.CharField(max_length=64)
    # slide 9
    cause_of_incident = forms.CharField(max_length=64)
    damaged_equipment = forms.CharField(max_length=64)
    damage_type = forms.CharField(max_length=64)
    meter_response = forms.CharField(max_length=8)


class PMCIncidentReport_General(forms.Form):
    # slide 10
    employee_name = forms.CharField(max_length=64)
    employee_id = forms.CharField(max_length=64)
    t_inc_report = forms.TimeField()
    monitor_type = forms.CharField(max_length=64)
    inc_observation = forms.CharField(max_length=64)

    weather_category = forms.CharField(max_length=16)  # =wtypes)
    humidity = forms.IntegerField()
    avg_temp = forms.IntegerField()


class PMCIncidentReport_PDO(forms.Form):
    # slide 11
    device_type = forms.CharField(max_length=64)
    device_id = forms.CharField(max_length=64)
    protect_type = forms.CharField(max_length=64)
    t_inc = forms.TimeField()
    element_type = forms.CharField(max_length=64)
    element_id = forms.CharField(max_length=64)
    fault_indicator = forms.CharField(max_length=64)
    possible_cause_type = forms.CharField(max_length=64)
    comms_failure = forms.CharField(max_length=64)
    comms_failure_type = forms.CharField(max_length=64)
