import typhoon.api.hil as hil 
from typhoon.api import hil as hil

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

#Contactores fechados (Rede e PAC)
hil.set_contactor('PCC.S1', swControl=True, swState=True) #PAC fechado 
hil.set_scada_input_value('Grid UI1.Connect', 1.0) #Contactor rede fechado

#Contatores das componentes 
hil.set_scada_input_value('Battery ESS (Generic) UI1.Enable', 1.0) #Contator da BESS Fechado
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Enable', 1.0) #Contator do DG fechado
hil.set_scada_input_value('PV Power Plant (Generic) UI1.Enable', 1.0) #Contator do PV fechado
hil.set_scada_input_value('Variable Load (Generic) UI1.Enable', 1.0) #Contator da carga fechado 

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
#BESS no modo seguidor de rede
hil.set_scada_input_value('Battery ESS (Generic) UI1.Converter mode', 0.0)

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
#GD no modo seguidor de rede
hil.set_scada_input_value('Diesel Genset (Generic) UI1.Operation mode', 0.0)


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


#Listas das mediçoes BESS
IA_RMS_BESS = []
IB_RMS_BESS = []
IC_RMS_BESS = []
VA_RMS_BESS = []
VB_RMS_BESS = []
VC_RMS_BESS = []
VAB_RMS_BESS = []
VBC_RMS_BESS = []
VCA_RMS_BESS = []
P_meas_BESS = []
Q_meas_BESS = []
Pativa_A_BESS = []
Pativa_B_BESS = []
Pativa_C_BESS = []
SOC = []
Preactiva_A_BESS = []
Preactiva_B_BESS = []
Preactiva_C_BESS = []

#Listas das mediçoes DG
IA_RMS_DG = []
IB_RMS_DG = []
IC_RMS_DG = []
VA_RMS_DG = []
VB_RMS_DG = []
VC_RMS_DG = []
VAB_RMS_DG = []
VBC_RMS_DG = []
VCA_RMS_DG = []
DG_RPM = []
DG_Pmeas = []
DG_Qmeas = []

#Listas das mediçoes PV
IA_RMS_PV = []
IB_RMS_PV = []
IC_RMS_PV = []
VA_RMS_PV = []
VB_RMS_PV = []
VC_RMS_PV = []
VAB_RMS_PV = []
VBC_RMS_PV = []
VCA_RMS_PV = []
PV_P_FaseA = []
PV_P_FaseB = []
PV_P_FaseC = []
PV_Q_FaseA = []
PV_Q_FaseB = []
PV_Q_FaseC = []
PV_P_meas = []
PV_Q_meas = []

#Lista das mediçoes Carga
IA_RMS_Carga = []
IB_RMS_Carga = []
IC_RMS_Carga = []
VA_RMS_Carga = []
VB_RMS_Carga = []
VC_RMS_Carga = []
VAB_RMS_Carga = []
VBC_RMS_Carga = []
VCA_RMS_Carga = []
Carga_Pmeas = []
Carga_Qmeas = []

#Lista das medicoes do PCC
IA_RMS_PCC = []
IB_RMS_PCC = []
IC_RMS_PCC = []
VA_RMS_PCC = []
VB_RMS_PCC = []
VC_RMS_PCC = []
VAB_RMS_PCC = []
VBC_RMS_PCC = []
VCA_RMS_PCC = []

#Lista das medicoes Rede
Tensão_rede_Fa = []
Tensão_rede_Fb = []
Tensão_rede_Fc = []
Frequencia_rede = []
Rede_Pmeas = []
Rede_Qmeas = []
Rede_Vrms = []

#Le passo de simulção
Execute_simulation = simulation_step
cont = 0

