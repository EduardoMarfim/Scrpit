def soma():

    val=input('Digite um valor: ')

    if(val.IsNumeric()):

        val=int(val)

        print('O valor digitado foi {0}'.format(val))

        retorno()

        pass

    else:

        print("Não é um número valido")

        pass


    pass


def retorno():

    resp=input('Deseja executar novamente?[s/n]: ')

    if(resp.lower()=='s'):

        #Recursividade do projeto
        
        soma()

        pass

    pass


soma()