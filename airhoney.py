import os
import socket
import subprocess

print("	   _   _                            	   ")
print("	  /_\ (_)_ __ /\  /\___  _ __   ___ _   _  ")
print("	 //_ \| | '__/ /_/ / _ \| '_ \ / _ \ | | | ")
print("	/  _  \ | | / __  / (_) | | | |  __/ |_| | ")
print("	\_/ \_/_|_| \/ /_/ \___/|_| |_|\___|\__, | ")
print("	                                     |___/ ")
print("	                                    	   ")
print("	    Wireless Audition Toolkit Installer    ")
print("	             By: Dormidera                 ")                    
print("	                                    	   ")	
print("	                                    	   ")
print("Selecciona una opcion:                  	   ")
print("	                                    	   ")
print("1: Add repositorios de Kali Linux")
print("2: Instalar MacChanger")
print("3: Instalar herramientas auditorias Wi-Fi")
print("4: Descargar diccionarios")
print("5: Instalar todo")
print("6: Salir")
print("	                                    	   ")
opcion = int(input("Opcion seleccionada: "))

if opcion == 1:

	os.system("echo '# Kali linux repositorios \ndeb http://http.kali.org/kali sana main non-free contrib\ndeb http://security.kali.org/kali-security sana/updates main contrib non-free\ndeb http://repo.kali.org/kali kali-bleeding-edge main' >>sudo /etc/apt/sources.list")
	os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
	os.system("sudo apt-get update -m")
	os.system("python airhoney.py")
	
elif opcion == 2:
	print("MacChanger")
	os.system("sudo apt-get install macchanger macchanger-gtk")
	os.system("python airhoney.py")
	
elif opcion == 3:
	print("Wifite\nAircrack-ng\nLinset\nBully\nReaver\nPixieWPS\nCowpatty\nPyrit\nFern_Wifi_Cracker")
	os.system("sudo apt-get  install libpcap-dev libssl-dev wifite aircrack-ng bully reaver pixiewps cowpatty pyrit")
	os.system("sudo git clone https://github.com/vk496/linset.git")
	os.system("sudo git clone https://github.com/savio-code/fern-wifi-cracker.git")
	os.system("python airhoney.py")

elif opcion == 4:
	print("Diccionarios")
	os.system("sudo git clone https://github.com/Dormidera/Passwords.git")	
	os.system("python airhoney.py")
	
elif opcion == 5:
	print("Instalar todo")
	os.system("echo '# Kali linux repositorios \ndeb http://http.kali.org/kali sana main non-free contrib\ndeb http://security.kali.org/kali-security sana/updates main contrib non-free\ndeb http://repo.kali.org/kali kali-bleeding-edge main' >>sudo /etc/apt/sources.list")
	os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
	os.system("sudo apt-get update -m")
	os.system("sudo apt-get install macchanger macchanger-gtk")
	os.system("sudo apt-get  install libpcap-dev libssl-dev wifite aircrack-ng bully reaver pixiewps cowpatty pyrit")
	os.system("sudo git clone https://github.com/vk496/linset.git")
	os.system("sudo git clone https://github.com/savio-code/fern-wifi-cracker.git")
	os.system("sudo git clone https://github.com/Dormidera/Passwords.git")	
	os.system("exit")
	
elif opcion == 6:
	os.system("clear")
	os.system("exit")
