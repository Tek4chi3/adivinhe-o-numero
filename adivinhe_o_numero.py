from random import randint
from time import sleep
pontos=0
random_num1=randint(1,3)
random_num2=randint(1,5)
random_num3=randint(1,10)
choosed_num=int(input('Estou pensando em um número de 1 a 3. Tente adivinhar qual é:'))
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
if choosed_num==random_num1:
    pontos+=1
    print(f'Você digitou o número {choosed_num} e \033[0;32macertou\033[m')
    sleep(2)
    print('Vamos dificultar as coisas...')
    choosed_num = int(input('Estou pensando em um número de 1 a 5. Tente adivinhar qual é:'))
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    if choosed_num==random_num2:
        pontos += 1
        print(f'Você digitou o número {choosed_num} e \033[0;32macertou\033[m')
        sleep(2)
        print('Agora, um último desafio...')
        choosed_num = int(input('Estou pensando em um número de 1 a 10. Tente adivinhar qual é:'))
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        if choosed_num==random_num3:
            pontos += 1
            print(f'Você digitou o número {choosed_num} e \033[0;32macertou\033[m')
            print('Você é muito bom em adivinhar o que estou pensando! Parabéns!')
        else:
            print(f'Você digitou o número {choosed_num} e \033[0;31merrou\033[m.Pensei no número {random_num3}')
    else:
        print(f'Você digitou o número {choosed_num} e \033[0;31merrou\033[m.Pensei no número {random_num2}')

else:
    print(f'Você digitou o número {choosed_num} e \033[0;31merrou\033[m.Pensei no número {random_num1}')
print(f'Sua pontuação: {pontos} de um total de 3 pontos')
if pontos==3:
    print('Parabéns!')
elif pontos==2:
    print('Foi quase...')
else:
    print('Boa sorte na próxima vez')
print('Fim do programa')