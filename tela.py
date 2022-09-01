
# Projeto 

# Fazer uma janela de pedidos  do tipo de sanduíche que o cliente quer(como se fosse um pedido no fast food "subway")
# Foi utilizado a biblioteca "PySimpleGUI" para fazer a tela de interação com o usuário

import PySimpleGUI as sg

# 1 - tela inicial
def Iniciar():
    
    sg.theme('GreenTan')

    layout = [

        [sg.Text('Digite o nome:')],
        [sg.Input(key = 'Nome')],
        [sg.Button('Enter')]
    ]

    return sg.Window('Nome do cliente', layout = layout , finalize= True)

# 2 - Tela de escolher o tamanho do pão

def Tamanho_pedido():
    
    sg.theme('GreenTan')

    layout = [

        [sg.Text('Escolha o tamanho do sandwíche:')],
        [sg.Radio('15 cm','sandwíche_tam',size=(10,0),key = 'sandwíche_15'),sg.Radio('30 cm','sandwíche_tam',key = 'sandwíche_30')],
        [sg.Button('Enter')]
    ]

    return sg.Window('Tamanho ', layout = layout , finalize= True)

# 3 - Tela de escolher o tipo de pão

def Tipo_pao():
    
    sg.theme('GreenTan')

    layout = [

        [sg.Text('Escolha o tipo de pão:')],
        [sg.Radio('3 queijos','tipo_pao',size=(15,0), key = 'pao_3_queijos'),                 sg.Radio('9 grãos','tipo_pao', key = 'pao_9_grãos')],
        [sg.Radio('Granola salgada','tipo_pao',size=(15,0), key = 'pao_Granola_salgada')         ,sg.Radio('Italiano branco','tipo_pao', key = 'pao_Italiano_branco')],
        [sg.Radio('Manteiga temperada','tipo_pao',size=(15,0), key = 'pao_Manteiga_temperada')   ,sg.Radio('Parmesão e orégano','tipo_pao', key = 'pao_Parmesão_orégano')],
        [sg.Button('Enter')]

    ]

    return sg.Window('Tipo de pão ', layout = layout , finalize= True)


# 4 - Tela de escolher o recheio

def Tipo_recheio():
    
    sg.theme('GreenTan')

    layout = [

        [sg.Text('Escolha o tipo de recheio:',size=(22,0))],
        [sg.Checkbox('Cheddar', key = 'recheio_Cheddar')],
        [sg.Checkbox('Suíço', key = 'recheio_Suíço')],
        [sg.Checkbox('Queijo Mussarela Ralada', key = 'recheio_Mussarela_Ralada')],
        [sg.Button('Enter')]
    ]

    return sg.Window('Recheio', layout = layout , finalize= True)

# 5 - Tela de escolher a carne

def Tipo_carne():
    
    sg.theme('GreenTan')

    layout = [

        [sg.Text('Escolha o tipo de carne:',size=(22,0))],
        [sg.Radio('Boi','tipo_carne', key = 'carne_Boi')],
        [sg.Radio('Frango','tipo_carne', key = 'carne_Frango')],
        [sg.Radio('Peixe','tipo_carne', key = 'carne_Peixe')],
        [sg.Button('Enter')]
    ]

    return sg.Window('Carne', layout = layout , finalize= True)



# 6 - Tela de escolher o vegetal

def Tipo_vegetal():
    
    sg.theme('GreenTan')

    layout = [

        [sg.Text('Escolha o tipo de vegetal:')],
        [sg.Checkbox('Azeitona',size=(9,0), key = 'vegetal_Azeitona'),sg.Checkbox('Picles',size=(9,0), key = 'vegetal_Picles'),sg.Checkbox('Pepinos',size=(9,0), key = 'vegetal_Pepinos'),sg.Checkbox('Pimentão',size=(12,0), key = 'vegetal_Pimentão'),sg.Checkbox('Alface',size=(9,0), key = 'vegetal_Alface')],
        [sg.Checkbox('Cebola Roxa',size=(9,0), key = 'vegetal_Cebola_Roxa'),sg.Checkbox('Tomate',size=(9,0), key = 'vegetal_Tomate'),sg.Checkbox('Rúcula',size=(9,0), key = 'vegetal_Rúcula'),sg.Checkbox('Cenoura Ralada',size=(12,0), key = 'vegetal_Cenoura_Ralada'),sg.Checkbox('Vinagrete',size=(9,0), key = 'vegetal_Vinagrete')],
        [sg.Button('Enter')]

    ]

    return sg.Window('Tipo de vegetal', layout = layout , finalize = True)

