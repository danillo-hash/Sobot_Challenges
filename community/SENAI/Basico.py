#!/usr/bin/python3
"""
Solis Robot - SoBot

Desafio001.py: Resolução do Desafio 001 com rampas oficiais Solis (AT3950/DT3950)
para curvas perfeitas de 90° e giro final de 180° para retornar ao início.

Company: Solis Tecnologia
"""

from time import sleep
import serial

# Configura a porta serial (padrão Raspberry Pi / Solis)
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()     # Aguarda configuração dos dados

# Habilita os motores das rodas
usb.write(b"MT0 E1")
sleep(0.5)

# --- BLOCO AZUL (IDA) ---

# 1. Avançar | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT2000 DT2000 V10")
sleep(7.5)

# 2. Esquerda (90° exatos com rampa Solis AT3950/DT3950) | LED Azul
usb.write(b"LT E1 RD0 GR0 BL50")
usb.write(b"MT0 E1 D90 L AT3950 DT3950 V10")
sleep(8.5)

# 3. Avançar | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT2000 DT2000 V10")
sleep(7.5)

# 4. Certo / Direita (90° eixo) | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(8.5)

# 5. Avançar | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT2000 DT2000 V10")
sleep(7.5)

# --- BLOCO ROXO (VOLTA AO INÍCIO) ---

# 6. Para trás (-500 mm) | LED Vermelho
usb.write(b"LT E1 RD50 GR0 BL0")
usb.write(b"MT0 E1 D-500 AT2000 DT2000 V10")
sleep(7.5)

# 7. Certo / Direita (90° eixo) | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(8.5)

# 8. Avançar | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT2000 DT2000 V10")
sleep(7.5)

# 9. Certo / Direita (90° eixo) | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(8.5)

# 10. Avançar (Retorna até a altura do início) | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT2000 DT2000 V10")
sleep(7.5)

# 11. Giro de 180° para a Esquerda para entrar no Início | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D180 L AT3950 DT3950 V10")
sleep(10.0)

# Finalização: Desliga a fita LED e desabilita os motores
usb.write(b"LT E0")
usb.write(b"MT0 E0")
sleep(0.5)
usb.close()
