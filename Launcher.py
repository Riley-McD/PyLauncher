import os
os.system("color a")

print "Welcome To Abconsender's MineCraft Launcher!"
print "Choose your options) "

print "1) Vanilla"
print "2) Optifine"

Opt = raw_input("> ")


if Opt == 1:
    Vanilla()


def Vanilla():
    import os
    os.system("RunLaunch.bat")

    
def Optifine():
    import os
    os.system("Optifine.bat")
