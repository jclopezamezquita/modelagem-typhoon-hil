import typhoon.api.hil as hil 
from typhoon.api import hil as hil
import numpy as np  


#Load model
hil.load_model(file=r'C:/Users/cindy/Google Drive/1. Posdoc UNICAMP/2. PPPD UNICAMP/Merge Unicamp/E75 - HIL/1. Microgrids Models/8. CAMPUSGRID_Meter/campusgrid Target files/campusgrid.cpd', offlineMode=False, vhil_device=True)
#Save settings of model
hil.save_settings_file(r'C:\Users\cindy\Google Drive\1. Posdoc UNICAMP\2. PPPD UNICAMP\Merge Unicamp\E75 - HIL\1. Microgrids Models\8. CAMPUSGRID_Meter\init.runx')
#Load settings of model
hil.load_settings_file(file=r'C:\Users\cindy\Google Drive\1. Posdoc UNICAMP\2. PPPD UNICAMP\Merge Unicamp\E75 - HIL\1. Microgrids Models\8. CAMPUSGRID_Meter\init.runx')

#Start the simulation
hil.start_simulation()
print ("Simulation Start")

#Step of simulation
simulation_step = hil.get_sim_step()
print(simulation_step)

#To read the load profile data and irradiance 
cont1 = 0
cont2 = 0
cont3 = 0
wait = simulation_step

def read_csv(file_path):
    lookup_file = open(file_path, 'r')
    calc_res = lookup_file.readlines()
    lookup_file.close()
    calc_res = np.array(calc_res).astype(float)

    return calc_res


def write_csv(file_path, data_array):
	
	file = open(file_path, 'w')
	for i in range(len(data_array)):
		file.write(str(data_array[i]) + '\n')
		
		file.close()
          

file_data  = read_csv('C:/Users/cindy/python/API HIL/pload_profile.txt')
file_data2 = read_csv('C:/Users/cindy/python/API HIL/qload_profile.txt')
file_data3 = read_csv('C:/Users/cindy/python/API HIL/solar_irradiation.txt')
#print(file_data)
#print(file_data2)
#print(file_data3)

#Contactors closed (Main grid and PCC)
hil.set_contactor('PCC.S1', swControl=True, swState=True) #PAC fechado 
hil.set_scada_input_value('Grid UI1.Connect', 1.0) #Contactor rede fechado

#DERs contactors closed
hil.set_scada_input_value('Battery ESS (Generic) UI1.Enable', 1.0) #BESS contactor closed 
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Enable', 1.0) #DG contactor closed
hil.set_scada_input_value('PV Power Plant (Generic) UI1.Enable', 1.0) #PV contactor closed
hil.set_scada_input_value('Variable Load (Generic) UI1.Enable', 1.0) #Load contactor closed

#********************Inputs BESS***********************
hil.set_scada_input_value('Battery ESS (Generic) UI1.Initial SOC', 80.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Initial SOH', 90.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Pref', 0.5)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Qref', 0.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Max SOC', 90.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Min SOC', 15.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.I alarm upper limit', 1.5)
hil.set_scada_input_value('Battery ESS (Generic) UI1.V alarm lower limit', 0.5)
hil.set_scada_input_value('Battery ESS (Generic) UI1.V alarm upper limit', 1.5)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Initial SOC', 80.0)
hil.set_scada_input_value('Battery ESS (Generic) UI1.Converter mode', 0.0) #BESS in grid following mode

#********************Inputs DG***********************
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Pref', 0.5)
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
hil.set_scada_input_value('PV Power Plant (Generic) UI1.Pcurtailment', 0.0)
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


#Scripts for load profile*******************
#*********************************
#Macro on timer
'''
hil.set_scada_input_value('Variable Load (Generic) UI1.Pref', file_data[cont1])

hil.wait_sec(wait)
cont1 += 1

if cont1 > len(file_data)-1:
	cont1 = 0
#*********************End of sript*********************
'''

#List of measurement of BESS
Imag_phase_A_rms_BESS   = []
Imag_phase_B_rms_BESS   = []
Imag_phase_C_rms_BESS   = []
Vmag_phase_A_rms_BESS   = []
Vmag_phase_B_rms_BESS   = []
Vmag_phase_C_rms_BESS   = []
Vmag_phases_AB_rms_BESS = []
Vmag_phases_BC_rms_BESS = []
Vmag_phases_CA_rms_BESS = []
Pmag_3phase_BESS        = []
Qmag_3phase_BESS        = []
Pmag_phase_A_rms_BESS   = []
Pmag_phase_B_rms_BESS   = []
Pmag_phase_C_rms_BESS   = []
Qmag_phase_A_rms_BESS   = []
Qmag_phase_B_rms_BESS   = []
Qmag_phase_C_rms_BESS   = []
SOC                     = []

