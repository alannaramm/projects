from pysnmp.hlapi import *

def get_snmp_data(target, oid, community="public"):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=0),
        UdpTransportTarget((target, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )
    
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        return f"Error: {errorIndication}"
    elif errorStatus:
        return f"SNMP Error: {errorStatus.prettyPrint()}"
    else:
        return f"{varBinds[0][1]}"

device_ip = "192.168.1.1"  # Replace with real IP
cpu_oid = "1.3.6.1.4.1.2021.11.9.0"  # Example OID for CPU load

print(f"CPU Load: {get_snmp_data(device_ip, cpu_oid)}%")
