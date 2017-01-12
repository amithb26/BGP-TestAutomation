*** Settings ***
Documentation     Resource file containing all the PYTHON API implementations.
Library           setup_actions.py
Library           Devices.py
Library           OSPF.py
Library           IBGP.py
Library		  operational_ph.py
Library           String
Variables         variable.py

*** Variables ***

@{Devices} =      R1    R2    R3    R4    R5   
${ELEMENT}

*** Keywords ***

Setup Actions

    Log To Console            Setup Actions done here

    Run Keyword and Continue On Failure    connect_all    enable

    
Teardown Actions

    Log To Console            Teardown Actions done here

    Log To Console            Unconfiguring IP_Address 

    Run Keyword and Continue On Failure    set_IP     R1    ${Links_of_R1}    unconfigure
    Log To Console            IP_Address unconfigured in R1
    Run Keyword and Continue On Failure    set_IP     R2    ${Links_of_R2}    unconfigure
    Log To Console            IP_Address unconfigured in R2
    Run Keyword and Continue On Failure    set_IP     R3    ${Links_of_R3}    unconfigure
    Log To Console            IP_Address unconfigured in R3 
    Run Keyword and Continue On Failure    set_IP     R4    ${Links_of_R4}    unconfigure
    Log To Console            IP_Address unconfigured in R4
    Run Keyword and Continue On Failure    set_IP     R5    ${Links_of_R5}    unconfigure
    Log To Console            IP_Address unconfigured in R5
		
    Log To Console            Disabling password and unsetting hostname
 
    Run Keyword and Continue On Failure    connect_all    disable
    
Configure IP addresses as per the topology
    
    Log To Console            Configuring IP_Address 
  
Configure ip address
 
    ${result}=    Run Keyword and Continue On Failure    set_IP     R1    ${Links_of_R1}    configure
    Run Keyword If    ${result}==False    FAIL    Configuring IP Address on R1 has failed
    Log To Console            IP_Address configured in R1

    
    ${result}=    Run Keyword and Continue On Failure    set_IP     R2    ${Links_of_R2}    configure
    Run Keyword If    ${result}==False    FAIL    Configuring IP Address on R2 has failed
    Log To Console            IP_Address configured in R2

    
    ${result}=    Run Keyword and Continue On Failure    set_IP     R3    ${Links_of_R3}    configure
    Run Keyword If    ${result}==False    FAIL    Configuring IP Address on R3 has failed
    Log To Console            IP_Address configured in R3

    ${result}=    Run Keyword and Continue On Failure    set_IP     R4    ${Links_of_R4}    configure
    Run Keyword If    ${result}==False    FAIL    Configuring IP Address on R4 has failed
    Log To Console            IP_Address configured in R4

    ${result}=    Run Keyword and Continue On Failure    set_IP     R5    ${Links_of_R5}    configure
    Run Keyword If    ${result}==False    FAIL    Configuring IP Address on R5 has failed
    Log To Console            IP_Address configured in R5

Set loopback interface 

    Log To Console            Setting Loopback interface

    ${result}=    Run Keyword and Continue On Failure    set_loopback     R1    set
    Run Keyword If    ${result}==False    FAIL    Configuring Loopback IP on R1 has failed    
    Log To Console            Loopback_Address configured in R1

    ${result}=    Run Keyword and Continue On Failure    set_loopback     R2    set
    Run Keyword If    ${result}==False    FAIL    Configuring Loopback IP on R2 has failed    
    Log To Console            Loopback_Address configured in R2

    ${result}=    Run Keyword and Continue On Failure    set_loopback     R3    set
    Run Keyword If    ${result}==False    FAIL    Configuring Loopback IP on R3 has failed    
    Log To Console            Loopback_Address configured in R3

    ${result}=    Run Keyword and Continue On Failure    set_loopback     R4    set
    Run Keyword If    ${result}==False    FAIL    Configuring Loopback IP on R4 has failed    
    Log To Console            Loopback_Address configured in R4
    
    ${result}=    Run Keyword and Continue On Failure    set_loopback     R5    set
    Run Keyword If    ${result}==False    FAIL    Configuring Loopback IP on R5 has failed    
    Log To Console            Loopback_Address configured in R5


Configure OSPF within AS2 to advertise the connected networks

    Log To Console             Configuring OSPF 

Enable OSPF in devices present in AS2 and set the ospf neighbors

    ${result}=    Run Keyword and Continue On Failure    Configure_ospf    R1    ${Process_id}    ${Networks_connected_to_R1}    ${Area1}    enable
    Run Keyword If    ${result}==False    FAIL    Configuring ospf on R1 has failed
    Log To Console            OSPF configured in R1


    ${result}=    Run Keyword and Continue On Failure    Configure_ospf    R2    ${Process_id}    ${Networks_connected_to_R2}    ${Area1}    enable
    Run Keyword If    ${result}==False    FAIL    Configuring ospf on R2 has failed
    Log To Console            OSPF configured in R2

    ${result}=    Run Keyword and Continue On Failure    Configure_ospf    R3    ${Process_id}    ${Networks_connected_to_R3}    ${Area1}    enable
    Run Keyword If    ${result}==False    FAIL    Configuring ospf on R3 has failed
    Log To Console            OSPF configured in R3


Configure IBGP and source the BGP updates from the loopback0 interfaces

    Log To Console    Setting IBGP between R2 and R3
    