#List of measurement of DG
Imag_phase_A_rms_DG   = []
Imag_phase_B_rms_DG   = []
Imag_phase_C_rms_DG   = []
Vmag_phase_A_rms_DG   = []
Vmag_phase_B_rms_DG   = []
Vmag_phase_C_rms_DG   = []
Vmag_phases_AB_rms_DG = []
Vmag_phases_BC_rms_DG = []
Vmag_phases_CA_rms_DG = []
Pmag_3phase_DG        = []
Qmag_3phase_DG        = [] 
Pmag_phase_A_rms_DG   = []
Pmag_phase_B_rms_DG   = []
Pmag_phase_C_rms_DG   = []
Qmag_phase_A_rms_DG   = []
Qmag_phase_B_rms_DG   = []
Qmag_phase_C_rms_DG   = []

#List of measurement of PV
Imag_phase_A_rms_PV   = []
Imag_phase_B_rms_PV   = []
Imag_phase_C_rms_PV   = []
Vmag_phase_A_rms_PV   = []
Vmag_phase_B_rms_PV   = []
Vmag_phase_C_rms_PV   = []
Vmag_phases_AB_rms_PV = []
Vmag_phases_BC_rms_PV = []
Vmag_phases_CA_rms_PV = []
Pmag_3phase_PV        = []
Qmag_3phase_PV        = [] 
Pmag_phase_A_rms_PV   = []
Pmag_phase_B_rms_PV   = []
Pmag_phase_C_rms_PV   = []
Qmag_phase_A_rms_PV   = []
Qmag_phase_B_rms_PV   = []
Qmag_phase_C_rms_PV   = []



#List of measurement of Load
Imag_phase_A_rms_Load   = []
Imag_phase_B_rms_Load   = []
Imag_phase_C_rms_Load   = []
Vmag_phase_A_rms_Load   = []
Vmag_phase_B_rms_Load   = []
Vmag_phase_C_rms_Load   = []
Vmag_phases_AB_rms_Load = []
Vmag_phases_BC_rms_Load = []
Vmag_phases_CA_rms_Load = []
Pmag_3phase_Load        = []
Qmag_3phase_Load        = [] 
Pmag_phase_A_rms_Load   = []
Pmag_phase_B_rms_Load   = []
Pmag_phase_C_rms_Load   = []
Qmag_phase_A_rms_Load   = []
Qmag_phase_B_rms_Load   = []
Qmag_phase_C_rms_Load   = []
P_meas_Load = []

#List of measurement of PCC
Imag_phase_A_rms_PCC   = []
Imag_phase_B_rms_PCC   = []
Imag_phase_C_rms_PCC   = []
Vmag_phase_A_rms_PCC   = []
Vmag_phase_B_rms_PCC   = []
Vmag_phase_C_rms_PCC   = []
Vmag_phases_AB_rms_PCC = []
Vmag_phases_BC_rms_PCC = []
Vmag_phases_CA_rms_PCC = []
Pmag_3phase_PCC        = []
Qmag_3phase_PCC        = [] 
Pmag_phase_A_rms_PCC   = []
Pmag_phase_B_rms_PCC   = []
Pmag_phase_C_rms_PCC   = []
Qmag_phase_A_rms_PCC   = []
Qmag_phase_B_rms_PCC   = []
Qmag_phase_C_rms_PCC   = []


#Read the step simulation
Execute_simulation = simulation_step
cont = 0

