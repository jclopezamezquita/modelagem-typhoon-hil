import typhoon.api.hil as hil
from datetime import date, datetime, timedelta
import time
import json
import math
import os


#Load model
# hil.load_model(file=r'C:/Users/cindy/Google Drive/1. Posdoc UNICAMP/2. PPPD UNICAMP/Merge Unicamp/E75 - HIL/1. Microgrids Models/8. CAMPUSGRID_Meter/campusgrid Target files/campusgrid.cpd', offlineMode=False, vhil_device=True)
hil.load_model(file=r'C:\Users\jessi\Downloads\Doutorado\MERGE\Etapas\E75 - Software de gestao de microrredes\HIL\e75-thyphoon-hil-main\e75-thyphoon-hil\9. CAMPUSGRID_Meters\CAMPUSGRID Target files\campusgrid.cpd', offlineMode=False, vhil_device=True)

#Save settings of model
#hil.save_settings_file(r'C:\Users\cindy\Google Drive\1. Posdoc UNICAMP\2. PPPD UNICAMP\Merge Unicamp\E75 - HIL\1. Microgrids Models\8. CAMPUSGRID_Meter\init.runx')

#Load settings of model
# hil.load_settings_file(file=r'C:\Users\cindy\Google Drive\1. Posdoc UNICAMP\2. PPPD UNICAMP\Merge Unicamp\E75 - HIL\1. Microgrids Models\8. CAMPUSGRID_Meter\init.runx')
hil.load_settings_file(file=r'C:\Users\jessi\Downloads\Doutorado\MERGE\Etapas\E75 - Software de gestao de microrredes\HIL\e75-thyphoon-hil-main\e75-thyphoon-hil\9. CAMPUSGRID_Meters\CAMPUSGRID Target files\init.runx')

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
#Initial Battery SOC set to 60%
hil.set_scada_input_value('Battery ESS (Generic) UI1.Initial SOH', 90.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Qref', 0.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Max SOC', 90.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Min SOC', 15.0)
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
hil.set_scada_input_value('PV Power Plant (Generic) UI1.Irradiance', 1000.0)
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
hil.set_scada_input_value('Variable Load (Generic) UI1.Pref', 0.2)
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

# To compute active power flow
Raa = 0.3570 #Resistence phase to phase 
Laa = 0.00189 #Inductance phase to phase
Gab = Raa / ((Raa**2) + Laa) 
Bkm = -Laa / (Raa + (Laa**2))

new_data = {}

# Time struct: YYYY, MM, DD, HH, Mim, Sec, wday, yday
x = time.localtime()
print(x)

# Sets initial time of the simulation
initial_time = datetime.now()

# Sets the first time to clean the data logger 
time_clean_data_logger = initial_time + timedelta(minutes=11)
time_clean_data_logger_str = time_clean_data_logger.strftime('%Y-%m-%dT%H:%M:%S')
print(time_clean_data_logger) 

# Read the dispatch file 
with open('dispatch.json') as json_file:
    dispatch = json.load(json_file)

while True:

    # First iteration is rejected
    if not new_data:
        time.sleep(60)

    time_now = datetime.now()
    
    index = x[3]
    Pref_bat = dispatch["bess"][index]
    Pref_genset = dispatch["genset"][index]
    print("Pref_bat:", Pref_bat)
    print("Pref_genset:", Pref_genset)
    hil.set_scada_input_value('Battery ESS (Generic) UI1.Pref', Pref_bat)
    hil.set_scada_input_value('Diesel Genset (Generic) UI1.Pref', Pref_genset)

    # Get measurements of node 1 - PCC
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')] = {}
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'] = []
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['name'] = "node_1"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['type'] = "PCC"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['Vmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VAn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['Vmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VBn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['Vmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VCn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['Pmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['Pmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['Pmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['Qmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_QA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['Qmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_QB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['Qmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_QC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][0]['SOC'] = 0.00

    # Get measurements of node 2 - DG (genset)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['name'] = "node_2"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['type'] = "genset"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['Vmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VAn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['Vmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VBn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['Vmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VCn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['Pmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['Pmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['Pmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['Qmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_QA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['Qmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_QB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['Qmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_QC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][1]['SOC'] = 0.00

    # Get measurements of node 3 - Load
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['name'] = "node_3"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['type'] = "load"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['Vmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VAn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['Vmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VBn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['Vmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VCn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['Pmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['Pmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['Pmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['Qmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_QA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['Qmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_QB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['Qmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_QC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][2]['SOC'] = 0.00

    # Get measurements of node 4 - BESS
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['name'] = "node_4"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['type'] = "bess"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['Vmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VAn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['Vmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VBn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['Vmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VCn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['Pmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['Pmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['Pmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['Qmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_QA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['Qmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_QB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['Qmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_QC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][3]['SOC'] = round(hil.read_analog_signal(name='Battery ESS (Generic) UI1.SOC'),2)

    # Get measurements of node 5 - PV
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['name'] = "node_5"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['type'] = "pv"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['Vmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VAn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['Vmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VBn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['Vmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VCn_RMS'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['Pmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['Pmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['Pmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['Qmag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_QA'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['Qmag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_QB'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['Qmag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_QC'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['node'][4]['SOC'] = 0.00

    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'] = []
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][0]['initial_node'] = "node_1"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][0]['final_node'] = "node_2"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][0]['Imag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (DG).IA_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][0]['Imag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (DG).IB_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][0]['Imag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (DG).IC_RMS1'),2)

    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][1]['initial_node'] = "node_1"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][1]['final_node'] = "node_3"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][1]['Imag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (Load).IA_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][1]['Imag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (Load).IB_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][1]['Imag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (Load).IC_RMS1'),2)

    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][2]['initial_node'] = "node_1"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][2]['final_node'] = "node_4"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][2]['Imag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (BESS).IA_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][2]['Imag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (BESS).IB_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][2]['Imag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (BESS).IC_RMS1'),2)

    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'].append({})
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][3]['initial_node'] = "node_1"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][3]['final_node'] = "node_5"
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][3]['Imag_phase_A_rms'] = round(hil.read_analog_signal(name='Meter (PV).IA_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][3]['Imag_phase_B_rms'] = round(hil.read_analog_signal(name='Meter (PV).IB_RMS1'),2)
    new_data[time_now.strftime('%Y-%m-%dT%H:%M:%S')]['branch'][3]['Imag_phase_C_rms'] = round(hil.read_analog_signal(name='Meter (PV).IC_RMS1'),2)


    # Update the dictionary new_data with the new measurements
    new_data.update(new_data)
    
    #if time_clean_data_logger_str in new_data.keys():
    if time_clean_data_logger <= time_now:
        print("\nentrou\n")
        print(time_clean_data_logger)
        delete_time = time_clean_data_logger - timedelta(minutes=9)
        #delete_time_str = delete_time.strftime('%Y-%m-%dT%H:%M:%S')
        print(delete_time)

        first_register = next(iter(new_data))
        print(first_register)
        new_data.pop(first_register)
        #del new_data[delete_time]
        #time_clean_data_logger = time_clean_data_logger + timedelta(seconds=60)
        #time_clean_data_logger_str = time_clean_data_logger.strftime('%Y-%m-%dT%H:%M:%S')
        #print(time_clean_data_logger_str) 
    

    # Write the dictionary in a json file
    with open('data_logger.json', 'w') as outfile:
        json.dump(new_data, outfile, indent=4)

    # Wait 60 seconds
    time.sleep(60)

    # Updates the current time
    x = time.localtime()

    if x[4] == 30:
        break

# Stop simulation
hil.stop_simulation()
print ("\n------ Stop simulation ------\n")

# and end script
hil.end_script_by_user()