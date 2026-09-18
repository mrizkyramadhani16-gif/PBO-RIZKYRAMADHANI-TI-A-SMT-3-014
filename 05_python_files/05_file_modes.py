# Mode file: r (read), w (write), a (append)
with open('mode.txt', 'w') as file:
    file.write('Contoh mode write.')
with open('mode.txt', 'r') as file:
    print(file.read())