while (Execute_simulation <= 10):
    rest_divi = cont % 200000

    if rest_divi == 0:
        #Realiza as leituras das mediçoes a cada 2.5seg

        #Leitura das mediçoes (BESS)
        IA_RMS_BESS.append(hil.read_analog_signal(name='Meter (BESS).IA_RMS1'))
        IB_RMS_BESS.append(hil.read_analog_signal(name='Meter (BESS).IB_RMS1'))
        IC_RMS_BESS.append(hil.read_analog_signal(name='Meter (BESS).IC_RMS1'))
        VA_RMS_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VAn_RMS'))
        VB_RMS_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VBn_RMS')) 
        VC_RMS_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VCn_RMS')) 
        VAB_RMS_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VAB_RMS'))
        VBC_RMS_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VBC_RMS'))
        VCA_RMS_BESS.append(hil.read_analog_signal(name='Meter (BESS).Three-phase Meter.VCA_RMS'))
        P_meas_BESS.append(hil.read_analog_signal(name='Battery ESS (Generic) UI1.Pmeas_kW'))
        Q_meas_BESS.append(hil.read_analog_signal(name='Battery ESS (Generic) UI1.Qa_meas_kVAr'))
        Pativa_A_BESS.append(hil.read_analog_signal(name='Battery ESS (Generic) UI1.Pa_meas_kW'))
        Pativa_B_BESS.append(hil.read_analog_signal(name='Battery ESS (Generic) UI1.Pb_meas_kW'))
        Pativa_C_BESS.append(hil.read_analog_signal(name='Battery ESS (Generic) UI1.Pc_meas_kW'))
        SOC.append(hil.read_analog_signal(name='Battery ESS (Generic) UI1.SOC'))
        Preactiva_A_BESS.append(hil.read_analog_signal(name='Battery ESS (Generic) UI1.Qa_meas_kVAr'))
        Preactiva_B_BESS.append(hil.read_analog_signal(name='Battery ESS (Generic) UI1.Qb_meas_kVAr'))
        Preactiva_C_BESS.append(hil.read_analog_signal(name='Battery ESS (Generic) UI1.Qc_meas_kVAr'))

        #Leitura das medicoes do DG
        IA_RMS_DG.append(hil.read_analog_signal(name='Meter (DG).IA_RMS1'))
        IB_RMS_DG.append(hil.read_analog_signal(name='Meter (DG).IB_RMS1'))
        IC_RMS_DG.append(hil.read_analog_signal(name='Meter (DG).IC_RMS1'))
        VA_RMS_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VAn_RMS'))
        VB_RMS_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VBn_RMS'))
        VC_RMS_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VCn_RMS'))
        VAB_RMS_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VAB_RMS'))
        VBC_RMS_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VBC_RMS'))
        VCA_RMS_DG.append(hil.read_analog_signal(name='Meter (DG).Three-phase Meter.VCA_RMS'))
        DG_RPM.append(hil.read_analog_signal(name='Diesel Genset (Generic) UI1.Gen_speed_RPM'))
        DG_Pmeas.append(hil.read_analog_signal(name='Diesel Genset (Generic) UI1.Pmeas_kW'))
        DG_Qmeas.append(hil.read_analog_signal(name='Diesel Genset (Generic) UI1.Qmeas_kVAr'))

        #Leitura das mediçoes (PV)
        IA_RMS_PV.append(hil.read_analog_signal(name='Meter (PV).IA_RMS1'))
        IB_RMS_PV.append(hil.read_analog_signal(name='Meter (PV).IB_RMS1'))
        IC_RMS_PV.append(hil.read_analog_signal(name='Meter (PV).IC_RMS1'))
        VA_RMS_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VAn_RMS'))
        VB_RMS_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VBn_RMS'))
        VC_RMS_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VCn_RMS'))
        VAB_RMS_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VAB_RMS'))
        VBC_RMS_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VBC_RMS'))
        VCA_RMS_PV.append(hil.read_analog_signal(name='Meter (PV).Three-phase Meter.VCA_RMS'))
        PV_P_FaseA.append(hil.read_analog_signal(name='PV Power Plant (Generic) UI1.Pa_meas_kW'))
        PV_P_FaseA.append(hil.read_analog_signal(name='PV Power Plant (Generic) UI1.Pa_meas_kW'))
        PV_P_FaseB.append(hil.read_analog_signal(name='PV Power Plant (Generic) UI1.Pb_meas_kW'))
        PV_P_FaseC.append(hil.read_analog_signal(name='PV Power Plant (Generic) UI1.Pc_meas_kW'))
        PV_Q_FaseA.append(hil.read_analog_signal(name='PV Power Plant (Generic) UI1.Qa_meas_kVAr'))
        PV_Q_FaseB.append(hil.read_analog_signal(name='PV Power Plant (Generic) UI1.Qb_meas_kVAr'))
        PV_Q_FaseC.append(hil.read_analog_signal(name='PV Power Plant (Generic) UI1.Qc_meas_kVAr'))
        PV_P_meas.append(hil.read_analog_signal(name='PV Power Plant (Generic) UI1.Pmeas_kW'))
        PV_Q_meas.append(hil.read_analog_signal(name='PV Power Plant (Generic) UI1.Qmeas_kVAr'))

        #Leitura das mediçoes (Load)
        IA_RMS_Carga.append(hil.read_analog_signal(name='Meter (Load).IA_RMS1'))
        IB_RMS_Carga.append(hil.read_analog_signal(name='Meter (Load).IB_RMS1'))
        IC_RMS_Carga.append(hil.read_analog_signal(name='Meter (Load).IC_RMS1'))
        VA_RMS_Carga.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VAn_RMS'))
        VB_RMS_Carga.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VBn_RMS'))
        VC_RMS_Carga.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VCn_RMS'))
        VAB_RMS_Carga.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VAB_RMS'))
        VBC_RMS_Carga.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VBC_RMS'))
        VCA_RMS_Carga.append(hil.read_analog_signal(name='Meter (Load).Three-phase Meter.VCA_RMS'))
        Carga_Pmeas.append(hil.read_analog_signal(name='Variable Load (Generic) UI1.Pmeas_kW'))
        Carga_Qmeas.append(hil.read_analog_signal(name='Variable Load (Generic) UI1.Qmeas_kVAr'))
        
        #Leitura das mediçoes (PCC)
        IA_RMS_PCC.append(hil.read_analog_signal(name='Meter (PCC).IA_RMS1'))
        IB_RMS_PCC.append(hil.read_analog_signal(name='Meter (PCC).IB_RMS1'))
        IC_RMS_PCC.append(hil.read_analog_signal(name='Meter (PCC).IC_RMS1'))
        VA_RMS_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VAn_RMS'))
        VB_RMS_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VBn_RMS'))
        VC_RMS_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VCn_RMS'))
        VAB_RMS_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VAB_RMS'))
        VBC_RMS_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VBC_RMS'))
        VCA_RMS_PCC.append(hil.read_analog_signal(name='Meter (PCC).Three-phase Meter.VCA_RMS'))

        #Leitura das mediçoes (Rede)
        Tensão_rede_Fa.append(hil.read_analog_signal(name='Grid1.Va'))
        Tensão_rede_Fb.append(hil.read_analog_signal(name='Grid1.Vb'))
        Tensão_rede_Fc.append(hil.read_analog_signal(name='Grid1.Vc'))
        Frequencia_rede.append(hil.read_analog_signal(name='Grid UI1.Fmeas_Hz'))
        Rede_Pmeas.append(hil.read_analog_signal(name='Grid UI1.Pmeas_kW'))
        Rede_Qmeas.append(hil.read_analog_signal(name='Grid UI1.Qmeas_kVAr'))
        Rede_Vrms.append(hil.read_analog_signal(name='Grid UI1.Vrms_meas_kV'))
        
    #Incrementando o passo da execução
    Execute_simulation += simulation_step
    cont += 1

