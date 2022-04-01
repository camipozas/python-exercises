'''Imaginemos que para ingresar al banco por primera vez nos dan una clave que ya viene dada. Nosotros ingresaremos la clave y mientras no sea, no accederemos'''

clave_banco = 'banco123'
primera_clave = (input('Ingrese primera clave: '))

if (primera_clave == clave_banco):
  print('Redireccionando al banco ...')
else:
  print('Intente nuevamente')