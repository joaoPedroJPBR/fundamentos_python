#dicionarios
agenda = {
    'Maria': [123456789, 99887755],
    'João': [987654321, 99887766],
    'Joaquim': [123456789, 99887777],
}

for i in agenda:
    print(i)
     
for i in enumerate(agenda):
    print(i)
    
for i in enumerate(agenda, start=20):
    print(i)

for i in agenda.items():
    print(i)
    
for i in enumerate(agenda.items()):
    print(i)
