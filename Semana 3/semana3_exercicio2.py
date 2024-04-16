produto1_0050 = 5
produto2_0054 = 10

selecao_produto1 = int(input("Quantos produtos 1 você quer adicionar ao carrinho? "))
selecao_produto2 = int(input("Quantos produtos 2 você quer adicionar ao carrinho? "))

valor_produto1 = produto1_0050*selecao_produto1
valor_produto2 = produto2_0054*selecao_produto2

if selecao_produto1 == 1 and selecao_produto2 == 0:
        print("O valor da sua compra é R$ ", produto1_0050, ",00. Que tal adicionar mais um produto para ganhar descontos? :) ", sep = "")

elif selecao_produto1 == 0 and selecao_produto2 == 1:
         print("O valor da sua compra é R$ ", produto2_0054, ",00. Que tal adicionar mais um produto para ganhar descontos? :) ", sep = "")

elif selecao_produto1 >= 2 and selecao_produto2 == 0:
        print("Maravilha! Você ganhou R$ 5,00 de desconto! O valor da sua compra é R$ ", (valor_produto1)-5, ",00.", sep = "")

elif selecao_produto1 == 0 and selecao_produto2 >= 2:
        print("Maravilha! Você ganhou R$ 5,00 de desconto! O valor da sua compra é R$ ", (valor_produto2)-5, ",00.", sep = "")

elif selecao_produto1 >= 1 and selecao_produto2 >= 1:
        print("Uhul! Você ganhou 50% de desconto! :D. O valor da sua compra é R$", (valor_produto1+valor_produto2)/2)





