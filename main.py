import socket

if __name__ == '__main__':
    def getPorts(portsList):
        totalPorts = len(portsList)
        portsStr = ''

        consec = 0

        for i in range(totalPorts):
            if i + 1 < totalPorts and portsList[i] + 1 == portsList[i+1]:
                consec += 1
            else:
                if consec > 0:
                    portsStr += str(portsList[i] - consec) + '-' + str(portsList[i])
                    consec = 0
                else:
                    portsStr += str(portsList[i])
                portsStr += '\n'

        return portsStr

    # return the ports list in string format, delimited by newlines.
    # if there are any consecutive patterns, print ranges instead
    outputFile = open('available_ports.txt', 'a')

    # truncate everything in the file before operating on it
    outputFile.seek(0)
    outputFile.truncate()

    totalPorts = None
    usablePorts = []
    unusablePorts = []

    beginPort = int(input('Enter the beginning port: '))
    endPort = int(input('Enter the ending port: '))

    totalPorts = endPort - beginPort + 1

    for port in range(beginPort, endPort + 1):
        try:
            # try to bind to the port. If no exception is thrown, it is open
            s = socket.socket()
            s.bind(('localhost', port))

            usablePorts.append(port)
        except OSError as osError:
            unusablePorts.append(port)

    usablePortsStr = getPorts(usablePorts)
    unusablePortsStr = getPorts(unusablePorts)

    # write all of the information to the file
    outputFile.write('Total ports tested: ' + str(totalPorts) + '\n')
    outputFile.write('Total available ports: ' + str(len(usablePorts)) + '\n')
    outputFile.write('Total unavailable ports: ' + str(len(unusablePorts)) + '\n\n')
    outputFile.write('Usable ports: \n' + str(usablePortsStr) + '\n')
    outputFile.write('Unusable ports: \n' + str(unusablePortsStr) + '\n')

    outputFile.close()