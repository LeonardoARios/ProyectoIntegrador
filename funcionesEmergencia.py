def presupuestar(lista):
    print(lista)
    buscaDNI = input("Ingrese el DNI a facturar\n>  ")
    if buscaDNI in lista.keys():
        print("="*70)
        for nombre,dato1 in lista[buscaDNI].items():
            if nombre == 'mascotas':
                continue
            print(f'{nombre}:{dato1}')
        print("="*70)
        for mascotas,datos in lista[buscaDNI].items():
            if mascotas == 'mascotas':
                print(f'Cantidad de Mascotas Registrado: {len(datos)}')
        for nombres in lista[buscaDNI][mascotas]:
            for key, value in nombres.items():
                if key == 'nombre Mascota':
                    print(f'Nombre de Mascota: {value}')
        print("="*70)
    while True:
        pregu1 = input("Desea hacer factura de este paciente?\n>  ").upper()
        if pregu1 == "S":
            servi = {"Vacuna":3000,
                     "Consulta":6000,
                     "Castacion":7000,
                     "Analisis":4000,
                     "Radiografia":5000,
                     "Ecografia":6000}
            print()
            print("Datos y Precios:")
            print("="*70)
            num = 1
            for servicio,precio in servi.items():
                print(f'{num} {servicio}: ${precio}')
                num += 1
                total = 0 
            print("="*70)
            while True:
                pregu2 = input("Seleccione los servicios que desea facturar\n>  ").upper()
                if pregu2 == "1":
                    suma1 = servi['Vacuna']
                    print((servi.values())[0])
                    total += suma1
                elif pregu2 == "2":
                    suma2 = servi['Consulta']
                    print(suma2)
                    total += suma2
                elif pregu2 == "3":
                    suma3 = servi['Castacion']
                    print(suma3)
                    total += suma3
                elif pregu2 == "4":
                    suma4 = servi['Analisis']
                    print(suma4)
                    total += suma4
                elif pregu2 == "5":
                    suma5 = servi['Radiogafria']
                    print(suma5)
                    total += suma5
                elif pregu2 == "6":
                    suma6 = servi['Ecografia']
                    print(suma6)
                    total += suma6
                else:
                    print()
                
        else:
            input("Presione Enter para continuar")
            break 
    return