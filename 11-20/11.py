# ping bot
# this code will ping ip's/domains

from os import system

x = input("what ip do you want to ping? >>>")

system(f"ping {x} -t 5")






