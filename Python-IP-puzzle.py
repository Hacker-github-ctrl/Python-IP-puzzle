#!/usr/bine/env python3
import time
import os
import requests
import json

def consulta():
  os.system("apt install python3")
  os.system("clear")

print("\nEsse SCRIPT É ESCRITO PELA LINGUAGEM DE PROGRAMAÇÃO 'PYTHON' ELE É DESENVOLVIDO PELO PROGRAMADOR DA LINGUAGEM DE PROGRAMAÇÃO")
print()
print("Esse SCRIPT é feito para consultar o IP de uma pessoa ou HACKEAR, MEUS SCRIPTS DE PROGRAMAÇÃO É FEITO PARA PRÁTICAR ETHICAL HACKING.")
print()

print("IP SCRIPT EM PYTHON")
print("\n")

ip = input("Digite o Endereço de IP: ")
if len(ip) != "":
  print("\n" + "Acesso Garantido !")
else:
  print("\nNão foi possivel HACKEAR O Endereço de IP!")
  exit()

r = requests.get(f"https://ipinfo.io/{ip}/json")

for ip in r.json():
  os.system("clear")
  print("\n")
  print("\nIP HACKEADO!")
  print("\n")
  print("\n_________________________________")
  print("\n|IP: ", r.json()["ip"])           
  print("\n|Cidade: ", r.json()["city"])     
  print("\n|Região: ", r.json()["region"])   
  print("\n|País: ", r.json()["country"])    
  print("\n|Localização: ", r.json()["loc"]) 
  print("\n|Organização: ", r.json()["org"]) 
  print("\n|_________________________________")
print("\n")
print("\nObrigado pelo o uso do meu SCRIPT ;)")

print("\n")
print("\nSim/Não")
print("\n")
pergunta = pergunta2 = input("Digite se vc deseja limpar a Tela?: ")
if pergunta == "sim" or pergunta == "s" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "S":
  print("\nSim")
  print(pergunta)
  os.system("clear")
elif pergunta2 == "não" or pergunta2 == "n" or pergunta2 == "N" or pergunta2 == "Não" or pergunta2 == "NÂO":
  print(pergunta2)
  exit()
