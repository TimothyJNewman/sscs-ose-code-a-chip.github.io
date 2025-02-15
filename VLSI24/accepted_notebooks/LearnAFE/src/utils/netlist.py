import subprocess


def write_netlist_AC(paras, filepath):
    with open(filepath, 'w') as f:
        f.write(
            "** sch_path: /AFE_Config/Sch/DSF_BPF.sch\n"
            "**.subckt DSF_BPF\n"
            "XM1 VOP V20 VSS VSS sky130_fd_pr__nfet_01v8 L=LM2 W=WM2 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM2 V11 net4 VSS VSS sky130_fd_pr__nfet_01v8 L=L2 W=W2 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM3 V20 V20 VSS VSS sky130_fd_pr__nfet_01v8 L=LM2 W=WM2 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "V1 VDD GND VDD\n"
            "V2 VSS GND 0\n"
            "I0 VDD V20 %s\n"
            "XC2 net4 VON sky130_fd_pr__cap_mim_m3_1 W=%s L=%s MF=1 m=1\n"
            "V3 VI VSS dc 0 ac 1 sin 0 vi fi\n"
            "V4 net1 VSS VB\n"
            "VI3 net4 VOP 0\n"
            ".save i(vi3)\n"
            "XM4 net3 V10 VDD VDD sky130_fd_pr__pfet_01v8 L=LM1 W=WM1 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "E1 VIP net1 VI VSS 0.5\n"
            "E2 VIN net1 VSS VI 0.5\n"
            "E3 VO VSS VO1 VO2 1\n"
            "XM5 net2 V10 VDD VDD sky130_fd_pr__pfet_01v8 L=LM1 W=WM1 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM6 V10 V10 VDD VDD sky130_fd_pr__pfet_01v8 L=LM1 W=WM1 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "I1 V10 VSS %s\n"
            "XM7 VON V20 VSS VSS sky130_fd_pr__nfet_01v8 L=LM2 W=WM2 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM8 net4 VIP V11 V11 sky130_fd_pr__pfet_01v8 L=L1 W=W1 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM9 VON VIN net2 net2 sky130_fd_pr__pfet_01v8 L=L1 W=W1 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XC1 V11 net2 sky130_fd_pr__cap_mim_m3_1 W=%s L=%s MF=1 m=1\n"
            "VI1 net3 V11 0\n"
            ".save i(vi1)\n"
            "XM10 net2 VON VSS VSS sky130_fd_pr__nfet_01v8 L=L2 W=W2 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM11 net5 V30 VDD VDD sky130_fd_pr__pfet_01v8 L=LM3 W=WM3 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM12 VO2 V30 VDD VDD sky130_fd_pr__pfet_01v8 L=LM3 W=WM3 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM13 V30 V30 VDD VDD sky130_fd_pr__pfet_01v8 L=LM3 W=WM3 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "I2 V30 VSS I_3\n"
            "VI2 net5 VO1 0\n"
            ".save i(vi2)\n"
            "XM14 VSS VOP VO1 VO1 sky130_fd_pr__pfet_01v8 L=L3 W=W3 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM15 VSS VON VO2 VO2 sky130_fd_pr__pfet_01v8 L=L3 W=W3 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "**** begin user architecture code\n"
            "\n"
            ".param mc_mm_switch=0\n"
            ".param mc_pr_switch=0\n"
            ".include /usr/local/share/pdk/sky130A/libs.tech/ngspice/corners/tt.spice\n"
            ".include /usr/local/share/pdk/sky130A/libs.tech/ngspice/r+c/res_typical__cap_typical.spice\n"
            ".include /usr/local/share/pdk/sky130A/libs.tech/ngspice/r+c/res_typical__cap_typical__lin.spice\n"
            ".include /usr/local/share/pdk/sky130A/libs.tech/ngspice/corners/tt/specialized_cells.spice\n"
            "\n"
            ".param VDD=1.8 %s=%.3fn %s=%.3fn I_3=1n VB=0.6 vi=0.5 fi=100 WM1=1 LM1=10 WM2=1 LM2=10 WM3=1 LM3=10 W1=1 L1=10 W2=1 L2=10 W3=1 L3=10 %s=%.1f %s=%.1f %s=%.1f %s=%.1f\n"
            ".include AFE_Config/SpiceAC/para.spice\n"
            "\n"
            ".control\n"
            "run\n"
            "save all\n"
            "\n"
            "op\n"
            "*print V(V10) V(V11) V(V20) V(VOP)\n"
            "*print i(VI1) i(VI3)\n"
            "*print V(V30) V(VO1)\n"
            "*print i(VI2)\n"
            "*wrdata IDD1.txt i(V1)\n"
            "\n"
            "ac dec 1000 1 1e4\n"
            "*plot db(V(VO)/V(VI))\n"
            "wrdata AFE_Config/SpiceAC/%s.txt db(V(VO)/V(VI))\n"
            "\n"
            "*noise V(VO) V3 dec 100 1 1e4\n"
            "*setplot noise1\n"
            "*plot inoise_spectrum\n"
            "*plot onoise_spectrum\n"
            "*wrdata BPF_IRN.txt inoise_spectrum\n"
            "*wrdata BPF_ORN.txt onoise_spectrum\n"
            "\n"
            "*tran 20u 10\n"
            "*plot V(VO)\n"
            "*wrdata BFP_TVO.txt V(VO)\n"
            "*fourier 100 vo\n"
            "*let idx = 2\n"
            "*let sum_mag_square = 0\n"
            "*while idx < 10\n"
            "*    let mag = fourier11[1][idx]\n"
            "*    let sum_mag_square = sum_mag_square + mag * mag\n"
            "*    let idx = idx + 1\n"
            "*end\n"
            "*let root_sum_mag_square = sqrt(sum_mag_square)\n"
            "*let thd = root_sum_mag_square / fourier11[1][1] * 100\n"
            "*print thd\n"
            "*wrdata THD.txt thd\n"
            "\n"
            ".endc\n"
            "\n"
            "**** end user architecture code\n"
            "**.ends\n"
            ".GLOBAL GND\n"
            ".end\n" 
            % paras
        )


