import time
import pandas as pd

db = [[154,	'29-09-22 01:39',	'11',	4001,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[165,	'29-09-22 01:39',	'11',	4001,	'1'],
[11,	'29-09-22 01:39',	'11',	3660,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[150,	'29-09-22 01:40',	'11',	4005,	'1'],
[160,	'29-09-22 01:40',	'11',	4006,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[165,	'29-09-22 01:39',	'11',	4001,	'1'],
[11,	'29-09-22 01:39',	'11',	3660,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[150,	'29-09-22 01:40',	'11',	4005,	'1'],
[160,	'29-09-22 01:40',	'11',	4006,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[165,	'29-09-22 01:39',	'11',	4001,	'1'],
[11,	'29-09-22 01:39',	'11',	3660,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[150,	'29-09-22 01:40',	'11',	4005,	'1'],
[160,	'29-09-22 01:40',	'11',	4006,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[165,	'29-09-22 01:39',	'11',	4001,	'1'],
[11,	'29-09-22 01:39',	'11',	3660,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[150,	'29-09-22 01:40',	'11',	4005,	'1'],
[160,	'29-09-22 01:40',	'11',	4006,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[165,	'29-09-22 01:39',	'11',	4001,	'1'],
[11,	'29-09-22 01:39',	'11',	3660,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[150,	'29-09-22 01:40',	'11',	4005,	'1'],
[160,	'29-09-22 01:40',	'11',	4006,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[165,	'29-09-22 01:39',	'11',	4001,	'1'],
[11,	'29-09-22 01:39',	'11',	3660,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[150,	'29-09-22 01:40',	'11',	4005,	'1'],
[160,	'29-09-22 01:40',	'11',	4006,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[165,	'29-09-22 01:39',	'11',	4001,	'1'],
[11,	'29-09-22 01:39',	'11',	3660,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[150,	'29-09-22 01:40',	'11',	4005,	'1'],
[160,	'29-09-22 01:40',	'11',	4006,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[165,	'29-09-22 01:39',	'11',	4001,	'1'],
[11,	'29-09-22 01:39',	'11',	3660,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[150,	'29-09-22 01:40',	'11',	4005,	'1'],
[160,	'29-09-22 01:40',	'11',	4006,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[165,	'29-09-22 01:39',	'11',	4001,	'1'],
[11,	'29-09-22 01:39',	'11',	3660,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[176,	'29-09-22 01:40',	'11',	4001,	'1'],
[150,	'29-09-22 01:40',	'11',	4005,	'1'],
[160,	'29-09-22 01:40',	'11',	4006,	'1'],
[22,	'29-09-22 01:40',	'11',	3660,	'1']]



#recebe como par??metro a matriz do n??
#retornaDataFrame com ??ltima ocorr??ncia de cada ID
def ultimaoOcorrencia(db):
    listaHidrometros = []
    unicaOcorencia = []
    aux = 0
    for hidrometro in db: #para criar uma lista com a ??ltima ocorr??ncia daquele hidr??metro
        id = hidrometro[3]        
        if id not in listaHidrometros: 
            listaHidrometros.append(id)
            unicaOcorencia.append(hidrometro)
            print(listaHidrometros)            
            aux = listaHidrometros.index(id)
        else:
            aux = listaHidrometros.index(id)
            unicaOcorencia.pop(aux)
            unicaOcorencia.append(hidrometro) 
            listaHidrometros.pop(aux)
            listaHidrometros.append(id)        
    tabelaDB =  pd.DataFrame(unicaOcorencia, columns= ['Litros Utilizados', 'Hor??rio', 'Vazao atual', 'ID', 'Situacao']) #dataFrame com a ??ltima ocrr??ncia de cada ID
    print('PRINT TABELA DB \n',tabelaDB)
    return tabelaDB

#retorna lista elencando os que mais gastaram
def maiorGasto(tabelaDB):
    listaTratada = []
    hidroAux = 0
    ordenado = tabelaDB.sort_values('Litros Utilizados', ascending=False)
    print('dataframe ordenado', ordenado)
    listaOrdenado = ordenado.values.tolist()
    for hidro in listaOrdenado:
        print('ID:', hidro[3], 'Litros utilizados:', hidro[0])
        hidroAux = str(hidro[3])+ ',' + str(hidro[0]) + ',' #para facilitar a parte do envio
        listaTratada.append(hidroAux)
    return listaTratada
    
    
    #agora enviamos para o servidor central

#retorna a m??dia do n??/ utiliza o dataFrame para isso
def mediaNo(tabelaDB):
    media = tabelaDB['Litros Utilizados'].median()
    print('A m??dia de litros utilizados ??: ', media)
    return media

#bloqueia o hidr??metro por m??dia geral do sistema
def bloqueioMediaGeral(tabelaDB, mediaGeral):
    print('bloqueio media geral')    
    bloqueioTabelaMediaGeral = tabelaDB.loc[tabelaDB['Litros Utilizados'] > mediaGeral] #filtramos com a m??dia geral
    # bloqueioTabelaMediaGeral = tabelaDB.loc[tabelaDB['Litros Utilizados'] > mediaGeral, ['ID']] #aqui ir?? retornar o ID
    print(bloqueioTabelaMediaGeral)

#bloqueia hidr??metros por seu teto de gastos
def bloqueioTetoGasto(tabelaDB, tetoGasto):
    print('BLOQUEIO TETO DE GASTOS')
    bloqueioTabelaTestoGasto = tabelaDB.loc[tabelaDB['Litros Utilizados'] > tetoGasto] #filtramos com o teto de gasto #o teto de gasto deve ser verificado ta todo momemento
    print(bloqueioTabelaTestoGasto)
    #depois ?? s?? pegar as id que foram retornadas


dataFrame = ultimaoOcorrencia(db)
maiorGasto(dataFrame)

