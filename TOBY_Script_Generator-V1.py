import os, re
from flask import Flask, render_template, request, url_for, redirect, json, send_file
from werkzeug.datastructures import CombinedMultiDict, MultiDict

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def form1():
    if request.method == "POST":
        create_toby_file(request.values)
        #return render_template('download_toby_file.html')
        return render_template('download_toby_file2.html')
    else:
        return render_template('toby_script_generator-v1.html')

@app.route('/return_file')
def return_file():
    return send_file('toby_file_1.robot')
        
@app.route('/results',methods=['GET', 'POST'])
def form1results():
    if request.method == "POST":
        return render_template('form1result.html')
    else:
        return render_template('form1result.html')

def create_toby_file(data_from_form):
    print ("inside create_toby_file")
    form_dict = data_from_form.to_dict()
    print(form_dict)

    patterns = [',']
    dut_handle = form_dict.get('dut_handle', 'dh_none')
    #    
    kw0 = form_dict.get('kw0')
    if (kw0):
        if re.search(',', kw0):
            kw0 = kw0.split(',')
            kw0 = [x.strip() for x in kw0]
        else:
            kw0 = kw0.strip()    

    #        
    kw1 = form_dict.get('kw1')
    if (kw1):
        if re.search(',', kw1):
            kw1 = kw1.split(',')
            kw1 = [x.strip() for x in kw1]
        else:
            kw1 = kw1.strip()    

    #        

    fr = open("C:\\Users\\pgudipati\\Me-Pras-Cloud\\Technical-Docs\\Python-UCSC\\Project\\toby_file_1.robot", 'w')
 
    fr.write('''#====================\n''')
    fr.write('''*** Settings ***\n''')
    fr.write('''#====================\n''')
    fr.write('''Documentation\n''')
    fr.write('''    ...             Author                 : \n''')
    fr.write('''    ...             JTMS DESCRIPTION       : \n''')
    fr.write('''    ...             RLI                    : \n''')
    fr.write('''    ...             DESCRIPTION            : \n''')
    fr.write('''    ...             TECHNOLOGY AREA        : \n''')
    fr.write('''    ...             MIN SUPPORT VERSION    : \n''')
    fr.write('''    ...             FEATURE                : \n''')
    fr.write('''    ...             SUB-AREA               : \n''')
    fr.write('''    ...             MPC/FPC TYPE           : \n''')
    fr.write('''    ...             CUSTOMER PR            : \n''')
    fr.write('''    ...             PLATFORM               : \n''')
    fr.write('''    ...             VIRTUALIZATION SUPPORT : \n''')
    fr.write('''    ...             DOMAIN                 : \n''')
    fr.write('''    ...             TESTER                 : \n''')
    fr.write('''    ...             JPG                    : \n''')
    fr.write('''    ...             MARKET USE CASES       : \n''')
    fr.write('''    ...             Supporting files to run script - \n''')
    fr.write('''\n''')

    fr.write('''Library     BuiltIn\n''')
    fr.write('''Library     Collections\n''')
    fr.write('''Library     String\n''')
    fr.write('''Library     jnpr/toby/system/jvision/jvision.py\n''')
    fr.write('''Library     jnpr/toby/init/init.py\n''')

    fr.write('''Resource    jnpr/toby/Master.robot\n''')
    fr.write('''Resource    jnpr/toby/toby.robot\n''')
    fr.write('''Resource    jnpr/toby/engines/verification/verification.robot\n''')
    fr.write('''Resource    jnpr/toby/engines/verification/verification_jvision.robot\n''')

    #
    resource_files = form_dict.get('resource_files')
    if resource_files:
        if re.search(',', resource_files):
            resource_files = resource_files.split(',')
            resource_files = [x.strip() for x in resource_files]
        else:
            resource_files = resource_files.strip()
    #
    if isinstance(resource_files, list):
        for i in resource_files:
            fr.write('''Resource    '''+i+'''\n''')
    else:
        fr.write('''Resource    '''+resource_files+'''\n''')

    fr.write('''\n''')
    fr.write('''Suite Setup     Run Keywords\n''')
    fr.write('''    ...         Toby Suite Setup\n''')
    fr.write('''\n''')
    fr.write('''Suite Teardown  Run Keywords\n''')
    fr.write('''    ...         Toby Suite Teardown\n''')
    fr.write('''\n''')
    fr.write('''Test Setup      Run Keywords\n''')
    fr.write('''    ...         Toby Test Setup\n''')
    fr.write('''\n''')
    fr.write('''Test Teardown   Run Keywords\n''')
    fr.write('''    ...         Toby Test Teardown\n''')

    fr.write(''' \n''')
    fr.write('''#========================================\n''')
    fr.write('''*** Test Cases ***\n''')
    fr.write('''#========================================\n''')
    fr.write(''' \n''')
    
