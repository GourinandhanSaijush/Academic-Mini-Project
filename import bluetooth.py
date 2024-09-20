import bluetooth
import uuid

# Generate or Hardcode your UUID
service_uuid = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # Replace with your UUID

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1)

client_socket, address = server_socket.accept()

# Continue with your Bluetooth communication code
