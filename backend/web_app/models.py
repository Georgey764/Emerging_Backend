# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class BatteryData(models.Model):
    station_num = models.ForeignKey('MesonetStations', models.DO_NOTHING, db_column='station_num', blank=True, null=True)
    timestamp = models.DateTimeField(db_column='TIMESTAMP', blank=True, null=True)
    batteryvoltage = models.DecimalField(db_column='BatteryVoltage', max_digits=10, decimal_places=2, blank=True, null=True)
    batterycurrent = models.DecimalField(db_column='BatteryCurrent', max_digits=10, decimal_places=2, blank=True, null=True) 
    loadcurrent = models.DecimalField(db_column='LoadCurrent', max_digits=10, decimal_places=2, blank=True, null=True) 
    chargeinputvoltage = models.DecimalField(db_column='ChargeInputVoltage', max_digits=10, decimal_places=2, blank=True, null=True)
    chargeinputcurrent = models.DecimalField(db_column='ChargeInputCurrent', max_digits=10, decimal_places=2, blank=True, null=True)
    chargetemp = models.DecimalField(db_column='ChargeTemp', max_digits=10, decimal_places=2, blank=True, null=True)
    chg_state = models.CharField(db_column='Chg_State', max_length=50, blank=True, null=True)
    chg_source = models.CharField(db_column='Chg_Source', max_length=50, blank=True, null=True) 
    ck_batt = models.CharField(db_column='Ck_Batt', max_length=50, blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'battery_data'


class MesonetStations(models.Model):
    station_number = models.IntegerField(primary_key=True)
    internal_station_id = models.CharField(unique=True, max_length=10, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    elevation_ft = models.IntegerField(blank=True, null=True)
    physical_location = models.CharField(max_length=255, blank=True, null=True)
    parish = models.CharField(max_length=100, blank=True, null=True)
    nws_office = models.CharField(max_length=100, blank=True, null=True)
    install_date = models.DateField(blank=True, null=True)
    type_of_site = models.CharField(max_length=100, blank=True, null=True)
    surroundings = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesonet_stations'


class SoilData(models.Model):
    station_num = models.ForeignKey(MesonetStations, models.DO_NOTHING, db_column='station_num', blank=True, null=True)
    timestamp = models.DateTimeField(db_column='TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    vwc_5cm_avg = models.DecimalField(db_column='VWC_5cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ka_5cm_avg = models.DecimalField(db_column='Ka_5cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soiltmpf_5cm_avg = models.DecimalField(db_column='SoilTmpF_5cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulkec_5cm_avg = models.DecimalField(db_column='BulkEC_5cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vwc_10cm_avg = models.DecimalField(db_column='VWC_10cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ka_10cm_avg = models.DecimalField(db_column='Ka_10cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soiltmpf_10cm_avg = models.DecimalField(db_column='SoilTmpF_10cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulkec_10cm_avg = models.DecimalField(db_column='BulkEC_10cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vwc_20cm_avg = models.DecimalField(db_column='VWC_20cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ka_20cm_avg = models.DecimalField(db_column='Ka_20cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soiltmpf_20cm_avg = models.DecimalField(db_column='SoilTmpF_20cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulkec_20cm_avg = models.DecimalField(db_column='BulkEC_20cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vwc_30cm_avg = models.DecimalField(db_column='VWC_30cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ka_30cm_avg = models.DecimalField(db_column='Ka_30cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soiltmpf_30cm_avg = models.DecimalField(db_column='SoilTmpF_30cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulkec_30cm_avg = models.DecimalField(db_column='BulkEC_30cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vwc_40cm_avg = models.DecimalField(db_column='VWC_40cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ka_40cm_avg = models.DecimalField(db_column='Ka_40cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soiltmpf_40cm_avg = models.DecimalField(db_column='SoilTmpF_40cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulkec_40cm_avg = models.DecimalField(db_column='BulkEC_40cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vwc_50cm_avg = models.DecimalField(db_column='VWC_50cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ka_50cm_avg = models.DecimalField(db_column='Ka_50cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soiltmpf_50cm_avg = models.DecimalField(db_column='SoilTmpF_50cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulkec_50cm_avg = models.DecimalField(db_column='BulkEC_50cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vwc_60cm_avg = models.DecimalField(db_column='VWC_60cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ka_60cm_avg = models.DecimalField(db_column='Ka_60cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soiltmpf_60cm_avg = models.DecimalField(db_column='SoilTmpF_60cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulkec_60cm_avg = models.DecimalField(db_column='BulkEC_60cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vwc_75cm_avg = models.DecimalField(db_column='VWC_75cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ka_75cm_avg = models.DecimalField(db_column='Ka_75cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soiltmpf_75cm_avg = models.DecimalField(db_column='SoilTmpF_75cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulkec_75cm_avg = models.DecimalField(db_column='BulkEC_75cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vwc_100cm_avg = models.DecimalField(db_column='VWC_100cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ka_100cm_avg = models.DecimalField(db_column='Ka_100cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    soiltmpf_100cm_avg = models.DecimalField(db_column='SoilTmpF_100cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bulkec_100cm_avg = models.DecimalField(db_column='BulkEC_100cm_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'soil_data'


class TemperaturePressure(models.Model):
    station_num = models.ForeignKey(MesonetStations, models.DO_NOTHING, db_column='station_num', blank=True, null=True)
    timestamp = models.DateTimeField(db_column='TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    t109_30ft_f_avg = models.DecimalField(db_column='T109_30ft_F_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t109_10ft_f_avg = models.DecimalField(db_column='T109_10ft_F_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    absbaro_inhg_avg = models.DecimalField(db_column='AbsBaro_inHg_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sealvlbaro_inhg_avg = models.DecimalField(db_column='SeaLvlBaro_inHg_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    heatindxtmpf_avg = models.DecimalField(db_column='HeatIndxTmpF_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    windchilltmpf_avg = models.DecimalField(db_column='WindChillTmpF_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temperature_pressure'


class WeatherConditions(models.Model):
    station_num = models.ForeignKey(MesonetStations, models.DO_NOTHING, db_column='station_num', blank=True, null=True)
    timestamp = models.DateTimeField(db_column='TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    record = models.IntegerField(db_column='RECORD', blank=True, null=True)  # Field name made lowercase.
    battv_avg = models.DecimalField(db_column='BattV_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ws_30ft_mph_avg = models.DecimalField(db_column='WS_30ft_mph_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ws_30ft_mph_max = models.DecimalField(db_column='WS_30ft_mph_Max', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    winddir_30ft_d1_wvt = models.DecimalField(db_column='WindDir_30ft_D1_WVT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    winddir_30ft_sd1_wvt = models.DecimalField(db_column='WindDir_30ft_SD1_WVT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ws_10ft_mph_avg = models.DecimalField(db_column='WS_10ft_mph_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ws_10ft_mph_max = models.DecimalField(db_column='WS_10ft_mph_Max', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    winddir_10ft_d1_wvt = models.DecimalField(db_column='WindDir_10ft_D1_WVT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    winddir_10ft_sd1_wvt = models.DecimalField(db_column='WindDir_10ft_SD1_WVT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ws_sonic_mph_avg = models.DecimalField(db_column='WS_Sonic_mph_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ws_sonic_mph_max = models.DecimalField(db_column='WS_Sonic_mph_Max', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    winddir_sonic_d1_wvt = models.DecimalField(db_column='WindDir_Sonic_D1_WVT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    winddir_sonic_sd1_wvt = models.DecimalField(db_column='WindDir_Sonic_SD1_WVT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    airtf_avg = models.DecimalField(db_column='AirTF_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rh_avg = models.DecimalField(db_column='RH_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    slrw_avg = models.DecimalField(db_column='SlrW_Avg', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    slrmj_tot = models.DecimalField(db_column='SlrMJ_Tot', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dewptf = models.DecimalField(db_column='DewPtF', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rainsincemidnight = models.DecimalField(db_column='RainSinceMidnight', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rv_pre_accu_tot = models.DecimalField(db_column='RV_Pre_Accu_Tot', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rv_tips_tot = models.DecimalField(db_column='RV_Tips_Tot', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rv_tot_pre_accu = models.DecimalField(db_column='RV_Tot_Pre_Accu', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rv_avg_pre_int_max = models.DecimalField(db_column='RV_Avg_Pre_Int_Max', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rv_max_pre_int_max = models.DecimalField(db_column='RV_Max_Pre_Int_Max', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weather_conditions'
