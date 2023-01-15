def calcula_puntos(event, acciones):
    '''
    Funcion que cuenta los puntos parciales realizados
    '''
    global puntos_casillas
    global puntos_parciales
    global contador_clics_c1
    global contador_clics_c2
    global contador_clics_c3
    global contador_clics_ord
    global contador_clics_cereza

    for i in range(len(acciones)):
        if (int(acciones[i]['x1']) <= event.x < int(acciones[i]['x2']) and
                int(acciones[i]['y1']) <= event.y < int(acciones[i]['y2'])):
            if str(acciones[i]['nombre']).__contains__("1_capa"):
                contador_clics_c1 = +1
                if (contador_clics_c1 >= (int(acciones[i]['max']))):
                    puntos_casillas[i]= 3
                else:
                    puntos_casillas[i] = puntos_casillas[i] + 1
            elif str(acciones[i]['nombre']).__contains__("2_capas"):
                contador_clics_c2 = +1
                if (contador_clics_c2 >= (int(acciones[i]['max']))):
                    puntos_casillas[i] = 6
                else:
                    puntos_casillas[i] = puntos_casillas[i] + 2
            elif str(acciones[i]['nombre']).__contains__("3_capas"):
                contador_clics_c3=+1
                if (contador_clics_c3 >= (int(acciones[i]['max']))):
                    puntos_casillas[i] = 9
                else:
                    puntos_casillas[i] = puntos_casillas[i] + 3
            elif str(acciones[i]['nombre']).__contains__("orden"):
                contador_clics_ord=+1
                if contador_clics_ord >= (int(acciones[i]['max'])):
                    puntos_casillas[i] = 21
                else:
                    puntos_casillas[i] = puntos_casillas[i] + 7
            elif str(acciones[i]['nombre']).__contains__("cereza"):
                contador_clics_cereza=+1
                if (contador_clics_cereza >= (int(acciones[i]['max']))):
                    puntos_casillas[i] = 9
                else:
                    puntos_casillas[i] = puntos_casillas[i] + 3

            posicion = (i // 5)
            puntos_parciales[posicion] = puntos_parciales[posicion]+puntos_casillas[i]
            contador_clics=puntos_parciales[posicion]


    #contador_clics = (contador_clics_c1 + contador_clics_c2 + contador_clics_c3 + contador_clics_ord
                     # + contador_clics_cereza)
    muestra_puntos(contador_clics, listaResultados, posicion)
    #datos_a_txt(contador_clics_c1, contador_clics_c2, contador_clics_c3, contador_clics_ord, contador_clics_cereza, contador_clics)
