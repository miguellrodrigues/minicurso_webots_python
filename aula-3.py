from lib.controller import Supervisor, PositionSensor, Motor
from typing import cast

supervisor = Supervisor()

no_motor_esquerda = Motor("motor_esquerda")
no_motor_direita = Motor("motor_direita")

no_encoder_esquerda = PositionSensor("encoder_esquerda")
no_encoder_direita = PositionSensor("encoder_direita")

# ativnado os encoders com taxa de amostragem de 14 milisegundos

no_encoder_esquerda.enable(14)
no_encoder_direita.enable(14)

# configurando os motores

no_motor_esquerda.setPosition(float('inf'))
no_motor_direita.setPosition(float('inf'))

no_motor_esquerda.setVelocity(0.0)
no_motor_direita.setVelocity(0.0)

while supervisor.step(14) != -1:
    pass