import subprocess


print("Geef  productnummer van leverancier door: ")
product_nummer = input()

if(len(product_nummer) == 7 ):
    print('[+] Dit is een kasius merk.')
else:   
    print("[-] Dit is geen kasius merk")

# subprocess.call(['C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Kladblok.exe'])


# 00151706 --> geen kasius