while (Execute_simulation <= 10):
    rest_divi = cont % 100000

    if rest_divi == 0:

        #To get the measurements of BESS
        Imag_phase_A_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).IA_RMS1'))  
        Imag_phase_B_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).IB_RMS1'))  
        Imag_phase_C_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).IC_RMS1'))  
        Vmag_phase_A_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VAn_RMS'))  
        Vmag_phase_B_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VBn_RMS'))  
        Vmag_phase_C_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VCn_RMS'))  
        Vmag_phases_AB_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VAB_RMS'))
        Vmag_phases_BC_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VBC_RMS'))
        Vmag_phases_CA_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VCA_RMS'))
        Pmag_3phase_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_P'))
        Qmag_3phase_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_Q'))
        Pmag_phase_A_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PA'))
        Pmag_phase_B_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PB'))
        Pmag_phase_C_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_PC'))
        Qmag_phase_A_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_QA'))
        Qmag_phase_B_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_QB'))
        Qmag_phase_C_rms_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.POWER_QC'))
        SOC.append(hil.read_analog_signal(name='Battery ESS (Generic) UI1.SOC'))                   

        #To get the measurements of DG
        Imag_phase_A_rms_DG.append(hil.read_analog_signal(name='Meter (DG).IA_RMS1'))  
        Imag_phase_B_rms_DG.append(hil.read_analog_signal(name='Meter (DG).IB_RMS1'))  
        Imag_phase_C_rms_DG.append(hil.read_analog_signal(name='Meter (DG).IC_RMS1'))  
        Vmag_phase_A_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VAn_RMS'))  
        Vmag_phase_B_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VBn_RMS'))  
        Vmag_phase_C_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VCn_RMS'))  
        Vmag_phases_AB_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VAB_RMS'))
        Vmag_phases_BC_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VBC_RMS'))
        Vmag_phases_CA_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VCA_RMS'))
        Pmag_3phase_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_P'))
        Qmag_3phase_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_Q'))
        Pmag_phase_A_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PA'))
        Pmag_phase_B_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PB'))
        Pmag_phase_C_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_PC'))
        Qmag_phase_A_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_QA'))
        Qmag_phase_B_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_QB'))
        Qmag_phase_C_rms_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.POWER_QC'))
 

        #To get the measurements of PV
        Imag_phase_A_rms_PV.append(hil.read_analog_signal(name='Meter (PV).IA_RMS1'))  
        Imag_phase_B_rms_PV.append(hil.read_analog_signal(name='Meter (PV).IB_RMS1'))  
        Imag_phase_C_rms_PV.append(hil.read_analog_signal(name='Meter (PV).IC_RMS1'))  
        Vmag_phase_A_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VAn_RMS'))  
        Vmag_phase_B_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VBn_RMS'))  
        Vmag_phase_C_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VCn_RMS'))  
        Vmag_phases_AB_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VAB_RMS'))
        Vmag_phases_BC_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VBC_RMS'))
        Vmag_phases_CA_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VCA_RMS'))
        Pmag_3phase_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_P'))
        Qmag_3phase_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_Q'))
        Pmag_phase_A_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PA'))
        Pmag_phase_B_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PB'))
        Pmag_phase_C_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_PC'))
        Qmag_phase_A_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_QA'))
        Qmag_phase_B_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_QB'))
        Qmag_phase_C_rms_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.POWER_QC'))

        #To get the measurements of Load
        Imag_phase_A_rms_Load.append(hil.read_analog_signal(name='Meter (Load).IA_RMS1'))  
        Imag_phase_B_rms_Load.append(hil.read_analog_signal(name='Meter (Load).IB_RMS1'))  
        Imag_phase_C_rms_Load.append(hil.read_analog_signal(name='Meter (Load).IC_RMS1'))  
        Vmag_phase_A_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VAn_RMS'))  
        Vmag_phase_B_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VBn_RMS'))  
        Vmag_phase_C_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VCn_RMS'))  
        Vmag_phases_AB_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VAB_RMS'))
        Vmag_phases_BC_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VBC_RMS'))
        Vmag_phases_CA_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VCA_RMS'))
        Pmag_3phase_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_P'))
        Qmag_3phase_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_Q'))
        Pmag_phase_A_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PA'))
        Pmag_phase_B_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PB'))
        Pmag_phase_C_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_PC'))
        Qmag_phase_A_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_QA'))
        Qmag_phase_B_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_QB'))
        Qmag_phase_C_rms_Load.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.POWER_QC'))
        P_meas_Load.append(hil.read_analog_signal(name='Variable Load (Generic) UI1.Pmeas_kW')) 

        
        #To get the measurements of PCC
        Imag_phase_A_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).IA_RMS1'))  
        Imag_phase_B_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).IB_RMS1'))  
        Imag_phase_C_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).IC_RMS1'))  
        Vmag_phase_A_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VAn_RMS'))  
        Vmag_phase_B_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VBn_RMS'))  
        Vmag_phase_C_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VCn_RMS'))  
        Vmag_phases_AB_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VAB_RMS'))
        Vmag_phases_BC_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VBC_RMS'))
        Vmag_phases_CA_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VCA_RMS'))
        Pmag_3phase_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_P'))
        Qmag_3phase_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_Q'))
        Pmag_phase_A_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PA'))
        Pmag_phase_B_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PB'))
        Pmag_phase_C_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_PC'))
        Qmag_phase_A_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_QA'))
        Qmag_phase_B_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_QB'))
        Qmag_phase_C_rms_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.POWER_QC'))

    #To increment execution step
    Execute_simulation += simulation_step
    cont += 1