# 7 - Tela de escolher molho

def Tipo_molho():
    
    sg.theme('GreenTan')

    layout = [

        [sg.Text('Escolha o tipo de molho:')],
        [sg.Checkbox('Cebola Agridoce',size=(12,0), key = 'molho_Cebola_Agridoce'),sg.Checkbox('Chipotle',size=(9,0), key = 'molho_Chipotle'),sg.Checkbox('Barbecue',size=(12,0), key = 'molho_Barbecue')],
        [sg.Checkbox('Parmesão',size=(12,0), key = 'molho_Parmesão'),sg.Checkbox('Maionese',size=(9,0), key = 'molho_Maionese'),sg.Checkbox('Mostarda e Mel',size=(12,0), key = 'molho_Mostarda_Mel')],
        [sg.Button('Enter')]
    ]

    return sg.Window('Tipo de vegetal', layout = layout , finalize = True)

def Pedido_final():
    
    sg.theme('GreenTan')

    layout =[

        [sg.Text('Pedido realizado:')],
        [sg.Button('Verificar')],
        [sg.Output(size = (30,20))]
    ]

    return sg.Window('Pedido final', layout = layout , finalize = True)


# Criando as variáveis que irão armazenar as janelas criadas
janela_iniciar , janela_tamanho_pedido , janela_pao, janela_recheio, janela_carne , janela_vegetal, janela_molho,janela_pedido_final  = Iniciar() , None , None, None, None, None, None, None

# Criando uma lista vazia na qual irá armazenar quais foram as opções escolhidas(True) e quais não foram escolhidas(False)
lista = []

# Lista que armazena o nome de todas as opções disponíveis no programa
lista_nomes = ['nome:','pão de 15cm:','pão de 30cm:','três queijos:','nove grãos:','granola salgada:','italiano branco:','manteiga temperada:','parmesão e orégano:','cheddar:','suíço:',
               'mussarela:','boi:','frango:','peixe:','azeitona:','picles:','pepino:','pimentao:','alface:','cebola roxa:','tomate:','rúcula:','cenoura ralada:','vinagrete:','cebola agridoce:',
               'chipotle:','barbecue:','parmesão:','maionese:','mostarda e mel:'
]

