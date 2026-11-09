#!/usr/bin/python3
"""
Solis Robot - SoBot

Desafio001.py: Resolução do Desafio 001 no padrão oficial da Solis Tecnologia.

Company: Solis Tecnologia
"""

from time import sleep
import serial

# Configura a porta serial (padrão Raspberry Pi / Solis)
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()     # Aguarda configuração dos dados

# Habilita os motores das rodas
usb.write(b"MT0 E1")
sleep(0.1)

# 1. Avançar | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT500 DT500 V10")
sleep(6.0)

# 2. Esquerda (90° eixo) | LED Azul
usb.write(b"LT E1 RD0 GR0 BL50")
usb.write(b"MT0 E1 D90 L AT500 DT500 V10")
sleep(3.5)

# 3. Avançar | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT500 DT500 V10")
sleep(6.0)

# 4. Certo / Direita (90° eixo) | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT500 DT500 V10")
sleep(3.5)

# 5. Avançar | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT500 DT500 V10")
sleep(6.0)

# 6. Para trás (-500 mm) | LED Vermelho
usb.write(b"LT E1 RD50 GR0 BL0")
usb.write(b"MT0 E1 D-500 AT500 DT500 V10")
sleep(6.0)

# 7. Certo / Direita (90° eixo) | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT500 DT500 V10")
sleep(3.5)

# 8. Avançar | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT500 DT500 V10")
sleep(6.0)

# 9. Certo / Direita (90° eixo) | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT500 DT500 V10")
sleep(3.5)

# 10. Avançar | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT500 DT500 V10")
sleep(6.0)

# 11. Certo / Direita (90° eixo) | LED Amarelo
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT500 DT500 V10")
sleep(3.5)

# Finalização: Desliga a fita LED e desabilita os motores
usb.write(b"LT E0")
usb.write(b"MT0 E0")
usb.close()
