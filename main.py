inputfreq = []
consonant = []
print("Separate each item with space bar.")
inputfreq =input("Enter frequencies/ratios, from the tonic to octave:")
consonant = inputfreq.split()
octaveratio = float(consonant[-1])/float(consonant[0])
cent = -5
lowerratio = 2**(cent/1200)
cent = 5
upperratio = 2**(cent/1200)
b = 1
n = 4
s = 1
scale = []
while n < 40:
    while s < (n+1):
        cal = float(consonant[0])*float(octaveratio**(s/n))
        while b < len(consonant):
            if cal/float(consonant[b]) < upperratio and cal/float(consonant[b]) > lowerratio:
                scale.append(cal)
            else:
                pass
            b += 1
            if len(scale) == (len(consonant)-1):
                print("Found",n,"-TET")
                scale.clear()
            else:
                pass
        s += 1
        b = 1
    scale.clear()
    n += 1
    s = 0
print("Nothing/nothing more is found, under",n,"-TET. Within boundary of +/-:",cent,"cents")