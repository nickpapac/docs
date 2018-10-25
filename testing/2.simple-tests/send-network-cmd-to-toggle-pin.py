# This example will send a couple of commands to our device, which will respond
# accordingly, to showcase a product's actual usage.
#
# In this particular example the device we are testing is a Smart Switch, which
# responds by toggling one of its pins On of Off based on the command.

# The goal of this example is to show you how you can send a network commands to
# your devices through the AWS device communication infrastructure, and read a
# device's output's to verify its response, using our Testboard.
#
# This is one real world example of a very simple functional test you would run
# for your devices.

import time
from Spanner import Spanner
from Testboard import Testboard
import Device

IFTTT_KEY = "hgql1kyuQEL-KJfSbP7v0v63TOphPTSLoE5nhxrfFa-"
device = Device.Ifttt(IFTTT_KEY)

testboard = Testboard("testboard_name")

# Our device's Output Pin will be connected to the Testboard's D7, making it our
# Input Pin
INPUT_PIN = "D7"

def test_switch_on_network_cmd():
    # send network command to our device
    device.sendCommand("turn_on")
    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(INPUT_PIN)
    spanner.assertTrue(value)

def test_switch_off_network_cmd():
    # send network command to our device
    device.sendCommand("turn_off")
    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(INPUT_PIN)
    spanner.assertFalse(value)


if __name__ == "__main__":

    test_switch_on_network_cmd()

    time.sleep(2)

    test_switch_off_network_cmd()
