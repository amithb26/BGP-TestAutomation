*** Settings ***

Metadata 	Version           1.0
...	        More Info         For more information about Robot Framework see http://robotframework.org
...             Author            Payal Jain 
...             Date              19 Dec 2016  
...	        Executed At  	  ${HOST}
...		Test Framework    Robot Framework Python

Documentation   A test suite with tests for configuring BGP.

...             Topology:-
...                          ____________________________
...                         |             R1         AS2 |
...                         |            /  \            |
...                         |           /    \           |
...                         |         R2      R3         |
...                         |_________|________|_________|
...                                   |        |
...                             ______|__   ___|______
...                            |      AS1| |       AS3|
...                            |    R4   | |   R5     |
...                            |_________| |__________|

...               Testplan Goals:-
...               1. Configure IP addresses as per the topology.
...               2. Each Router should have a loopback0 interface.
...               3. Configure OSPF within AS2 to advertise the loopback0 interfaces.
...                  Don't advertise or run OSPF on the links interconnecting AS1 and AS3.
...               4. Configure IBGP between R2 and R3. Source the BGP updates from the loopback0 interfaces.
...               5. Enable BGP synchronisation.
...               6. Configure EBGP between R2 and R4.
...               7. Configure EBGP between R3 and R5.
...               8. Advertise the loopback0 interfaces on R4 and R5.
...               9. Ensure AS1 and AS3 can communicate with each other without removing the BGP synchronisation command.

Resource          Resource.robot

Suite Setup       Setup Actions

Suite Teardown    Teardown Actions

*** Test Cases ***

Initiation_Phase
    
    Configure IP addresses as per the topology
	    Configure ip address 
	    Set loopback interface
  
    Configure OSPF within AS2 to advertise the connected networks
	    Enable OSPF in devices present in AS2 and set the ospf neighbors

    Configure IBGP and source the BGP updates from the loopback0 interfaces
	    Enable IBGP and advertise the updates from the loopback interface

    Enable BGP Synchronisation
	    Enable synchronisation between border routers


    Configure EBGP and source the BGP updates from the loopback0 interfaces
	    Enable BGP and advertise networks connected outside the autonomous system

            Advertise loopback interface on AS1 and AS3

            Establish route between R2 and R3

            Redistribute routes from OSPF into BGP
   
Validation_Phase

    Check if ip address is set and interface is up 

    Ensure that different autonomous systems can communicate with each other

    Check if OSPF neighbors are established
			
    Check if all routes are learnt by devices  


Sustenance_Phase	 	

     Track the scale on eBGP peers

     Track the scale on iBGP peers

     Verify the number of routes the DUT is able to receive 

     Verify the number of routes the DUT is able to announce to a single iBGP neighbor

     Evaluate peering convergence speed
 
     

     

