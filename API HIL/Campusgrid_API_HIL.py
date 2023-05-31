import typhoon.api.hil as hil
from datetime import date, datetime, timedelta
import time
import json
import math
import requests


#Load model
# hil.load_model(file=r'C:/Users/cindy/Google Drive/1. Posdoc UNICAMP/2. PPPD UNICAMP/Merge Unicamp/E75 - HIL/1. Microgrids Models/8. CAMPUSGRID_Meter/campusgrid Target files/campusgrid.cpd', offlineMode=False, vhil_device=True)
hil.load_model(file=r'C:\Users\jessi\Downloads\Doutorado\MERGE\Etapas\E75 - Software de gestao de microrredes\HIL\e75-thyphoon-hil-main\e75-thyphoon-hil\9. CAMPUSGRID_Meters\CAMPUSGRID Target files\CAMPUSGRID.cpd', offlineMode=False, vhil_device=True)

#Save settings of model
#hil.save_settings_file(r'C:\Users\cindy\Google Drive\1. Posdoc UNICAMP\2. PPPD UNICAMP\Merge Unicamp\E75 - HIL\1. Microgrids Models\8. CAMPUSGRID_Meter\init.runx')

#Load settings of model
# hil.load_settings_file(file=r'C:\Users\cindy\Google Drive\1. Posdoc UNICAMP\2. PPPD UNICAMP\Merge Unicamp\E75 - HIL\1. Microgrids Models\8. CAMPUSGRID_Meter\init.runx')
hil.load_settings_file(file=r'C:\Users\jessi\Downloads\Doutorado\MERGE\Etapas\E75 - Software de gestao de microrredes\HIL\e75-thyphoon-hil-main\e75-thyphoon-hil\9. CAMPUSGRID_Meters\CAMPUSGRID Target files\init.runx')

hil.set_scada_input_value('Battery ESS (Generic) UI1.Initial SOC', 18.0)

# Start simulation
hil.start_simulation()
print ("\n------ Simulation Start ------\n")

# Contactors closed (Main grid and PCC)
hil.set_contactor('PCC.S1', swControl=True, swState=True) #PAC fechado 
hil.set_scada_input_value('Grid UI1.Connect', 1.0) #Contactor rede fechado

# DERs contactors closed
hil.set_scada_input_value('Battery ESS (Generic) UI1.Enable', 1.0) #BESS contactor closed 
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Enable', 1.0) #DG contactor closed
hil.set_scada_input_value('PV Power Plant (Generic) UI1.Enable', 1.0) #PV contactor closed
hil.set_scada_input_value('Variable Load (Generic) UI1.Enable', 1.0) #Load contactor closed

