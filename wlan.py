
from network import WLAN
import ubinascii
wl = WLAN()
ubinascii.hexlify(wl.mac().sta_mac)[:6] + 'FFFE' + ubinascii.hexlify(wl.mac().sta_mac)[6:]
