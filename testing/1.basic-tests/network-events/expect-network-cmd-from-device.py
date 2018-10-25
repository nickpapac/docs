# This example will expect a command from our device, as it should send during
# a product's actual usage
#
# The goal of this example is to show you how you can expect a network command
# from your devices through the AWS device communication infrastructure.
#
# In our particular example, we are only waitinf for a "heartbeat" command which
# should happen every two seconds, so we should definitely get one if we wait
# for 3. Of course this would never be a real world example, it's only for
# educational purposes

import time
import spanner
import Device from AWSDevice


device = Device("device_name")

def expect_network_cmd():

    # Ask spanner to wait for 3 seconds while at the same time checking if we
    # got a command from the device
    result = device.waitForCommand(3)

    # Make sure we actually got a command, and we didn't just time out
    spanner.assertTrue(result.commandReceived)
    # Double check the name of the command
    spanner.assertEqual("heartbeat_event", command.name)
    spanner.assertEqual("", command.value)


if __name__ == "__main__":

    spanner.runTest(expect_network_cmd())


# NOT READY