def write_netlist_Trans(paras, filepath):
    with open(filepath, 'w') as f:
        f.write(
            "** sch_path: /AFE_Config/Sch/DSF_BPF.sch\n"
            "**.subckt DSF_BPF\n"
            "XM1 VOP V20 VSS VSS sky130_fd_pr__nfet_01v8 L=LM2 W=WM2 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM2 V11 net4 VSS VSS sky130_fd_pr__nfet_01v8 L=L2 W=W2 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM3 V20 V20 VSS VSS sky130_fd_pr__nfet_01v8 L=LM2 W=WM2 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "V1 VDD GND VDD\n"
            "V2 VSS GND 0\n"
            "I0 VDD V20 %s\n"
            "XC2 net4 VON sky130_fd_pr__cap_mim_m3_1 W=%s L=%s MF=1 m=1\n"
            "V4 net1 VSS VB\n"
            "VI3 net4 VOP 0\n"
            ".save i(vi3)\n"
            "XM4 net3 V10 VDD VDD sky130_fd_pr__pfet_01v8 L=LM1 W=WM1 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "E1 VIP net1 VI VSS 0.5\n"
            "E2 VIN net1 VSS VI 0.5\n"
            "E3 VO VSS VO1 VO2 1\n"
            "XM5 net2 V10 VDD VDD sky130_fd_pr__pfet_01v8 L=LM1 W=WM1 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM6 V10 V10 VDD VDD sky130_fd_pr__pfet_01v8 L=LM1 W=WM1 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "I1 V10 VSS %s\n"
            "XM7 VON V20 VSS VSS sky130_fd_pr__nfet_01v8 L=LM2 W=WM2 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM8 net4 VIP V11 V11 sky130_fd_pr__pfet_01v8 L=L1 W=W1 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM9 VON VIN net2 net2 sky130_fd_pr__pfet_01v8 L=L1 W=W1 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XC1 V11 net2 sky130_fd_pr__cap_mim_m3_1 W=%s L=%s MF=1 m=1\n"
            "VI1 net3 V11 0\n"
            ".save i(vi1)\n"
            "XM10 net2 VON VSS VSS sky130_fd_pr__nfet_01v8 L=L2 W=W2 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM11 net5 V30 VDD VDD sky130_fd_pr__pfet_01v8 L=LM3 W=WM3 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM12 VO2 V30 VDD VDD sky130_fd_pr__pfet_01v8 L=LM3 W=WM3 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM13 V30 V30 VDD VDD sky130_fd_pr__pfet_01v8 L=LM3 W=WM3 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "I2 V30 VSS I_3\n"
            "VI2 net5 VO1 0\n"
            ".save i(vi2)\n"
            "XM14 VSS VOP VO1 VO1 sky130_fd_pr__pfet_01v8 L=L3 W=W3 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "XM15 VSS VON VO2 VO2 sky130_fd_pr__pfet_01v8 L=L3 W=W3 nf=1 ad='int((nf+1)/2) * W/nf * 0.29' as='int((nf+2)/2) * W/nf * 0.29' pd='2*int((nf+1)/2) * (W/nf + 0.29)'\n"
            "+ ps='2*int((nf+2)/2) * (W/nf + 0.29)' nrd='0.29 / W' nrs='0.29 / W' sa=0 sb=0 sd=0 mult=1 m=1\n"
            "**** begin user architecture code\n"
            "\n"
            ".param mc_mm_switch=0\n"
            ".param mc_pr_switch=0\n"
            ".include /usr/local/share/pdk/sky130A/libs.tech/ngspice/corners/tt.spice\n"
            ".include /usr/local/share/pdk/sky130A/libs.tech/ngspice/r+c/res_typical__cap_typical.spice\n"
            ".include /usr/local/share/pdk/sky130A/libs.tech/ngspice/r+c/res_typical__cap_typical__lin.spice\n"
            ".include /usr/local/share/pdk/sky130A/libs.tech/ngspice/corners/tt/specialized_cells.spice\n"
            "\n"
            ".param VDD=1.8 %s=%.3fn %s=%.3fn I_3=1n VB=0.6 vi=0.5 fi=100 WM1=1 LM1=10 WM2=1 LM2=10 WM3=1 LM3=10 W1=1 L1=10 W2=1 L2=10 W3=1 L3=10 %s=%.1f %s=%.1f %s=%.1f %s=%.1f\n"
            ".include AFE_Config/SpiceTrans/para.spice\n"
            "\n"
            ".model fsrc filesource(file=\"%s\" timeoffset=0 timescale=1\n"
            "+                                           amploffset=[0] amplscale=[1.0]\n"
            "+                                           timerelative=false amplstep=false)\n"
            "ain %%v[VI] fsrc\n"
            ".control\n"
            "run\n"
            "save all\n"
            "\n"
            "op\n"
            "*print V(V10) V(V11) V(V20) V(VOP)\n"
            "*print i(VI1) i(VI3)\n"
            "*print V(V30) V(VO1)\n"
            "*print i(VI2)\n"
            "\n"
            "*plot db(V(VO)/V(VI))"
            "\n"
            "*noise V(VO) V3 dec 100 1 1e4\n"
            "*setplot noise1\n"
            "*plot inoise_spectrum\n"
            "*plot onoise_spectrum\n"
            "*wrdata BPF_IRN.txt inoise_spectrum\n"
            "*wrdata BPF_ORN.txt onoise_spectrum\n"
            "\n"
            "tran 50u 1\n"
            "let lin-tstart=0\n"
            "let lin-tstop=1\n"
            "let lin-tstep=50u\n"
            "linearize V(VO)\n"
            "wrdata AFE_Config/SpiceTrans/%s.txt V(VO)"
            "\n"
            "*tran 20u 10\n"
            "*plot V(VO)\n"
            "*wrdata BFP_TVO.txt V(VO)\n"
            "*fourier 100 vo\n"
            "*let idx = 2\n"
            "*let sum_mag_square = 0\n"
            "*while idx < 10\n"
            "*    let mag = fourier11[1][idx]\n"
            "*    let sum_mag_square = sum_mag_square + mag * mag\n"
            "*    let idx = idx + 1\n"
            "*end\n"
            "*let root_sum_mag_square = sqrt(sum_mag_square)\n"
            "*let thd = root_sum_mag_square / fourier11[1][1] * 100\n"
            "*print thd\n"
            "*wrdata THD.txt thd\n"
            "\n"
            ".endc\n"
            "\n"
            "**** end user architecture code\n"
            "**.ends\n"
            ".GLOBAL GND\n"
            ".end\n"
            % paras
        )


