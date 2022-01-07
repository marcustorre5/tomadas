from time import sleep

while True:

    def tomadas():

        print('=' * 30)
        print('Tomadas para Cômodos')
        print('=' * 30)
        print(end=' \n')

        print(' [1] Suítes\n [2] Dormitórios\n [3] Cozinha\n [4] Sala\n ')

        tomadas = int(input('Seleciona o cômodo > '))

        if tomadas == 1:
            s = int(input('Digite o número de tomadas que vai ter > '))
            s1 = 1200/s
            s2 = s1/s
            print(s2,'W')

        if tomadas == 2:
            d = int(input('Digite o número de tomadas que vai ter > '))
            d1 = 1600/d
            d2 = d1/d
            print(d2,'W')

        if tomadas == 3:
            c = int(input('Digite o número de tomadas que vai ter > '))
            c1 = 2000/c
            c2 = c1/c
            print(c2,'W')

        if tomadas == 4:
            ss = int(input('Digite o número de tomadas que vai ter > '))
            ss1 = 1200/ss
            ss2 = ss1/ss
            print(ss2,'W')
    tomadas()

    sleep(2)