Enable IBGP and advertise the updates from the loopback interface

    ${result}=    Run Keyword and Continue On Failure    Configure_IBGP    R2    ${AS_id}    ${R3_interface}    enable
    Run Keyword If    ${result}==False    FAIL    Configuring ibgp on R2 has failed         
    Log To Console    IBGP configured in R2

    ${result}=    Run Keyword and Continue On Failure    Configure_IBGP    R3    ${AS_id}    ${R2_interface}    enable              
    Run Keyword If    ${result}==False    FAIL    Configuring ibgp on R3 has failed 
    Log To Console    IBGP configured in R3

Enable BGP Synchronisation
    
    Log To Console    Enabling BGP synchronization

Enable synchronisation between border routers

    Run Keyword and Continue On Failure    enable_syn    R2    ${AS_id} 
    Run Keyword and Continue On Failure    enable_syn    R3    ${AS_id}

Configure EBGP and source the BGP updates from the loopback0 interfaces
 
    Log To Console    Configuring EBGP between devices in different autonomous systems

Enable BGP and advertise networks connected outside the autonomous system

    ${result}=    Run Keyword and Continue On Failure    Configure_EBGP    R2    ${R2_AS_id}    ${R2_einterface}    ${R2_neighbor_AS_id}    enable
    Run Keyword If    ${result}==False    FAIL    Configuring ebgp on R2 has failed 
    Log To Console    EBGP configured in R2     
    
    ${result}=    Run Keyword and Continue On Failure    Configure_EBGP    R4    ${R4_AS_id}    ${R4_einterface}    ${R4_neighbor_AS_id}    enable
    Run Keyword If    ${result}==False    FAIL    Configuring ebgp on R4 has failed 
    Log To Console    EBGP configured in R4
    
    ${result}=    Run Keyword and Continue On Failure    Configure_EBGP    R3    ${R3_AS_id}    ${R3_einterface}    ${R3_neighbor_AS_id}    enable
    Run Keyword If    ${result}==False    FAIL    Configuring ebgp on R3 has failed 
    Log To Console    EBGP configured in R3

    ${result}=    Run Keyword and Continue On Failure    Configure_EBGP    R5    ${R5_AS_id}    ${R5_einterface}    ${R5_neighbor_AS_id}    enable
    Run Keyword If    ${result}==False    FAIL    Configuring ebgp on R5 has failed 
    Log To Console    EBGP configured in R5

Advertise loopback interface on AS1 and AS3
    Run Keyword and Continue On Failure    advertising_loopback    R4    ${R4_AS_id}    ${R4_interface}    ${R4_mask}
    Run Keyword and Continue On Failure    advertising_loopback    R5    ${R5_AS_id}    ${R5_interface}    ${R5_mask}

Establish route between R2 and R3
    Run Keyword and Continue On Failure    route    R2    ${R2_AS_id}     ${R3_lointerface}
    Run Keyword and Continue On Failure    route    R3    ${R3_AS_id}     ${R2_lointerface}
     

Redistribute routes from OSPF into BGP
    Log To Console    Redistributing routes from OSPF into BGP
    Run Keyword and Continue On Failure    redistribution    R2    ${R2_AS_id}    ${Process_id}    
    Run Keyword and Continue On Failure    redistribution    R3    ${R3_AS_id}    ${Process_id}

Check if ip address is set and interface is up 
    Log To Console    Checking if ip address is set and interface is up  
    :FOR    ${ELEMENT}    IN    @{Devices}
    \    ${result}=    Run Keyword and Continue On Failure    checking_operabilty    ${ELEMENT}    show ip interface brief
    \    Log    Interfaces up in ${ELEMENT}
    \    Run Keyword If    ${result}==False    FAIL    ip address not set or interface not up in  ${ELEMENT} 


Ensure that different autonomous systems can communicate with each other

    Log    Autonomous system communication validated
       
Check if OSPF neighbors are established
    Log To Console    Checking if OSPF neighbors are established 
    :FOR    ${ELEMENT}    IN    @{Devices}
    \    ${result}=    Run Keyword and Continue On Failure    checking_operabilty    ${ELEMENT}    show ip ospf neighbor
    \    Log     OSPF neighbors learnt in ${ELEMENT}
    \    Run Keyword If    ${result}==False    FAIL    neighbor not established ${ELEMENT} 

Check if all routes are learnt by devices 
    Log To Console    Checking if all routes are learnt by devices   
    :FOR    ${ELEMENT}    IN    @{Devices}
    \    ${result}=    Run Keyword and Continue On Failure    checking_operabilty    ${ELEMENT}    show ip bgp
    \    Log    Routes learnt by ${Element}
    \    Run Keyword If    ${result}==False    FAIL    routes not learnt ${ELEMENT}  	 


Track the scale on eBGP peers
    Log To Console    Tracking the scale on eBGP peers

Track the scale on iBGP peers
    Log To Console    Tracking the scale on iBGP peers

Verify the number of routes the DUT is able to receive
    Log To Console    Verifying the number of routes the DUT is able to receive 

Verify the number of routes the DUT is able to announce to a single iBGP neighbor
    Log To Console    Verifying the number of routes the DUT is able to announce

Evaluate peering convergence speed
    Log To Console    Evaluating peering convergence speed



    

