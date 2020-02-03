new = open('red.ppm', 'w+')

new.write('P3\n')
new.write('500 500\n')
new.write('255\n')

def change(number):
    num = str(number)
    if len(num) == 2:
        num = ' ' + num
    if len(num) == 1:
        num = '  ' + num
    return num

for x in range(500):
    sp = ['255','255','255']
    for y in range(500):
        new.write(sp[0] + ' ' + sp[1] + ' ' + sp[2] + '\n')
        if (y % 2) == 1:
            sp[1] = change(int(sp[1]) - 1)
        else:
            sp[2] = change(int(sp[2]) - 1)

new.close()