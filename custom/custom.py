from talon import Module
import socket, json

mod = Module()
        
def _send_command_remote(command):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('192.168.1.11', 8000)
        print('Connecting to {} port {}'.format(*server_address))
        client_socket.connect(server_address)
        data = {"type": "phrase", "message": command}
        data_string = json.dumps(data)
        client_socket.sendall(data_string.encode())
    except:
        print('Connection failed')
        return False
    finally:
        print('Closing socket')
        client_socket.close() 
        
def _send_command_message_remote(command):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('192.168.1.11', 8000)
        print('Connecting to {} port {}'.format(*server_address))
        client_socket.connect(server_address)
        data = {"type": "command", "message": command}
        data_string = json.dumps(data)
        client_socket.sendall(data_string.encode())
    except:
        print('Connection failed')
        return False
    finally:
        print('Closing socket')
        client_socket.close() 
    
    

        
@mod.capture(rule="Jarvis <phrase>")
def command_send(word) -> bool:
    phrase = word._sequence[1]
    # print(phrase.words[0])
    if phrase.words[0] == 'stop':
        _send_command_message_remote('stop')
    elif phrase.words[0] == 'clear':
        _send_command_message_remote('clear')
    else:
        send_phrase = ' '.join(phrase.words)
        _send_command_remote(send_phrase)
    
# @mod.capture(rule="Jarvis stop")
# def command_send(word) -> bool:
#     # phrase = word._sequence[1]
#     # send_phrase = ' '.join(phrase.words)
#     _send_command_message_remote('stop')
    
# @mod.capture(rule="minimize window")
# def command_send(word) -> None:
#         if len(word._sequence) > 1:
#             command = " ".join(word._sequence)
#         else:
#             command = word._sequence[0]
#         _send_command_local(command)
