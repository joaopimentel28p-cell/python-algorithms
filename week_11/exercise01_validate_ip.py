print('Hi! In this moment, for the verification, you need to enter your IP Address!')

while True:
    ip = input('Enter your IP separated by dots: ').strip()
    separated = ip.split(".")

    if len(separated) != 4:
        print(" Invalid: IPv4 must have exactly 4 octets.")
        continue

    valid = True 

    for parte in separated:

        if not parte.isdigit():
            print(f" Invalid: '{parte}' is not a number.")
            valid = False
            break

        numero = int(parte)

        if numero < 0 or numero > 255:
            print(f" Invalid: '{parte}' is out of range (0-255).")
            valid = False
            break

        if parte != "0" and parte.startswith("0"):
            print(f" Invalid: '{parte}' has leading zeros.")
            valid = False
            break

    if valid:
        print(f" '{ip}' is a valid IPv4 address!")
		
     
