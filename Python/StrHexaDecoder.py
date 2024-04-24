import numpy as np
np.set_printoptions( threshold=40 ) # máximo de elementos de um array a serem mostrados no print

# = = = = = = = = = = = = = = = = = #
def DecoderStrHexaSeparador(txt, separador):
    vetor = txt.split(separador)
    
    #Descomente as linhas a seguir se quiser ver os caracteres individualmente
    #print("Array cortado: ")
    #print(vetor)
    #print("")

    print("Frase desconvertida para texto comum: \n")
    for c in vetor:
        # A função 'int(c, 16)' converte os valores hexadecimais em decimais,
        # que alimentam a função 'chr(int(base10))', que irá retornar o respectivo caractere
        print(chr(int(c, 16)), end="")
    print()
        
def DecoderStrHexaPlainText(txt):
    tamanho = len(txt)
    vetor = []
    
    for i in range(0, tamanho-1, 2):
        vetor.append(txt[i] + txt[i+1])
        
    #Descomente as linhas a seguir se quiser ver os caracteres individualmente
    #print("Array cortado: ")
    #print(vetor)
    #print("")

    print("Frase desconvertida para texto comum: \n")
    for c in vetor:
        # A função 'int(c, 16)' converte os valores hexadecimais em decimais,
        # que alimentam a função 'chr(int(base10))', que irá retornar o respectivo caractere
        print(chr(int(c, 16)), end="")
    print()
# = = = = = = = = = = = = = = = = = #

#Exemplo 1:
strHex1 = "59%69%70%70%65%68%21%20%59%6F%75%72%20%55%52%4C%20%69%73%20%63%68%61%6C%6C%65%6E%67%65%2F%74%72%61%69%6E%69%6E%67%2F%65%6E%63%6F%64%69%6E%67%73%2F%75%72%6C%2F%73%61%77%5F%6C%6F%74%69%6F%6E%2E%70%68%70%3F%70%3D%6C%69%73%62%61%67%6F%6F%66%67%64%68%26%63%69%64%3D%35%32%23%70%61%73%73%77%6F%72%64%3D%66%69%62%72%65%5F%6F%70%74%69%63%73%20%56%65%72%79%20%77%65%6C%6C%20%64%6F%6E%65%21"
DecoderStrHexaSeparador(strHex1, "%")

print("\n - - - - - - - - - - - \n")

#Exemplo 2:
strHex2 = "4573746520c3a920756d206578656d706c6f20646520746578746f2c20706f7274616e746f206ec3a36f2068c3a1206e6563657373696461646520646520636f6d706c65786964616465206465736e6563657373c3a17269612e"
DecoderStrHexaPlainText(strHex2)