#********************Inputs BESS***********************
#
hil.set_scada_input_value('Battery ESS (Generic) UI1.Initial SOH', 90.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Qref', 0.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Max SOC', 100.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Min SOC', 15.5)
hil.set_scada_input_value('Battery ESS (Generic) UI1.I alarm upper limit', 1.5)
hil.set_scada_input_value('Battery ESS (Generic) UI1.V alarm lower limit', 0.5)
hil.set_scada_input_value('Battery ESS (Generic) UI1.V alarm upper limit', 1.5)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Converter mode', 0.0) #BESS in grid following mode

#********************Inputs DG***********************
# hil.set_scada_input_value('Diesel Genset (Generic) UI1.Pref', 0.5)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Fref', 1.0)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Fref rate of change', 0.02)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Fref rate of change', 0.02)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Frequency droop coeff', 2.0)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Frequency droop offset', 0.0)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.I alarm timeout', 10.0)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.I alarm upper limit', 1.5)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Pref rate of change', 0.1)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Sync timeout', 20.0)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.V alarm lower limit', 0.5)
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Operation mode', 0.0) #DG in grid following mode

#********************Inputs PV***********************
# hil.set_scada_input_value('PV Power Plant (Generic) UI1.Irradiance', 1000.0)
hil.set_scada_input_value('PV Power Plant (Generic) UI1.LVRT enable', 0.0)
hil.set_scada_input_value('PV Power Plant (Generic) UI1.LVRT Q contribution', 2.0)
hil.set_scada_input_value('PV Power Plant (Generic) UI1.I alarm upper limit', 1.5)
hil.set_scada_input_value('PV Power Plant (Generic) UI1.F alarm lower limit', 0.5)
hil.set_scada_input_value('PV Power Plant (Generic) UI1.F alarm upper limit', 1.5)
hil.set_scada_input_value('PV Power Plant (Generic) UI1.Pcurtailment', 1.0)
hil.set_scada_input_value('PV Power Plant (Generic) UI1.Pcurtailment rate of change', 0.1)
hil.set_scada_input_value('PV Power Plant (Generic) UI1.V alarm lower limit', 0.5)
hil.set_scada_input_value('PV Power Plant (Generic) UI1.V alarm upper limit', 1.5)

#********************Inputs Load***********************
# hil.set_scada_input_value('Variable Load (Generic) UI1.Pref', 0.2)
hil.set_scada_input_value('Variable Load (Generic) UI1.P dependency type', 0.0)
hil.set_scada_input_value('Variable Load (Generic) UI1.P(f) k1', 0.0)
hil.set_scada_input_value('Variable Load (Generic) UI1.P(f) k2', 0.0)
hil.set_scada_input_value('Variable Load (Generic) UI1.P(V) k1', 0.0)
hil.set_scada_input_value('Variable Load (Generic) UI1.P(V) k2', 0.0)
hil.set_scada_input_value('Variable Load (Generic) UI1.I alarm upper limit', 1.5)
hil.set_scada_input_value('Variable Load (Generic) UI1.F alarm upper limit', 1.5)
hil.set_scada_input_value('Variable Load (Generic) UI1.F alarm lower limit', 0.5)
hil.set_scada_input_value('Variable Load (Generic) UI1.V alarm lower limit', 0.5)
hil.set_scada_input_value('Variable Load (Generic) UI1.V alarm upper limit', 1.5)

# To compute active and reactive power flow
with open('Line_parameters.json') as json_file:
    impedance = json.load(json_file)

new_data = {}

# Time struct: YYYY, MM, DD, HH, Mim, Sec, wday, yday
x = time.localtime()
print(x)

# Sets initial time of the simulation
initial_time = datetime.now()

# Sets the first time to clean the data logger 
time_clean_data_logger = initial_time + timedelta(hours=10,minutes=1)
print(time_clean_data_logger) 

max_irradiance = 710.59

#Read the profile file
with open('profiles.json') as json_file:
    profiles = json.load(json_file)


def dispatch_requests():
    URL = "http://192.168.0.185:8051/"
    dispatch_EMS = requests.get(url=URL + "v1/api/economic_dispatch", headers={"accept" : "application/json"})
    dispatch_EMS = json.loads(dispatch_EMS.text)

    dispatch_file = {}
    dispatch_file["bess"] = []
    for x in range(0,10):
        if (dispatch_EMS[0]['bat_power_t0' + str(x)]) == 0:
            dispatch_file["bess"].append(round((dispatch_EMS[0]['bat_power_t0' + str(x)])/810,3))
        else:
            dispatch_file["bess"].append(round(((dispatch_EMS[0]['bat_power_t0' + str(x)])*(-1))/810,3))
    for x in range(10,24):
        if (dispatch_EMS[0]['bat_power_t' + str(x)]) == 0:
            dispatch_file["bess"].append(round((dispatch_EMS[0]['bat_power_t' + str(x)])/810,3))
        else:
            dispatch_file["bess"].append(round((dispatch_EMS[0]['bat_power_t' + str(x)])*(-1)/810,3))
    dispatch_file["genset"] = []
    for x in range(0,10):
        dispatch_file["genset"].append(dispatch_EMS[0]['genset_power_t0' + str(x)])
    for x in range(10,24):
        dispatch_file["genset"].append(dispatch_EMS[0]['genset_power_t' + str(x)])
    dispatch_file["pv_curt"] = []
    for x in range(0,10):
        dispatch_file["pv_curt"].append(dispatch_EMS[0]['pv_curt_t0' + str(x)])
    for x in range(10,24):
        dispatch_file["pv_curt"].append(dispatch_EMS[0]['pv_curt_t' + str(x)])
    dispatch_file["load_curt"] = []
    for x in range(0,10):
        dispatch_file["load_curt"].append(dispatch_EMS[0]['load_curt_t0' + str(x)])
    for x in range(10,24):
        dispatch_file["load_curt"].append(dispatch_EMS[0]['load_curt_t' + str(x)])

    with open('dispatch_file.json', 'w') as outfile:
	    json.dump(dispatch_file, outfile, indent=1)


while True:

    # First iteration is rejected
    if not new_data:
        #dispatch_requests()
        time.sleep(60)

    time_now = datetime.now()
    
    # Read the dispatch file 
    with open('dispatch_file.json') as json_file:
        dispatch_file = json.load(json_file)

    index = x[3]
    #Pref_bat = dispatch_file["bess"][index]
    Pref_genset = dispatch_file["genset"][index]

    if x[4] <= 35:
        Pref_bat = 0.3
    else:
        Pref_bat = -0.5

    index_5min = ((index * 60) + x[4])//5
    print(index_5min)
    Pref_pload = profiles["pload"][index_5min]
    Pref_qload = profiles["qload"][index_5min]
    Irradiance = (profiles["irradiance"][index_5min]) * max_irradiance
    
    print("Pref_bat:", Pref_bat)
    print("Pref_genset:", Pref_genset)
    print("Pref_pload:", Pref_pload)
    print("Pref_qload:", Pref_qload)
    print("Irradiance:", Irradiance)

    hil.set_scada_input_value('Battery ESS (Generic) UI1.Pref', Pref_bat)

    if Pref_bat == 0.0:
        hil.set_contactor('name', swControl = True, swState = False)
    else:
        hil.set_scada_input_value('Diesel Genset (Generic) UI1.Pref', Pref_genset)
    
    hil.set_scada_input_value('Variable Load (Generic) UI1.Pref', Pref_pload)
    hil.set_scada_input_value('Variable Load (Generic) UI1.Qref', Pref_qload )
    hil.set_scada_input_value('PV Power Plant (Generic) UI1.Irradiance', Irradiance)

    # To compute angles and power flow at each node 
    PF_PCC_A  = hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PFA')
    PF_PCC_B  = hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PFB')
    PF_PCC_C  = hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PFC')
    PF_DG_A  = hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PFA')
    PF_DG_B  = hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PFB')
    PF_DG_C  = hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PFC')
    PF_Load_A  = hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PFA')
    PF_Load_B  = hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PFB')
    PF_Load_C  = hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PFC')
    PF_BESS_A  = hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PFA')
    PF_BESS_B  = hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PFB')
    PF_BESS_C  = hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PFC')
    PF_PV_A  = hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PFA') 
    PF_PV_B  = hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PFB')
    PF_PV_C  = hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PFC')
    angl_PCC_A  = math.acos(PF_PCC_A)
    angl_PCC_B  = math.acos(PF_PCC_B)
    angl_PCC_C  = math.acos(PF_PCC_C)
    angl_DG_A  = math.acos(PF_DG_A)
    angl_DG_B  = math.acos(PF_DG_B)
    angl_DG_C  = math.acos(PF_DG_C)
    angl_Load_A  = math.acos(PF_Load_A)
    angl_Load_B  = math.acos(PF_Load_B)
    angl_Load_C  = math.acos(PF_Load_C)
    angl_BESS_A  = math.acos(PF_BESS_A)
    angl_BESS_B  = math.acos(PF_BESS_B)
    angl_BESS_C  = math.acos(PF_BESS_C)
    angl_PV_A  = math.acos(PF_PV_A)
    angl_PV_B  = math.acos(PF_PV_B)
    angl_PV_C  = math.acos(PF_PV_C)

    # Get measurements of node 1 - PCC
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')] = {}
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'] = []
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['name'] = "1"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['der'] = "pcc"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['Vmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VAn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['Vmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VBn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['Vmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VCn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['Pmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['Pmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['Pmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['Qmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_QA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['Qmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_QB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['Qmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_QC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][0]['SOC'] = 0.00

    # Get measurements of node 2 - DG (genset)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['name'] = "2"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['der'] = "genset"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['Vmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VAn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['Vmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VBn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['Vmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VCn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['Pmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['Pmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['Pmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['Qmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_QA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['Qmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_QB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['Qmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_QC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][1]['SOC'] = 0.00

    # Get measurements of node 3 - Load
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['name'] = "3"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['der'] = "load"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['Vmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VAn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['Vmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VBn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['Vmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VCn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['Pmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['Pmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['Pmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['Qmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_QA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['Qmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_QB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['Qmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_QC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][2]['SOC'] = 0.00

    # Get measurements of node 4 - BESS
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['name'] = "4"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['der'] = "bess"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['Vmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VAn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['Vmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VBn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['Vmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VCn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['Pmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['Pmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['Pmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['Qmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_QA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['Qmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_QB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['Qmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_QC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][3]['SOC'] = round(hil.read_analog_signal(name='Battery ESS (Generic) UI1.SOC'),2)

    # Get measurements of node 5 - PV
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['name'] = "5"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['der'] = "pv"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['Vmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VAn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['Vmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VBn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['Vmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VCn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['Pmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['Pmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['Pmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['Qmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_QA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['Qmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_QB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['Qmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_QC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['node'][4]['SOC'] = 0.00

    # Get measurements of branch 1 - 2
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'] = []
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['initial_node'] = "1"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['final_node'] = "2"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['Imag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (DG).IA_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['Imag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (DG).IB_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['Imag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (DG).IC_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['Active_power_flow_phase_A'] = round((hil.read_analog_signal(name='Meter (DG).IA_RMS1'))**2*impedance["Raa"]*(math.cos(angl_PCC_A - angl_DG_A)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['Active_power_flow_phase_B'] = round((hil.read_analog_signal(name='Meter (DG).IB_RMS1'))**2*impedance["Rbb"]*(math.cos(angl_PCC_B - angl_DG_B)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['Active_power_flow_phase_C'] = round((hil.read_analog_signal(name='Meter (DG).IC_RMS1'))**2*impedance["Rcc"]*(math.cos(angl_PCC_C - angl_DG_C)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['Reactive_power_flow_phase_A'] = round((hil.read_analog_signal(name='Meter (DG).IA_RMS1'))**2*impedance["Xaa"]*(math.sin(angl_PCC_A - angl_DG_A)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['Reactive_power_flow_phase_B'] = round((hil.read_analog_signal(name='Meter (DG).IB_RMS1'))**2*impedance["Xbb"]*(math.sin(angl_PCC_B - angl_DG_B)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][0]['Reactive_power_flow_phase_C'] = round((hil.read_analog_signal(name='Meter (DG).IC_RMS1'))**2*impedance["Xcc"]*(math.sin(angl_PCC_C - angl_DG_C)),2)

    # Get measurements of branch 1 - 3
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['initial_node'] = "1"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['final_node'] = "3"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['Imag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (Load).IA_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['Imag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (Load).IB_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['Imag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (Load).IC_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['Active_power_flow_phase_A'] = round((hil.read_analog_signal(name='Meter (Load).IA_RMS1'))**2*impedance["Raa"]*(math.cos(angl_PCC_A - angl_Load_A)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['Active_power_flow_phase_B'] = round((hil.read_analog_signal(name='Meter (Load).IB_RMS1'))**2*impedance["Rbb"]*(math.cos(angl_PCC_B - angl_Load_B)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['Active_power_flow_phase_C'] = round((hil.read_analog_signal(name='Meter (Load).IC_RMS1'))**2*impedance["Rcc"]*(math.cos(angl_PCC_C - angl_Load_C)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['Reactive_power_flow_phase_A'] = round((hil.read_analog_signal(name='Meter (Load).IA_RMS1'))**2*impedance["Xaa"]*(math.sin(angl_PCC_A - angl_Load_A)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['Reactive_power_flow_phase_B'] = round((hil.read_analog_signal(name='Meter (Load).IB_RMS1'))**2*impedance["Xbb"]*(math.sin(angl_PCC_B - angl_Load_B)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][1]['Reactive_power_flow_phase_C'] = round((hil.read_analog_signal(name='Meter (Load).IC_RMS1'))**2*impedance["Xcc"]*(math.sin(angl_PCC_C - angl_Load_C)),2)

    # Get measurements of branch 1 - 4
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['initial_node'] = "1"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['final_node'] = "4"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['Imag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (BESS).IA_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['Imag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (BESS).IB_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['Imag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (BESS).IC_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['Active_power_flow_phase_A'] = round((hil.read_analog_signal(name='Meter (BESS).IA_RMS1'))**2*impedance["Raa"]*(math.cos(angl_PCC_A - angl_BESS_A)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['Active_power_flow_phase_B'] = round((hil.read_analog_signal(name='Meter (BESS).IB_RMS1'))**2*impedance["Rbb"]*(math.cos(angl_PCC_B - angl_BESS_B)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['Active_power_flow_phase_C'] = round((hil.read_analog_signal(name='Meter (BESS).IC_RMS1'))**2*impedance["Rcc"]*(math.cos(angl_PCC_C - angl_BESS_C)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['Reactive_power_flow_phase_A'] = round((hil.read_analog_signal(name='Meter (BESS).IA_RMS1'))**2*impedance["Xaa"]*(math.sin(angl_PCC_A - angl_BESS_A)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['Reactive_power_flow_phase_B'] = round((hil.read_analog_signal(name='Meter (BESS).IB_RMS1'))**2*impedance["Xbb"]*(math.sin(angl_PCC_B - angl_BESS_B)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][2]['Reactive_power_flow_phase_C'] = round((hil.read_analog_signal(name='Meter (BESS).IC_RMS1'))**2*impedance["Xcc"]*(math.sin(angl_PCC_C - angl_BESS_C)),2)

    # Get measurements of branch 1 - 5
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['initial_node'] = "1"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['final_node'] = "5"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['Imag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PV).IA_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['Imag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PV).IB_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['Imag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PV).IC_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['Active_power_flow_phase_A'] = round((hil.read_analog_signal(name='Meter (PV).IA_RMS1'))**2*impedance["Raa"]*(math.cos(angl_PCC_A - angl_PV_A)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['Active_power_flow_phase_B'] = round((hil.read_analog_signal(name='Meter (PV).IB_RMS1'))**2*impedance["Rbb"]*(math.cos(angl_PCC_B - angl_PV_B)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['Active_power_flow_phase_C'] = round((hil.read_analog_signal(name='Meter (PV).IC_RMS1'))**2*impedance["Rcc"]*(math.cos(angl_PCC_C - angl_PV_C)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['Reactive_power_flow_phase_A'] = round((hil.read_analog_signal(name='Meter (PV).IA_RMS1'))**2*impedance["Xaa"]*(math.sin(angl_PCC_A - angl_PV_A)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['Reactive_power_flow_phase_B'] = round((hil.read_analog_signal(name='Meter (PV).IB_RMS1'))**2*impedance["Xbb"]*(math.sin(angl_PCC_B - angl_PV_B)),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S.%f%z')]['branch'][3]['Reactive_power_flow_phase_C'] = round((hil.read_analog_signal(name='Meter (PV).IC_RMS1'))**2*impedance["Xcc"]*(math.sin(angl_PCC_C - angl_PV_C)),2)


    # Update the dictionary new_data with the new measurements
    new_data.update(new_data)
    
    # 
    if time_clean_data_logger <= time_now:
        first_register = next(iter(new_data))
        new_data.pop(first_register)

        print("Irá limpar o registro:", first_register)
        print("E adicionar o registro:", time_now)
        
    # Write the dictionary in a json file
    with open('data_logger.json', 'w') as outfile:
        json.dump(new_data, outfile, indent=4)

    # Wait 60 seconds
    time.sleep(60)

    # Updates the current time 
    x = time.localtime()

    # Update the dispatch at 23h e 59 min
    if x[3] == 23 and x[4] == 59:
        dispatch_requests()

    # Time struct: YYYY, MM, DD, HH, Mim, Sec, wday, yday
    if x[1] == 2 and x[2] == 5 and x[3] == 15:
        break

# Stop simulation
hil.stop_simulation()
print ("\n------ Stop simulation ------\n")

# and end script
hil.end_script_by_user()