# Parar a simulação
hil.stop_simulation()
print ("Stop simulation")


#Visualização na consola
print ("Corrente RMS Fase A na Bateria (A):", IA_RMS_BESS)
print ("Corrente RMS Fase B na Bateria (A):", IB_RMS_BESS)
print ("Corrente RMS Fase C na Bateria (A):", IC_RMS_BESS)
print ("Tensão RMS Fase A na Bateria (V):", VA_RMS_BESS)
print ("Tensão RMS Fase B na Bateria (V):", VB_RMS_BESS)
print ("Tensão RMS Fase C na Bateria (V):", VC_RMS_BESS)
print ("Tensão RMS Fases AB na Bateria (V):", VAB_RMS_BESS)
print ("Tensão RMS Fases BC na Bateria (V):", VBC_RMS_BESS)
print ("Tensão RMS Fases CA na Bateria (V):", VCA_RMS_BESS)
print ("Potência ativa medida na Bateria (kW):", P_meas_BESS)
print ("Potência reativa medida na Bateria (kVAr):", Q_meas_BESS)
print ("Potência ativa da fase A na Bateria (kW):", Pativa_A_BESS)
print ("Potência ativa da fase B na Bateria (kW):", Pativa_B_BESS)
print ("Potência ativa da fase C na Bateria (kW):", Pativa_C_BESS)
print ("Potência reativa da fase A na Bateria (kVAr):", Preactiva_A_BESS)
print ("Potência reativa da fase B na Bateria (kVAr):", Preactiva_B_BESS)
print ("Potência reativa da fase C na Bateria (kVAr):", Preactiva_C_BESS)
print ("SOC (%):", SOC)
#print ("Potência ativa medida na Bateria (kW):", P_meas_BESS)
print ("Corrente RMS Fase A no Diesel Genset (A):", IA_RMS_DG)
print ("Corrente RMS Fase B no Diesel Genset (A):", IB_RMS_DG)
print ("Corrente RMS Fase C no Diesel Genset (A):", IC_RMS_DG)
print ("Tensão RMS Fase A no Disel Genset (V):", VA_RMS_DG)
print ("Tensão RMS Fase B no Disel Genset (V):", VB_RMS_DG)
print ("Tensão RMS Fase C no Disel Genset (V):", VC_RMS_DG)
print ("Tensão RMS Fases AB no Diesel Genset (V):", VAB_RMS_DG)
print ("Tensão RMS Fases BC no Diesel Genset (V):", VBC_RMS_DG)
print ("Tensão RMS Fases CA no Diesel Genset (V):", VCA_RMS_DG)
print ("RPMs no Diesel Genset:", DG_RPM)
print ("Potência ativa medida no Diesel Genset (kW):", DG_Pmeas)
print ("Potência reativa medida no Diesel Genset (kW):", DG_Qmeas)
print ("Corrente RMS Fase A no PV (A):", IA_RMS_PV)
print ("Corrente RMS Fase B no PV (A):", IB_RMS_PV)
print ("Corrente RMS Fase C no PV (A):", IC_RMS_PV)
print ("Tensão RMS Fase A no PV (V):", VA_RMS_PV)
print ("Tensão RMS Fase B no PV (V):", VB_RMS_PV)
print ("Tensão RMS Fase C no PV (V):", VC_RMS_PV)
print ("Tensão RMS Fases AB no PV (V):", VAB_RMS_PV)
print ("Tensão RMS Fases BC no PV (V):", VBC_RMS_PV)
print ("Tensão RMS Fases CA no PV (V):", VCA_RMS_PV)
print ("Potência ativa da fase A no PV (kW):", PV_P_FaseA)
print ("Potência ativa da fase B no PV (kW):", PV_P_FaseB)
print ("Potência ativa da fase c no PV (kW):", PV_P_FaseC)
print ("Potência reativa da fase A no PV (kW):", PV_Q_FaseA)
print ("Potência reativa da fase B no PV (kW):", PV_Q_FaseB)
print ("Potência reativa da fase c no PV (kW):", PV_Q_FaseC)
print ("Potência ativa medida no PV (kW):", PV_P_meas)
print ("Potência reativa medida no PV (kVAr):", PV_Q_meas)
print ("Potência ativa medida na carga (kW):", Carga_Pmeas)
print ("Potência reativa medida na carga (kVAr):", Carga_Qmeas)
print ("Corrente RMS Fase A no PCC (A):", IA_RMS_PCC)
print ("Corrente RMS Fase B no PCC (A):", IB_RMS_PCC)
print ("Corrente RMS Fase C no PCC (A):", IC_RMS_PCC)
print ("Tensão RMS Fase A no PCC (V):", VA_RMS_PCC)
print ("Tensão RMS Fase B no PCC (V):", VB_RMS_PCC)
print ("Tensão RMS Fase C no PCC (V):", VC_RMS_PCC)
print ("Tensão RMS Fases AB no PCC (V):", VAB_RMS_PCC)
print ("Tensão RMS Fases BC no PCC (V):", VBC_RMS_PCC)
print ("Tensão RMS Fases CA no PCC (V):", VCA_RMS_PCC)
print ("Tensão na rede fase A:", Tensão_rede_Fa)
print ("Tensão na rede fase B:", Tensão_rede_Fb)
print ("Tensão na rede fase C:", Tensão_rede_Fc)
print ("Frequencia da rede (Hz): ", Frequencia_rede)
print ("Potência ativa medida na Rede (kW):", Rede_Pmeas)
print ("Potência reativa medida na Rede (kVAr):", Rede_Qmeas)
print ("Tensão RMS na rede:", Rede_Vrms)
#print ("BESS_ALARM:", BESS_ALARM)
#print (simulation_step)

# and end script
hil.end_script_by_user()