# TCs for Protocols Flapping:
    # OSPF
    proto_flap_count = form_dict.get('prot_flap_count')
    ospf_flag = form_dict.get('ospf', 'No')
    if (ospf_flag == "yes"):            
        fr.write('''##########\n''')
        fr.write('''Tc Flap OSPF\n''')
        fr.write('''########## \n''')
        fr.write('''    [Documentation]  Deacitave then activate protocols ospf \{\} multiple times \n''')
        fr.write('''    [Setup]   NONE  \n''')
        fr.write('''    [Tags]   Negative  \n\n''')
        fr.write('''    Log   **************************************************Starting ${TEST NAME}**************************************************\n\n''')
        fr.write('''        :FOR     ${var}    in range    1     ''' + str(proto_flap_count) + '''\n''')
        fr.write('''        \\   Config Engine    device_list=r0    cmd_list=deactivate protocols ospf       commit=1\n''')
        fr.write('''        \\   Sleep    2s\n''')
        fr.write('''        \\   Config Engine    device_list=r0    cmd_list=activate protocols ospf       commit=1\n''')
        fr.write('''        \\   Sleep    2s\n''')
        fr.write('''        Run Keyword And Continue On Failure       ''' + kw1 + '''\n\n''')
        fr.write('''    Log   **************************************************END of  ${TEST NAME}**************************************************\n\n''')

    # isis
    isis_flag = form_dict.get('isis', 'No')
    if (isis_flag == "yes"):            
        fr.write('''##########\n''')
        fr.write('''Tc Flap isis\n''')
        fr.write('''########## \n''')
        fr.write('''    [Documentation]  Deacitave then activate protocols ISIS \{\} multiple times \n''')
        fr.write('''    [Setup]   NONE  \n''')
        fr.write('''    [Tags]   Negative  \n\n''')
        fr.write('''    Log   **************************************************Starting ${TEST NAME}**************************************************\n\n''')
        fr.write('''        :FOR     ${var}    in range    1     ''' + str(proto_flap_count) + '''\n''')
        fr.write('''        \\   Config Engine    device_list=r0    cmd_list=deactivate protocols isis       commit=1\n''')
        fr.write('''        \\   Sleep    2s\n''')
        fr.write('''        \\   Config Engine    device_list=r0    cmd_list=activate protocols isis       commit=1\n''')
        fr.write('''        \\   Sleep    2s\n''')
        fr.write('''        Run Keyword And Continue On Failure       ''' + kw1 + '''\n\n''')
        fr.write('''    Log   **************************************************END of  ${TEST NAME}**************************************************\n\n''')

    # bgp
    bgp_flag = form_dict.get('bgp', 'No')
    if (bgp_flag == "yes"):            
        fr.write('''##########\n''')
        fr.write('''Tc Flap bgp\n''')
        fr.write('''########## \n''')
        fr.write('''    [Documentation]  Deacitave then activate protocols bgp \{\} multiple times \n''')
        fr.write('''    [Setup]   NONE  \n''')
        fr.write('''    [Tags]   Negative  \n\n''')
        fr.write('''    Log   **************************************************Starting ${TEST NAME}**************************************************\n\n''')
        fr.write('''        :FOR     ${var}    in range    1     ''' + str(proto_flap_count) + '''\n''')
        fr.write('''        \\   Config Engine    device_list=r0    cmd_list=deactivate protocols bgp       commit=1\n''')
        fr.write('''        \\   Sleep    2s\n''')
        fr.write('''        \\   Config Engine    device_list=r0    cmd_list=activate protocols bgp       commit=1\n''')
        fr.write('''        \\   Sleep    2s\n''')
        fr.write('''        Run Keyword And Continue On Failure       ''' + kw1 + '''\n\n''')
        fr.write('''    Log   **************************************************END of  ${TEST NAME}**************************************************\n\n''')

    # mpls
    mpls_flag = form_dict.get('mpls', 'No')
    if (mpls_flag == "yes"):            
        fr.write('''##########\n''')
        fr.write('''Tc Flap mpls\n''')
        fr.write('''########## \n''')
        fr.write('''    [Documentation]  Deacitave then activate protocols mpls \{\} multiple times \n''')
        fr.write('''    [Setup]   NONE  \n''')
        fr.write('''    [Tags]   Negative  \n\n''')
        fr.write('''    Log   **************************************************Starting ${TEST NAME}**************************************************\n\n''')
        fr.write('''        :FOR     ${var}    in range    1     ''' + str(proto_flap_count) + '''\n''')
        fr.write('''        \\   Config Engine    device_list=r0    cmd_list=deactivate protocols mpls       commit=1\n''')
        fr.write('''        \\   Sleep    2s\n''')
        fr.write('''        \\   Config Engine    device_list=r0    cmd_list=activate protocols mpls       commit=1\n''')
        fr.write('''        \\   Sleep    2s\n''')
        fr.write('''        Run Keyword And Continue On Failure       ''' + kw1 + '''\n\n''')
        fr.write('''    Log   **************************************************END of  ${TEST NAME}**************************************************\n\n''')

