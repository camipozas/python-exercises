'''Imaginemos que para ingresar al banco por primera vez nos dan una clave que ya viene dada. Nosotros ingresaremos la clave y mientras no sea, no accederemos'''

# The variable `clave_banco` is assigned the value `banco123`. The variable `primera_clave` is
# assigned the value entered by the user. If the value entered by the user is equal to the value of
# `clave_banco`, the user is redirected to the bank. Otherwise, the user is asked to try again.
clave_banco = 'banco123'
primera_clave = (input('Ingrese primera clave: '))

if (primera_clave == clave_banco):
    print('Redireccionando al banco ...')
else:
    print('Intente nuevamente')
