def pyramid(layers):
    star = '*'
    for i in range(layers):
       
        print(star.center(layers*2, ' '))
        star += '**'

pyramid(9)        