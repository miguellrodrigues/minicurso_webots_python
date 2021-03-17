from lib.controller import Supervisor, Motor, PositionSensor
from math import pi


supervisor = Supervisor()

diametro_roda = 0.08
raio_roda = diametro_roda / 2.0

diametro_c = 0.1825
raio_c = diametro_c / 2.0

motores = []
encoders = []

ultima_posicao = [.0, .0, .0, .0]


for i in range(1, 5):
    motores.append(Motor("wheel{}".format(i)))
    encoders.append(PositionSensor("encoder{}".format(i)))


for motor in motores:
    motor.setPosition(float('inf'))
    motor.setVelocity(.0)


for encoder in encoders:
    encoder.enable(14)


def setar_velocidades(velocidades):
    for i in range(len(motores)):
        motores[i].setVelocity(velocidades[i])


def leitura_encoder(encoder):
    return encoders[encoder].getValue() * raio_roda


def virar(angulo):
    x = (pi * raio_c * angulo) / 180.0

    if x > 0:
        while leitura_encoder(2) - ultima_posicao[2] < x:
            setar_velocidades([2, -2, 2, -2])

            supervisor.step(16)
    else:
        while leitura_encoder(1) - ultima_posicao[1] < -x:
            setar_velocidades([-2, 2, -2, 2])

            supervisor.step(16)

    ultima_posicao[2] = leitura_encoder(2)
    ultima_posicao[1] = leitura_encoder(1)


while supervisor.step(16) != -1:
    virar(90)    
    virar(-90) 
