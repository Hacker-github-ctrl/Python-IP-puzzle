#!/usr/bine/env python3
import time
import os
import requests
import json


def consulta():
  os.system("apt install python3")
  time.sleep(3)
  os.system("clear")


ip = input("Digite o Endereço de IP: ")
if ip == 9:
  print("\nNão foi possivel achar o IP!")
  exit()

r = requests.get(f"https://ipinfo.io/{ip}/json")

for ip in r.json():
  os.system("clear")
  print("\nIP HACKEADO!")
  print("\n")
  print("\nIP: ", r.json()["ip"])
  print("\nCidade: ", r.json()["city"])
  print("\nRegião: ", r.json()["region"])
  print("\nPaís: ",a r.json()["country"])
  print("\nLocalização: ", r.json()["loc"])
  print("\nOrganização: ", r.json()["org"])

print("\n")
print("\nObrigdo pelo o uso do meu Script ;)")
