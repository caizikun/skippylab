"""
Wrapper around the PrologixGPIBEthernet adapter, to transparently
manage instruments which are connected via GPIB and the respective controller

"""

from plx_gpib_ethernet import PrologixGPIBEthernet

def prologix_gpib_ethernet_provider(ip, gpib_addres):
    """
    Provide a vxi11 compatible instrument which is accesible 
    transparently through its ip.    

    Args:
        ip (str): ip address of the controller
        gpib_address (str): gpib adress of the instrument

    Returns: 
        vxi11.instrument
    """
    instrument = PrologixGPIBEthernet(ip)
    gpib.connect()
    gpib.select(gpib_address)

    return gpib

