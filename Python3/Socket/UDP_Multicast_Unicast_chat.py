import socket
import struct
import os
import time
import json

host = '224.0.0.127' # Adresse Multicast
port = 7186 # Communication Port
my_host = '192.168.1.15' # Adresse fixe de la machine

name = input("Choisir votre nom >> ") # Selection du pseudo

socket_io = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_io.bind(('', port)) # Bind toute les adresses possibles du port

TSAP = (host, port)
mreq = struct.pack("4sl", socket.inet_aton(host), socket.INADDR_ANY)

socket_io.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
socket_io.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1) # Option pour envoyer un message en unicast

pid = os.fork() # Fork pour lecture ecriture
if pid: # Condition de lecture
    while True: # Boucle infinie
        (data, (ip, port)) = socket_io.recvfrom(1000) # Variable reception de message + ip et port
        if ip == my_host: # Si c'est mon IP je n'affiche pas
            continue
        out = data.decode('utf-8') # Decode Byte python3
        out = out.replace('\n', '')
        sender = out.split(':')[0] # Variable du pseudo de l'envoyeur
        message = out.split(':')[1] # Varialbe du message
        with open('users.json') as json_file: # Import du fichier JSON
            list_users = json.load(json_file)
        try:
            exist = list_users[sender] # Verification si le pseudo existe
        except Exception:
            exist = None
        if exist is None:
            list_users[sender] = ip # Si il n'existe on ajoute l'ip au jSON
        with open('users.json', 'w') as json_file:
            json.dump(list_users, json_file, indent=4) # Sauvegarde du JSON
        print("{}: {}\n::".format(sender, message), end=" ") # affichage du message formaté
else:
    while True: # Boucle infinie
        unicast = False
        time.sleep(0.1) # Sleep pour un affichage correct des ::
        clavier = input(':: ') # On demande le message à l'utilisateur
        if not clavier:
            break
        if clavier.startswith('>all'):
	    	with open('users.json') as json_file:
	        	users = json.load(json_file)
	        	listed_users = []
		        for user in users:
		            listed_users.append(user)
	        print(", ".join(listed_users))
	        continue
        elif clavier.startswith('@'): # Si il commence par @
            target = clavier.split(' ')[0].replace('@', '') # On dégage le pseudo de l'utilisateur qu'on vise
            clavier = clavier.split(' ')
            clavier.pop(0)
            clavier = " ".join(clavier) # On reforme le message sans le pseudo
            unicast = True
        else:
            target = "*" # Si il n'y a pas de target alors le message est pour tout le monde
        msg = "{}:{}:{}".format(name, target, clavier) # On prepare le message qu'on envoie
        if unicast: # Si on target une personne
            with open('users.json') as json_file:
                users = json.load(json_file)
            socket_io.sendto(msg.encode('utf-8'), (users[target], port)) # On envoie le message sur son IP
        else:
            socket_io.sendto(msg.encode('utf-8'), TSAP) # Sinon on envoie à tout le monde
socket_io.close()
