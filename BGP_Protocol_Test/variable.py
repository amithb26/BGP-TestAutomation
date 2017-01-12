Devices = ['R1','R2','R3','R4','R5']





Links_of_R1 = ["Link_R1_R2_1","Link_R1_R3_1"]
Links_of_R2 = ["Link_R1_R2_1","Link_R2_R4_1"]                                
Links_of_R3 = ["Link_R1_R3_1","Link_R3_R5_1"]
Links_of_R4 = ["Link_R2_R4_1"]
Links_of_R5 = ["Link_R3_R5_1"]



#Autonomous systems
# Autonomous system = ['Device1',......] connected in AS2
AS1 = ['R5']
AS2 = ['R1','R2','R3']
AS3 = ['R4']




#AS2
Process_id = 1
Area1 = 0
#Networks_connected_to_('Device') = ["<NID>  <WCM>",.......,"<Loopback address>  <WCM>"] 
Networks_connected_to_R1 = ["192.168.23.0  0.0.0.255","192.168.34.0  0.0.0.255", "3.3.3.0  0.0.0.255"]
Networks_connected_to_R2 = ["192.168.23.0  0.0.0.255","2.2.2.0  0.0.0.255"]
Networks_connected_to_R3 = ["192.168.34.0  0.0.0.255","4.4.4.0  0.0.0.255"]

#IBGP
AS_id = 2
R2_interface = "2.2.2.2"
R3_interface = "4.4.4.4"
 
#EBGP
R2_AS_id = 2
R2_neighbor_AS_id = 1
R2_einterface = "192.168.12.1"


R4_AS_id = 1
R4_neighbor_AS_id = 2
R4_einterface = "192.168.12.2"


R3_AS_id = 2
R3_neighbor_AS_id = 3
R3_einterface = "192.168.45.5"


R5_AS_id = 3
R5_neighbor_AS_id = 2
R5_einterface = "192.168.45.4"

#advertising Loopback

R4_interface = "1.1.1.0"
R4_mask = "255.255.255.0"


R5_interface = "5.5.5.0"
R5_mask = "255.255.255.0"			


R2_lointerface = "2.2.2.2"
R3_lointerface = "4.4.4.4"






















