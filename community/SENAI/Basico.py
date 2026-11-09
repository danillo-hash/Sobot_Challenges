#!/usr/bin/python3
"""
Solis Robot - SoBot

Desafio001.py: Resolução do Desafio 001 com rampas corrigidas (AT500/DT500)
para curvas exatas de 90° e deslocamento 100% de frente no retorno.

Company: Solis Tecnologia
"""

from time import sleep
import serial

# Configuração da porta serial
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()

# Habilita os motores
usb.write(b"MT0 E1")
sleep(0.5)

# ==========================================
# 1. PERCURSO AZUL (IDA)
# ==========================================

# 1. Avançar (500mm) | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 2. Giro de 90° à Esquerda (Rampa de 500ms para giro completo) | LED Azul
usb.write(b"LT E1 RD0 GR0 BL50")
usb.write(b"MT0 E1 D90 L AT500 DT500 V10")
sleep(3.5)

# 3. Avançar (500mm) | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 4. Giro de 90° à Direita | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT500 DT500 V10")
sleep(3.5)

# 5. Avançar (500mm - topo do trecho azul) | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# ==========================================
# 2. TRANSIÇÃO: MEIA-VOLTA (180°) E ROXO DE FRENTE
# ==========================================

# 6a. Meia-volta de 180° no topo | LED Vermelho
usb.write(b"LT E1 RD50 GR0 BL0")
usb.write(b"MT0 E1 D180 R AT1000 DT1000 V10")
sleep(5.5)

# 6b. Avançar de frente (500mm) no trecho roxo | LED Vermelho
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# ==========================================
# 3. PERCURSO ROXO DE RETORNO AO INÍCIO
# ==========================================

# 7. Giro de 90° à Esquerda (para seguir para a direita no papel) | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 L AT500 DT500 V10")
sleep(3.5)

# 8. Avançar (500mm) | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 9. Giro de 90° à Direita (para descer no papel) | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT500 DT500 V10")
sleep(3.5)

# 10. Avançar (500mm - chega ao lado da posição de início) | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 11. Giro de 90° à Esquerda para entrar de frente na posição inicial | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 L AT500 DT500 V10")
sleep(3.5)

# Finalização: Desliga a fita LED e os motores
usb.write(b"LT E0")
usb.write(b"MT0 E0")
sleep(0.5)
usb.close()
