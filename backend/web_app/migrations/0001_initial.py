# Generated by Django 5.1.7 on 2025-03-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_column='TIMESTAMP', null=True)),
                ('batteryvoltage', models.DecimalField(blank=True, db_column='BatteryVoltage', decimal_places=2, max_digits=10, null=True)),
                ('batterycurrent', models.DecimalField(blank=True, db_column='BatteryCurrent', decimal_places=2, max_digits=10, null=True)),
                ('loadcurrent', models.DecimalField(blank=True, db_column='LoadCurrent', decimal_places=2, max_digits=10, null=True)),
                ('chargeinputvoltage', models.DecimalField(blank=True, db_column='ChargeInputVoltage', decimal_places=2, max_digits=10, null=True)),
                ('chargeinputcurrent', models.DecimalField(blank=True, db_column='ChargeInputCurrent', decimal_places=2, max_digits=10, null=True)),
                ('chargetemp', models.DecimalField(blank=True, db_column='ChargeTemp', decimal_places=2, max_digits=10, null=True)),
                ('chg_state', models.CharField(blank=True, db_column='Chg_State', max_length=50, null=True)),
                ('chg_source', models.CharField(blank=True, db_column='Chg_Source', max_length=50, null=True)),
                ('ck_batt', models.CharField(blank=True, db_column='Ck_Batt', max_length=50, null=True)),
            ],
            options={
                'db_table': 'battery_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MesonetStations',
            fields=[
                ('station_number', models.IntegerField(primary_key=True, serialize=False)),
                ('internal_station_id', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('elevation_ft', models.IntegerField(blank=True, null=True)),
                ('physical_location', models.CharField(blank=True, max_length=255, null=True)),
                ('parish', models.CharField(blank=True, max_length=100, null=True)),
                ('nws_office', models.CharField(blank=True, max_length=100, null=True)),
                ('install_date', models.DateField(blank=True, null=True)),
                ('type_of_site', models.CharField(blank=True, max_length=100, null=True)),
                ('surroundings', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'mesonet_stations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SoilData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_column='TIMESTAMP', null=True)),
                ('vwc_5cm_avg', models.DecimalField(blank=True, db_column='VWC_5cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ka_5cm_avg', models.DecimalField(blank=True, db_column='Ka_5cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('soiltmpf_5cm_avg', models.DecimalField(blank=True, db_column='SoilTmpF_5cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('bulkec_5cm_avg', models.DecimalField(blank=True, db_column='BulkEC_5cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('vwc_10cm_avg', models.DecimalField(blank=True, db_column='VWC_10cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ka_10cm_avg', models.DecimalField(blank=True, db_column='Ka_10cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('soiltmpf_10cm_avg', models.DecimalField(blank=True, db_column='SoilTmpF_10cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('bulkec_10cm_avg', models.DecimalField(blank=True, db_column='BulkEC_10cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('vwc_20cm_avg', models.DecimalField(blank=True, db_column='VWC_20cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ka_20cm_avg', models.DecimalField(blank=True, db_column='Ka_20cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('soiltmpf_20cm_avg', models.DecimalField(blank=True, db_column='SoilTmpF_20cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('bulkec_20cm_avg', models.DecimalField(blank=True, db_column='BulkEC_20cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('vwc_30cm_avg', models.DecimalField(blank=True, db_column='VWC_30cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ka_30cm_avg', models.DecimalField(blank=True, db_column='Ka_30cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('soiltmpf_30cm_avg', models.DecimalField(blank=True, db_column='SoilTmpF_30cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('bulkec_30cm_avg', models.DecimalField(blank=True, db_column='BulkEC_30cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('vwc_40cm_avg', models.DecimalField(blank=True, db_column='VWC_40cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ka_40cm_avg', models.DecimalField(blank=True, db_column='Ka_40cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('soiltmpf_40cm_avg', models.DecimalField(blank=True, db_column='SoilTmpF_40cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('bulkec_40cm_avg', models.DecimalField(blank=True, db_column='BulkEC_40cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('vwc_50cm_avg', models.DecimalField(blank=True, db_column='VWC_50cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ka_50cm_avg', models.DecimalField(blank=True, db_column='Ka_50cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('soiltmpf_50cm_avg', models.DecimalField(blank=True, db_column='SoilTmpF_50cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('bulkec_50cm_avg', models.DecimalField(blank=True, db_column='BulkEC_50cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('vwc_60cm_avg', models.DecimalField(blank=True, db_column='VWC_60cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ka_60cm_avg', models.DecimalField(blank=True, db_column='Ka_60cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('soiltmpf_60cm_avg', models.DecimalField(blank=True, db_column='SoilTmpF_60cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('bulkec_60cm_avg', models.DecimalField(blank=True, db_column='BulkEC_60cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('vwc_75cm_avg', models.DecimalField(blank=True, db_column='VWC_75cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ka_75cm_avg', models.DecimalField(blank=True, db_column='Ka_75cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('soiltmpf_75cm_avg', models.DecimalField(blank=True, db_column='SoilTmpF_75cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('bulkec_75cm_avg', models.DecimalField(blank=True, db_column='BulkEC_75cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('vwc_100cm_avg', models.DecimalField(blank=True, db_column='VWC_100cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ka_100cm_avg', models.DecimalField(blank=True, db_column='Ka_100cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('soiltmpf_100cm_avg', models.DecimalField(blank=True, db_column='SoilTmpF_100cm_Avg', decimal_places=2, max_digits=10, null=True)),
                ('bulkec_100cm_avg', models.DecimalField(blank=True, db_column='BulkEC_100cm_Avg', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'soil_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TemperaturePressure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_column='TIMESTAMP', null=True)),
                ('t109_30ft_f_avg', models.DecimalField(blank=True, db_column='T109_30ft_F_Avg', decimal_places=2, max_digits=10, null=True)),
                ('t109_10ft_f_avg', models.DecimalField(blank=True, db_column='T109_10ft_F_Avg', decimal_places=2, max_digits=10, null=True)),
                ('absbaro_inhg_avg', models.DecimalField(blank=True, db_column='AbsBaro_inHg_Avg', decimal_places=2, max_digits=10, null=True)),
                ('sealvlbaro_inhg_avg', models.DecimalField(blank=True, db_column='SeaLvlBaro_inHg_Avg', decimal_places=2, max_digits=10, null=True)),
                ('heatindxtmpf_avg', models.DecimalField(blank=True, db_column='HeatIndxTmpF_Avg', decimal_places=2, max_digits=10, null=True)),
                ('windchilltmpf_avg', models.DecimalField(blank=True, db_column='WindChillTmpF_Avg', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'temperature_pressure',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeatherConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_column='TIMESTAMP', null=True)),
                ('record', models.IntegerField(blank=True, db_column='RECORD', null=True)),
                ('battv_avg', models.DecimalField(blank=True, db_column='BattV_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ws_30ft_mph_avg', models.DecimalField(blank=True, db_column='WS_30ft_mph_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ws_30ft_mph_max', models.DecimalField(blank=True, db_column='WS_30ft_mph_Max', decimal_places=2, max_digits=10, null=True)),
                ('winddir_30ft_d1_wvt', models.DecimalField(blank=True, db_column='WindDir_30ft_D1_WVT', decimal_places=2, max_digits=10, null=True)),
                ('winddir_30ft_sd1_wvt', models.DecimalField(blank=True, db_column='WindDir_30ft_SD1_WVT', decimal_places=2, max_digits=10, null=True)),
                ('ws_10ft_mph_avg', models.DecimalField(blank=True, db_column='WS_10ft_mph_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ws_10ft_mph_max', models.DecimalField(blank=True, db_column='WS_10ft_mph_Max', decimal_places=2, max_digits=10, null=True)),
                ('winddir_10ft_d1_wvt', models.DecimalField(blank=True, db_column='WindDir_10ft_D1_WVT', decimal_places=2, max_digits=10, null=True)),
                ('winddir_10ft_sd1_wvt', models.DecimalField(blank=True, db_column='WindDir_10ft_SD1_WVT', decimal_places=2, max_digits=10, null=True)),
                ('ws_sonic_mph_avg', models.DecimalField(blank=True, db_column='WS_Sonic_mph_Avg', decimal_places=2, max_digits=10, null=True)),
                ('ws_sonic_mph_max', models.DecimalField(blank=True, db_column='WS_Sonic_mph_Max', decimal_places=2, max_digits=10, null=True)),
                ('winddir_sonic_d1_wvt', models.DecimalField(blank=True, db_column='WindDir_Sonic_D1_WVT', decimal_places=2, max_digits=10, null=True)),
                ('winddir_sonic_sd1_wvt', models.DecimalField(blank=True, db_column='WindDir_Sonic_SD1_WVT', decimal_places=2, max_digits=10, null=True)),
                ('airtf_avg', models.DecimalField(blank=True, db_column='AirTF_Avg', decimal_places=2, max_digits=10, null=True)),
                ('rh_avg', models.DecimalField(blank=True, db_column='RH_Avg', decimal_places=2, max_digits=10, null=True)),
                ('slrw_avg', models.DecimalField(blank=True, db_column='SlrW_Avg', decimal_places=2, max_digits=10, null=True)),
                ('slrmj_tot', models.DecimalField(blank=True, db_column='SlrMJ_Tot', decimal_places=2, max_digits=10, null=True)),
                ('dewptf', models.DecimalField(blank=True, db_column='DewPtF', decimal_places=2, max_digits=10, null=True)),
                ('rainsincemidnight', models.DecimalField(blank=True, db_column='RainSinceMidnight', decimal_places=2, max_digits=10, null=True)),
                ('rv_pre_accu_tot', models.DecimalField(blank=True, db_column='RV_Pre_Accu_Tot', decimal_places=2, max_digits=10, null=True)),
                ('rv_tips_tot', models.DecimalField(blank=True, db_column='RV_Tips_Tot', decimal_places=2, max_digits=10, null=True)),
                ('rv_tot_pre_accu', models.DecimalField(blank=True, db_column='RV_Tot_Pre_Accu', decimal_places=2, max_digits=10, null=True)),
                ('rv_avg_pre_int_max', models.DecimalField(blank=True, db_column='RV_Avg_Pre_Int_Max', decimal_places=2, max_digits=10, null=True)),
                ('rv_max_pre_int_max', models.DecimalField(blank=True, db_column='RV_Max_Pre_Int_Max', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'weather_conditions',
                'managed': False,
            },
        ),
    ]
