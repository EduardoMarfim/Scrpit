def soma():

    val=input('Digite um valor: ')

    if(val.IsNumeric()):

        val=int(val)

        print('O valor digitado foi {0}'.format(val))

        pass

    else:

        print("Não é um número valido")

        pass


    pass


soma()