# Criando o "loop" que mantém a janela aberta
while True:
    window , event , values = sg.read_all_windows()     
    
    #Tela Inicial:

    # -Fechando Tela inicial
    if window == janela_iniciar and event == sg.WIN_CLOSED:
        break

    # -Indo da Tela "inicial" para a Tela "tamanho do pedido"
    if window == janela_iniciar and event == 'Enter':
        nome = values['Nome']
        

        lista.append(nome)
        
        janela_tamanho_pedido = Tamanho_pedido()
        janela_iniciar.hide()
    
    #Tela Tamanho do pedido:
    
    # -Fechando Tela do tamanho do pedido
    if window == janela_tamanho_pedido and event == sg.WIN_CLOSED:
        break

    # -Indo da Tela "tamanho do pedido"  para a Tela "tipo de pão"
    if window == janela_tamanho_pedido and event == 'Enter':
        pao_15 = values['sandwíche_15']
        pao_30 = values['sandwíche_30']
        

        lista.append(pao_15)
        lista.append(pao_30)

        janela_pao = Tipo_pao()
        janela_tamanho_pedido.hide()
    
    #Tela Tipo de pão:
    

    # -Fechando Tela do tipo de pão
    if window == janela_pao and event == sg.WIN_CLOSED:
        break

    # -Indo da Tela "tipo de pão" para a Tela "tipo de recheio"
    if window == janela_pao and event == 'Enter':
        tres_queijos = values['pao_3_queijos']
        nove_graos = values['pao_9_grãos']
        granola_salgada = values['pao_Granola_salgada']
        italiano_branco = values['pao_Italiano_branco']
        manteiga_temperada = values['pao_Manteiga_temperada']
        parmesao_oregano = values['pao_Parmesão_orégano']
        

        lista.append(tres_queijos)
        lista.append(nove_graos)
        lista.append(granola_salgada)
        lista.append(italiano_branco)
        lista.append(manteiga_temperada)
        lista.append(parmesao_oregano)


        janela_recheio = Tipo_recheio()
        janela_pao.hide()
    
    #Tela Tipo de recheio:   

    # -Fechando Tela do tipo de recheio
    if window == janela_recheio and event == sg.WIN_CLOSED:
        break

    # -Indo da Tela "tipo de recheio" para a Tela "tipo de carne"
    if window == janela_recheio and event == 'Enter':
        cheddar = values['recheio_Cheddar']
        suico = values['recheio_Suíço']
        mussarela = values['recheio_Mussarela_Ralada']
        

        lista.append(cheddar)
        lista.append(suico)
        lista.append(mussarela)
     


        janela_carne = Tipo_carne()
        janela_recheio.hide()
    
    #Tela tipo de carne:

    # -Fechando Tela do tipo de carne
    if window == janela_carne and event == sg.WIN_CLOSED:
        break

    # -Indo da Tela "tipo de carne" para a Tela "tipo de vegetal"
    if window == janela_carne and event == 'Enter':
        boi = values['carne_Boi']
        frango = values['carne_Frango']
        peixe = values['carne_Peixe']
        

        lista.append(boi)
        lista.append(frango)
        lista.append(peixe)



        janela_vegetal = Tipo_vegetal()
        janela_carne.hide()

    #Tela tipo de vegetal:

    
    # -Fechando Tela do tipo de vegetal
    if window == janela_vegetal and event == sg.WIN_CLOSED:
        break

    # -Indo da Tela "tipo de vegetal" para a Tela "tipo de molho"
    if window == janela_vegetal and event == 'Enter':
        azeitona = values['vegetal_Azeitona']
        picles = values['vegetal_Picles']
        pepino = values['vegetal_Pepinos']
        pimentao = values['vegetal_Pimentão']
        alface = values['vegetal_Alface']
        cebola_roxa = values['vegetal_Cebola_Roxa']
        tomate = values['vegetal_Tomate']
        rucula = values['vegetal_Rúcula']
        cenoura_ralada = values['vegetal_Cenoura_Ralada']
        vinagrete = values['vegetal_Vinagrete']
        

        lista.append(azeitona)
        lista.append(picles)
        lista.append(pepino)
        lista.append(pimentao)
        lista.append(alface)
        lista.append(cebola_roxa)
        lista.append(tomate)
        lista.append(rucula)
        lista.append(cenoura_ralada)
        lista.append(vinagrete)



        janela_molho = Tipo_molho()
        janela_vegetal.hide()

    #Tela tipo de molho:

    # -Fechando Tela do tipo de molho
    if window == janela_molho and event == sg.WIN_CLOSED:
        break
    
    # -Indo da Tela "tipo de molho" para a Tela "pedido final"
    if window == janela_molho and event == 'Enter':
        cebola_agridoce = values['molho_Cebola_Agridoce']
        chipotle = values['molho_Chipotle']
        barbecue = values['molho_Barbecue']
        parmessao = values['molho_Parmesão']
        maionese = values['molho_Maionese']
        mostarda_mel = values['molho_Mostarda_Mel']
        

        lista.append(cebola_agridoce)
        lista.append(chipotle)
        lista.append(barbecue)
        lista.append(parmessao)
        lista.append(maionese)
        lista.append(mostarda_mel)


        janela_pedido_final = Pedido_final()
        janela_molho.hide()

    #Tela tipo pedido final:
    
    # -Fechando Tela do pedido final
    if window == janela_pedido_final and event == sg.WIN_CLOSED:
        break
    
    if window == janela_pedido_final and event == 'Verificar':
        
        # Criando o loop que faz aparecer na tela só as opções selecionadas pelo usuário
        i = 0
        while i < len(lista):
            
            if lista[i] == False:
                pass
            else:
                print(lista_nomes[i],lista[i])
            i = i + 1
        

        

    
    

    

    

    
    
    

    
    


   
    
    
    
    
    

    

    

    

    
    
    