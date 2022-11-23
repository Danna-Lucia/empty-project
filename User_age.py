from datetime import datetime
def run():

print('''Edad segun tu fecha de nacimiento''')
fecha=(input('''ingresa le fecha de tu nacimiento con el siguiente formato: DD,MM,YYYY'''))

f_hoy=datetime.today().strftime('%d,%m,%Y')
fecha=fecha.split(',')
f_hoy=f_hoy.split(',')

if int(f_hoy[1]) > int(fecha[1]) or int(f_hoy[1]) == int(fecha[1]) and int(f_hoy[0]) >= int(fecha[0]):
r=int(f_hoy[2])-int(fecha[2])
print('Tienes ' + str(r) + ' años')
else:
r=int(f_hoy[2])-int(fecha[2])-1
print('Tienes ' + str(r) + ' añ

if __name__=="__main__":
run()