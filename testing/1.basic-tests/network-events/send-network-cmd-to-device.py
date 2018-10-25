# This example will send a couple of commands to our device, as we would if we
# were using our Phone, or our regular Infrastructure during a product's actual
# usage
#
# The goal of this example is to show you how you can send a network command to
# your devices through the AWS device communication infrastructure.
#
# In our particular example, we are only sending a command and not asserting
# anything. Of course this would never be a real world example, it's only for
# educational purposes


import time
import Device
from Spanner import Spanner

IFTTT_KEY = "hgql1kyuQEL-KJfSbP7v0v63TOphPTSLoE5nhxrfFa-"
device = Device.Ifttt(IFTTT_KEY)

def send_network_cmds():
    # send network command to our device
    device.sendCommand("turn_on")

    time.sleep(2)

    device.sendCommand("turn_off")

if __name__ == "__main__":
	send_network_cmds()
