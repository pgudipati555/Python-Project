#====================
*** Settings ***
#====================
Documentation
    ...             Author                 : 
    ...             JTMS DESCRIPTION       : 
    ...             RLI                    : 
    ...             DESCRIPTION            : 
    ...             TECHNOLOGY AREA        : 
    ...             MIN SUPPORT VERSION    : 
    ...             FEATURE                : 
    ...             SUB-AREA               : 
    ...             MPC/FPC TYPE           : 
    ...             CUSTOMER PR            : 
    ...             PLATFORM               : 
    ...             VIRTUALIZATION SUPPORT : 
    ...             DOMAIN                 : 
    ...             TESTER                 : 
    ...             JPG                    : 
    ...             MARKET USE CASES       : 
    ...             Supporting files to run script - 

Library     BuiltIn
Library     Collections
Library     String
Library     jnpr/toby/system/jvision/jvision.py
Library     jnpr/toby/init/init.py
Resource    jnpr/toby/Master.robot
Resource    jnpr/toby/toby.robot
Resource    jnpr/toby/engines/verification/verification.robot
Resource    jnpr/toby/engines/verification/verification_jvision.robot
Resource    38094_keywords1.robot
Resource    38094_keywords2.robot

Suite Setup     Run Keywords
    ...         Toby Suite Setup

Suite Teardown  Run Keywords
    ...         Toby Suite Teardown

Test Setup      Run Keywords
    ...         Toby Test Setup

Test Teardown   Run Keywords
    ...         Toby Test Teardown
 
#========================================
*** Test Cases ***
#========================================
 
##########
Tc Flap OSPF
########## 
    [Documentation]  Deacitave then activate protocols ospf \{\} multiple times 
    [Setup]   NONE  
    [Tags]   Negative  

    Log   **************************************************Starting ${TEST NAME}**************************************************

        :FOR     ${var}    in range    1     3
        \   Config Engine    device_list=r0    cmd_list=deactivate protocols ospf       commit=1
        \   Sleep    2s
        \   Config Engine    device_list=r0    cmd_list=activate protocols ospf       commit=1
        \   Sleep    2s
        Run Keyword And Continue On Failure       check_core_functions_1

    Log   **************************************************END of  ${TEST NAME}**************************************************

##########
Tc Flap isis
########## 
    [Documentation]  Deacitave then activate protocols ISIS \{\} multiple times 
    [Setup]   NONE  
    [Tags]   Negative  

    Log   **************************************************Starting ${TEST NAME}**************************************************

        :FOR     ${var}    in range    1     3
        \   Config Engine    device_list=r0    cmd_list=deactivate protocols isis       commit=1
        \   Sleep    2s
        \   Config Engine    device_list=r0    cmd_list=activate protocols isis       commit=1
        \   Sleep    2s
        Run Keyword And Continue On Failure       check_core_functions_1

    Log   **************************************************END of  ${TEST NAME}**************************************************

##########
Tc Flap bgp
########## 
    [Documentation]  Deacitave then activate protocols bgp \{\} multiple times 
    [Setup]   NONE  
    [Tags]   Negative  

    Log   **************************************************Starting ${TEST NAME}**************************************************

        :FOR     ${var}    in range    1     3
        \   Config Engine    device_list=r0    cmd_list=deactivate protocols bgp       commit=1
        \   Sleep    2s
        \   Config Engine    device_list=r0    cmd_list=activate protocols bgp       commit=1
        \   Sleep    2s
        Run Keyword And Continue On Failure       check_core_functions_1

    Log   **************************************************END of  ${TEST NAME}**************************************************

##########
Tc RPD restart
########## 
    [Documentation]  RPD Restart
    [Setup]   NONE  
    [Tags]   Negative  

    Log   **************************************************Starting ${TEST NAME}**************************************************

        ${test} =  Execute Cli Command On Device   device={dh_r0}   command=restart routing
        Run Keyword And Continue On Failure       check_core_functions_1

    Log   **************************************************END of  ${TEST NAME}**************************************************

##########
Tc chassisd restart
########## 
    [Documentation]  chassisd Restart
    [Setup]   NONE  
    [Tags]   Negative  

    Log   **************************************************Starting ${TEST NAME}**************************************************

        ${test} =  Execute Cli Command On Device   device={dh_r0}   command=restart chassisd
        Run Keyword And Continue On Failure       check_core_functions_1

    Log   **************************************************END of  ${TEST NAME}**************************************************

