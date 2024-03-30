from talon import Module, Context
import socket

mod = Module()

# @mod.capture(rule="one")
# def say_hello(m) -> int:
#     return m

@mod.capture(rule="one|two|minimize window")
def command_send(word) -> bool:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 12345)
        print('Connecting to {} port {}'.format(*server_address))
        client_socket.connect(server_address)
    except:
        print('Connection failed')
        return False
    try:
        if len(word._sequence) > 1:
            command = " ".join(word._sequence)
        else:
            command = word._sequence[0]
        print(f'Sending {command}')
        client_socket.sendall(command.encode('utf-8'))
    finally:
        print('Closing socket')
        client_socket.close() 
    return True