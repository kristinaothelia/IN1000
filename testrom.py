from rom import Rom

romFil = open("OJD-rom.csv", "r")
alleRom = []

for linje in romFil :
    romData = linje.split(",")
    nyttRom = Rom(int(romData[0]), romData[1], romData[2], int(romData[3]))
    alleRom.append(nyttRom)

for rom in alleRom :
    if rom.passer(8, "Linux"):
        rom.skrivLinje()
