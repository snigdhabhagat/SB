from __future__ import unicode_literals

from django.db import models


class SubstationIncidentReport(models.Model):
    substation_name = models.CharField(max_length=100)
    t_inc_report = models.TimeField(auto_now_add=True)
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    obstypes = ("Protective_Device_Operation", "Network_Element_Failure")
    inc_onservation = models.CharField(max_length=32)  # =obstypes)

    wtypes = ("foggy", "rainy", "sunny", "cloudy")
    weather_category = models.CharField(max_length=16)  # =wtypes)
    humidity = models.IntegerField()
    avg_temp = models.IntegerField()

    devicetypes = ("circuit_breaker", "auto_recloser", "fuse")
    device_type = models.CharField(max_length=20)  # =devicetypes, null=True, default=None)
    device_id = models.CharField(max_length=20, null=True, default=None)
    protect_type = models.CharField(max_length=64, null=True, default=None)
    t_inc = models.TimeField(null=True, default=None)
    element_type = models.CharField(max_length=64, null=True, default=None)
    element_id = models.CharField(max_length=64, null=True, default=None)
    fault_indicator = models.CharField(max_length=64, null=True, default=None)
    possible_cause_type = models.CharField(max_length=64, null=True, default=None)


class CustomerIncidentReport(models.Model):
    # slide 7
    consumer_type = models.CharField(max_length=50)
    consumer_id = models.CharField(max_length=50)
    consumer_address = models.CharField(max_length=250)
    t_inc_report = models.TimeField()
    consumer_inc_type = models.CharField(max_length=50)

    wtypes = ("foggy", "rainy", "sunny", "cloudy")
    weather_category = models.CharField(max_length=16)  # =wtypes)
    humidity = models.IntegerField()
    avg_temp = models.IntegerField()

    # common in slide 8, 9
    incident_type = models.CharField(max_length=64, null=True, default=None)
    t_inc = models.TimeField()
    phases_affected = models.CharField(max_length=64, null=True, default=None)
    damage_observed = models.CharField(max_length=64, null=True)

    device_type = models.CharField(max_length=64, null=True, default=None)
    device_operation = models.CharField(max_length=64, null=True, default=None)

    # slide 8
    answer = models.CharField(max_length=8, null=True, default=None)
    answer_attempt = models.CharField(max_length=8, null=True, default=None)
    final_status = models.CharField(max_length=64, null=True, default=None)
    answer_response = models.CharField(max_length=64, null=True, default=None)

    # slide 9
    cause_of_incident = models.CharField(max_length=64, null=True, default=None)
    damaged_equipment = models.CharField(max_length=64, null=True, default=None)
    damage_type = models.CharField(max_length=64, null=True, default=None)
    meter_response = models.CharField(max_length=8, null=True, default=None)


class PMCIncidentReport(models.Model):
    # slide 10
    employee_name = models.CharField(max_length=64)
    employee_id = models.CharField(max_length=64)
    t_inc_report = models.TimeField()
    monitor_type = models.CharField(max_length=64)
    inc_observation = models.CharField(max_length=64)

    wtypes = ("foggy", "rainy", "sunny", "cloudy")
    weather_category = models.CharField(max_length=16)  # =wtypes)
    humidity = models.IntegerField()
    avg_temp = models.IntegerField()

    # slide 11
    device_type = models.CharField(max_length=64, null=True, default=None)
    device_id = models.CharField(max_length=64, null=True, default=None)
    protect_type = models.CharField(max_length=64, null=True, default=None)
    t_inc = models.TimeField(null=True, default=None)
    element_type = models.CharField(max_length=64, null=True, default=None)
    element_id = models.CharField(max_length=64, null=True, default=None)
    fault_indicator = models.CharField(max_length=64, null=True, default=None)
    possible_cause_type = models.CharField(max_length=64, null=True, default=None)
    comms_failure = models.CharField(max_length=64, null=True, default=None)
    comms_failure_type = models.CharField(max_length=64, null=True, default=None)






    