# Stop the simulation
hil.stop_simulation()
print ("Stop simulation")


#To vizualize at console
print ("Battery RMS Current at phase A(A):", Imag_phase_A_rms_BESS)
print ("Battery RMS Current at phase B(A):", Imag_phase_B_rms_BESS)
print ("Battery RMS Current at phase C(A):", Imag_phase_C_rms_BESS)
print ("Battery RMS Voltage at phase A(V):", Vmag_phase_A_rms_BESS)
print ("Battery RMS Voltage at phase B(V):", Vmag_phase_B_rms_BESS)
print ("Battery RMS Voltage at phase C(V):", Vmag_phase_C_rms_BESS)
print ("Battery RMS Voltages at phases AB (V):", Vmag_phases_AB_rms_BESS)
print ("Battery RMS Voltages at phases BC (V):", Vmag_phases_BC_rms_BESS)
print ("Battery RMS Voltages at phases CA (V):", Vmag_phases_CA_rms_BESS)
print ("RMS three-phase reactive power at the Battery (W):", Pmag_3phase_BESS)
print ("RMS three-phase active power at the Battery (VAr):", Qmag_3phase_BESS)
print ("Active power of phase A in the battery (W):", Pmag_phase_A_rms_BESS)
print ("Active power of phase B in the battery (W):", Pmag_phase_B_rms_BESS)
print ("Active power of phase C in the battery (W):", Pmag_phase_C_rms_BESS)
print ("Reactive power of phase A in the battery(VAr):", Qmag_phase_A_rms_BESS)
print ("Reactive power of phase B in the battery(VAr):", Qmag_phase_B_rms_BESS)
print ("Reactive power of phase C in the battery(VAr):", Qmag_phase_C_rms_BESS)
print ("SOC of Battery:", SOC)


print ("Diesel Genset RMS Current at phase A(A):", Imag_phase_A_rms_DG)
print ("Diesel Genset RMS Current at phase B(A):", Imag_phase_B_rms_DG)
print ("Diesel Genset RMS Current at phase C(A):", Imag_phase_C_rms_DG)
print ("Diesel Genset RMS Voltage at phase A(V):", Vmag_phase_A_rms_DG)
print ("Diesel Genset RMS Voltage at phase B(V):", Vmag_phase_B_rms_DG)
print ("Diesel Genset RMS Voltage at phase C(V):", Vmag_phase_C_rms_DG)
print ("Diesel Genset RMS Voltages at phases AB (V):", Vmag_phases_AB_rms_DG)
print ("Diesel Genset RMS Voltages at phases BC (V):", Vmag_phases_BC_rms_DG)
print ("Diesel Genset RMS Voltages at phases CA (V):", Vmag_phases_CA_rms_DG)
print ("RMS  three-phase active power at the Diesel Genset (W):", Pmag_3phase_DG)
print ("RMS  three-phase reactive power at the Diesel Genset (VAr):", Qmag_3phase_DG)
print ("Active power of phase A in the Diesel Genset (W):", Pmag_phase_A_rms_DG)
print ("Active power of phase B in the Diesel Genset (W):", Pmag_phase_B_rms_DG)
print ("Active power of phase C in the Diesel Genset (W):", Pmag_phase_C_rms_DG)
print ("Reactive power of phase A in the Diesel Genset(VAr):", Qmag_phase_A_rms_DG)
print ("Reactive power of phase B in the Diesel Genset(VAr):", Qmag_phase_B_rms_DG)
print ("Reactive power of phase C in the Diesel Genset(VAr):", Qmag_phase_C_rms_DG)