def write_paras(paras, filepath):
    filepath = filepath + '/para.spice'
    with open(filepath, 'w') as f:
        f.write(
            ".param I_1_1=%.3fn I_2_1=%.3fn W_C1_1=%.1f L_C1_1=%.1f W_C2_1=%.1f L_C2_1=%.1f\n"
            ".param I_1_2=%.3fn I_2_2=%.3fn W_C1_2=%.1f L_C1_2=%.1f W_C2_2=%.1f L_C2_2=%.1f\n"
            ".param I_1_3=%.3fn I_2_3=%.3fn W_C1_3=%.1f L_C1_3=%.1f W_C2_3=%.1f L_C2_3=%.1f\n"
            ".param I_1_4=%.3fn I_2_4=%.3fn W_C1_4=%.1f L_C1_4=%.1f W_C2_4=%.1f L_C2_4=%.1f\n"
            ".param I_1_5=%.3fn I_2_5=%.3fn W_C1_5=%.1f L_C1_5=%.1f W_C2_5=%.1f L_C2_5=%.1f\n"
            ".param I_1_6=%.3fn I_2_6=%.3fn W_C1_6=%.1f L_C1_6=%.1f W_C2_6=%.1f L_C2_6=%.1f\n"
            ".param I_1_7=%.3fn I_2_7=%.3fn W_C1_7=%.1f L_C1_7=%.1f W_C2_7=%.1f L_C2_7=%.1f\n"
            ".param I_1_8=%.3fn I_2_8=%.3fn W_C1_8=%.1f L_C1_8=%.1f W_C2_8=%.1f L_C2_8=%.1f\n"
            ".param I_1_9=%.3fn I_2_9=%.3fn W_C1_9=%.1f L_C1_9=%.1f W_C2_9=%.1f L_C2_9=%.1f\n"
            ".param I_1_10=%.3fn I_2_10=%.3fn W_C1_10=%.1f L_C1_10=%.1f W_C2_10=%.1f L_C2_10=%.1f\n"
            ".param I_1_11=%.3fn I_2_11=%.3fn W_C1_11=%.1f L_C1_11=%.1f W_C2_11=%.1f L_C2_11=%.1f\n"
            ".param I_1_12=%.3fn I_2_12=%.3fn W_C1_12=%.1f L_C1_12=%.1f W_C2_12=%.1f L_C2_12=%.1f\n"
            ".param I_1_13=%.3fn I_2_13=%.3fn W_C1_13=%.1f L_C1_13=%.1f W_C2_13=%.1f L_C2_13=%.1f\n"
            ".param I_1_14=%.3fn I_2_14=%.3fn W_C1_14=%.1f L_C1_14=%.1f W_C2_14=%.1f L_C2_14=%.1f\n"
            ".param I_1_15=%.3fn I_2_15=%.3fn W_C1_15=%.1f L_C1_15=%.1f W_C2_15=%.1f L_C2_15=%.1f\n"
            ".param I_1_16=%.3fn I_2_16=%.3fn W_C1_16=%.1f L_C1_16=%.1f W_C2_16=%.1f L_C2_16=%.1f\n"
            "\n"
            ".param VDD=1.8 I_3=1n VB=0.6 vi=0.05 fi=100 WM1=4 LM1=10 WM2=1 LM2=10 WM3=2 LM3=10 W1=5 L1=10 W2=5 L2=2 W3=1 L3=10\n"
            % paras
        )


def run_netlist(netlist_path): 
    p = subprocess.Popen(['ngspice', '-b', netlist_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out, err