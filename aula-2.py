from lib.controller import Supervisor

def_robo = "youBot"

supervisor = Supervisor() # criando um objeto para o supervisor do robo

node = supervisor.getFromDef(def_robo) # criando uma variavel para guardar o nó referente ao robô, obtido através da DEF

# dentro de cada nó existem vários Fields (Campos), que armazenam informações como rotação, posição, velocidade, torque, etc.

translation_field = node.getField("translation") # salvando o Filed de translação na variável translation_field
rotation_filed = node.getField("rotation") # salvando o Filed de rotação na variável rotation_field

print("\nAcessando os valores de translação do Nó\n")

# acessar a posição atráves do nó
# utilizando a função getPosition

node_position = node.getPosition()

print("Utilizando a função getPosition {}".format(node_position))

# acessar a posição através do Field

translation = translation_field.getSFVec3f()

print("Utilizando o field de translação {}".format(translation))

# Observa-se que o resultado é o mesmo, pois a função getPosition presente no nó executa os mesmos passos utilizados acima

print("\n\nAcessando os valores de rotação do Nó\n")

# # # # # # # # # # 

# acessar a orientação através do nó
# retorna a matriz de rotação do nó

node_orientation = node.getOrientation()

print("Utilizando a função getOrientation {}\n".format(node_orientation))

# acessar a orientação através do Field
# retorna a rotação em eixo-ângulo

orientation = rotation_filed.getSFRotation()

print("Utilizando o field de rotação {}".format(orientation))

# # # # # # # # # # # # # # # # # # # 

# alterando os valores de translação
# como ja observamos, quando chamamos a função que nos retorna a translação de um nó,
# obtemos uma lista de 3 elementos, sendo eles a posição em x, y e z, respectivamente.
# para alterarmos esses valores, também precisamos passar uma lista de 3 valores como parâmetro.

nova_posicao = [0.52, 0.25, 0.36]

# usaremos a funcao setSFVec3f do objeto translation_field

translation_field.setSFVec3f(nova_posicao)

# devemos informar os 4 valores para alterarmos a rotação. rx, ry, rz e alpha
# para alterar a rotação, seguimos os mesmos passos, porém utilizando o field de rotação

nova_rotacao = [.12, .5, .6, 1.57]

rotation_filed.setSFRotation(nova_rotacao)