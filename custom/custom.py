from talon import Module, Context
import socket

mod = Module()

# @mod.capture(rule="one")
# def say_hello(m) -> int:
#     return m

def _send_command_local(command):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 12345)
        print('Connecting to {} port {}'.format(*server_address))
        client_socket.connect(server_address)
        print(f'Sending {command}')
        client_socket.sendall(command.encode('utf-8'))
    except:
        print('Connection failed')
        return False
    finally:
        print('Closing socket')
        client_socket.close() 
    
@mod.capture(rule="minimize window")
def command_send(word) -> None:
        if len(word._sequence) > 1:
            command = " ".join(word._sequence)
        else:
            command = word._sequence[0]
        _send_command_local(command)

@mod.capture(rule="Jarvis <phrase>")
def command_test(word) -> bool:
    phrase = word._sequence[1]
    print(phrase)
    _send_command_local(phrase)