# TCs for Deamons Restart:
    # RPD restart
    rpd_flag = form_dict.get('rpd', 'No')
    if (rpd_flag == "yes"):            
        fr.write('''##########\n''')
        fr.write('''Tc RPD restart\n''')
        fr.write('''########## \n''')
        fr.write('''    [Documentation]  RPD Restart\n''')
        fr.write('''    [Setup]   NONE  \n''')
        fr.write('''    [Tags]   Negative  \n\n''')
        fr.write('''    Log   **************************************************Starting ${TEST NAME}**************************************************\n\n''')
        fr.write('''        ${test} =  Execute Cli Command On Device   device=''' + dut_handle + '''   command=restart routing\n''')
        fr.write('''        Run Keyword And Continue On Failure       ''' + kw1 + '''\n\n''')
        fr.write('''    Log   **************************************************END of  ${TEST NAME}**************************************************\n\n''')

    #chassisd  
    chassisd_flag = form_dict.get('chassisd', 'No')
    if (chassisd_flag == "yes"):            
        fr.write('''##########\n''')
        fr.write('''Tc chassisd restart\n''')
        fr.write('''########## \n''')
        fr.write('''    [Documentation]  chassisd Restart\n''')
        fr.write('''    [Setup]   NONE  \n''')
        fr.write('''    [Tags]   Negative  \n\n''')
        fr.write('''    Log   **************************************************Starting ${TEST NAME}**************************************************\n\n''')
        fr.write('''        ${test} =  Execute Cli Command On Device   device=''' + dut_handle + '''   command=restart chassisd\n''')
        fr.write('''        Run Keyword And Continue On Failure       ''' + kw1 + '''\n\n''')
        fr.write('''    Log   **************************************************END of  ${TEST NAME}**************************************************\n\n''')
         
# TCs for Links Flap:

    # End of File Writing =======================================
    fr.close()
    return True

if __name__ == "__main__":
    #host = os.getenv('IP', '127.0.0.1')
    #port = int(os.getenv('PORT', 5000))
    #print (host, port)
    app.run()