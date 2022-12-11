from dronekit import connect

if __name__ == "__main__":
    vehicle = connect("/dev/ttyS0", wait_ready=True, baud=57600)