print ("PV RMS Current at phase A(A):", Imag_phase_A_rms_PV)
print ("PV RMS Current at phase B(A):", Imag_phase_B_rms_PV)
print ("PV RMS Current at phase C(A):", Imag_phase_C_rms_PV)
print ("PV RMS Voltage at phase A(V):", Vmag_phase_A_rms_PV)
print ("PV RMS Voltage at phase B(V):", Vmag_phase_B_rms_PV)
print ("PV RMS Voltage at phase C(V):", Vmag_phase_C_rms_PV)
print ("PV RMS Voltages at phases AB (V):", Vmag_phases_AB_rms_PV)
print ("PV RMS Voltages at phases BC (V):", Vmag_phases_BC_rms_PV)
print ("PV RMS Voltages at phases CA (V):", Vmag_phases_CA_rms_PV)
print ("RMS three-phase active power at the PV (W):", Pmag_3phase_PV)
print ("RMS  three-phase active power at the PV (VAr):", Qmag_3phase_PV)
print ("Active power of phase A in the PV (W):", Pmag_phase_A_rms_PV)
print ("Active power of phase B in the PV (W):", Pmag_phase_B_rms_PV)
print ("Active power of phase C in the PV (W):", Pmag_phase_C_rms_PV)
print ("Reactive power of phase A in the PV (VAr):", Qmag_phase_A_rms_PV)
print ("Reactive power of phase B in the PV (VAr):", Qmag_phase_B_rms_PV)
print ("Reactive power of phase C in the PV (VAr):", Qmag_phase_C_rms_PV)

print ("Load RMS Current at phase A(A):", Imag_phase_A_rms_Load)
print ("Load RMS Current at phase B(A):", Imag_phase_B_rms_Load)
print ("Load RMS Current at phase C(A):", Imag_phase_C_rms_Load)
print ("Load RMS Voltage at phase A(V):", Vmag_phase_A_rms_Load)
print ("Load RMS Voltage at phase B(V):", Vmag_phase_B_rms_Load)
print ("Load RMS Voltage at phase C(V):", Vmag_phase_C_rms_Load)
print ("Load RMS Voltages at phases AB (V):", Vmag_phases_AB_rms_Load)
print ("Load RMS Voltages at phases BC (V):", Vmag_phases_BC_rms_Load)
print ("Load RMS Voltages at phases CA (V):", Vmag_phases_CA_rms_Load)
print ("RMS three-phase active power at the Load (W):", Pmag_3phase_Load)
print ("RMS  three-phase active power at the Load (VAr):", Qmag_3phase_Load)
print ("Active power of phase A in the Load (W):", Pmag_phase_A_rms_Load)
print ("Active power of phase B in the Load (W):", Pmag_phase_B_rms_Load)
print ("Active power of phase C in the Load (W):", Pmag_phase_C_rms_Load)
print ("Reactive power of phase A in the Load (VAr):", Qmag_phase_A_rms_Load)
print ("Reactive power of phase B in the Load (VAr):", Qmag_phase_B_rms_Load)
print ("Reactive power of phase C in the Load (VAr):", Qmag_phase_C_rms_Load)

print ("PCC RMS Current at phase A(A):", Imag_phase_A_rms_PCC)
print ("PCC RMS Current at phase B(A):", Imag_phase_B_rms_PCC)
print ("PCC RMS Current at phase C(A):", Imag_phase_C_rms_PCC)
print ("PCC RMS Voltage at phase A(V):", Vmag_phase_A_rms_PCC)
print ("PCC RMS Voltage at phase B(V):", Vmag_phase_B_rms_PCC)
print ("PCC RMS Voltage at phase C(V):", Vmag_phase_C_rms_PCC)
print ("PCC RMS Voltages at phases AB (V):", Vmag_phases_AB_rms_PCC)
print ("PCC RMS Voltages at phases BC (V):", Vmag_phases_BC_rms_PCC)
print ("PCC RMS Voltages at phases CA (V):", Vmag_phases_CA_rms_PCC)
print ("RMS three-phase active power at the PCC (W):", Pmag_3phase_PCC)
print ("RMS three-phase active power at the PCC (VAr):", Qmag_3phase_PCC)
print ("Active power of phase A in the PCC (W):", Pmag_phase_A_rms_PCC)
print ("Active power of phase B in the PCC (W):", Pmag_phase_B_rms_PCC)
print ("Active power of phase C in the PCC (W):", Pmag_phase_C_rms_PCC)
print ("Reactive power of phase A in the PCC (VAr):", Qmag_phase_A_rms_PCC)
print ("Reactive power of phase B in the PCC (VAr):", Qmag_phase_B_rms_PCC)
print ("Reactive power of phase C in the PCC (VAr):", Qmag_phase_C_rms_PCC)

# and end script
hil.end_script_by_user()





