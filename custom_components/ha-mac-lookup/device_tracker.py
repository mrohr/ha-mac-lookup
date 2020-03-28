import logging
import arpreq
import socket


from homeassistant.components.device_tracker import (
    DOMAIN,
    PLATFORM_SCHEMA,
    DeviceScanner,
)

_LOGGER = logging.getLogger(__name__)

def get_scanner(hass, config):
    return ArpreqDeviceScanner(config[DOMAIN])

class ArpreqDeviceScanner(DeviceScanner):

    def __init__(self, config):
        """Initialize the scanner."""
        _LOGGER.debug("Initializing")
        try:
            self.hostname = socket.gethostname()
            self.ip = socket.gethostbyname(self.hostname)
            self.subnet = ".".join(self.ip.split(".")[:-1]
        except Exception as e:
            _LOGGER.error(e)

    def scan_devices(self):
        connected_devices = []
        _LOGGER.debug("Scanning")
        try:
            for i in range(256):
                test_ip = "{}.{}".format(self.subnet, i)
                mac = arpreq.arpreq(test_ip)
                if mac is not None:
                  connected_devices.append(mac)
        except Exception ase e:
            _LOGGER.error("Unable to scan devices")
            _LOGGER.error(e)
        _LOGGER.debug("Scanning complete!")
        return connected_devices

    def get_device_name(self, device):
        return None
