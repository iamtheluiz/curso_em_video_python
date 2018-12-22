n1 = float(input('Um valor: '))
n2 = float(input('Outro valor: '))

soma  = n1 + n2
mult  = n1 * n2
div   = n1 / n2
div_i = n1 // n2
expo  = n1 ** n2

print('{} + {} = {}'.format(n1, n2, soma))
print('{} x {} = {}'.format(n1, n2, mult))
print('{} / {} = {:.3f}'.format(n1, n2, div))
print('{} // {} = {}'.format(n1, n2, div_i))
print('{} ^ {} = {}'.format(n1, n2, expo))
