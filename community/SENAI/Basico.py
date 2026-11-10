#!/usr/bin/python3
"""
Solis Robot - SoBot

Desafio001.py: Resolução do Desafio 001 com áudio do Bluetooth no início 
e efeito sonoro ("Butterfly") executado a cada curva.

Company: Solis Tecnologia
"""

import os
from time import sleep
import serial
import pygame

# --- NOMES DOS FICHEIROS DE ÁUDIO ---
AUDIO_INICIO = "bluetooth_ready.mp3"
AUDIO_CURVA = "butterfly.mp3"

def inicializar_audio():
    """Inicializa o sistema de som do Pygame."""
    try:
        pygame.mixer.init()
    except Exception as e:
        print(f"[AVISO] Não foi possível inicializar áudio: {e}")

def tocar_inicio():
    """Toca o som do Bluetooth ao ligar o robô."""
    if os.path.exists(AUDIO_INICIO):
        try:
            pygame.mixer.music.load(AUDIO_INICIO)
            pygame.mixer.music.play()
            print('[ÁUDIO] "The bluetooth device is ready to pair"')
        except Exception as e:
            print(f"[AVISO] Erro ao tocar áudio inicial: {e}")

def tocar_curva():
    """Toca o efeito sonoro ("Butterfly") em cada curva."""
    if os.path.exists(AUDIO_CURVA):
        try:
            som = pygame.mixer.Sound(AUDIO_CURVA)
            som.play()
            print('[ÁUDIO] 🎵 Efeito de curva: "Butterfly"')
        except Exception as e:
            print(f"[AVISO] Erro ao tocar áudio de curva: {e}")


# ==========================================
# INICIALIZAÇÃO DA CONEXÃO E ÁUDIO
# ==========================================

inicializar_audio()

# Configuração da porta serial (9600 bps padrão Solis)
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()

# Toca o som inicial do Bluetooth
tocar_inicio()

# Habilita os motores das rodas
usb.write(b"MT0 E1")
sleep(0.5)

# ==========================================
# 1. PERCURSO AZUL (IDA)
# ==========================================

# 1. Avançar (500mm) | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 2. Giro de 90° à Esquerda | LED Azul + SOM DA CURVA
tocar_curva()
usb.write(b"LT E1 RD0 GR0 BL50")
usb.write(b"MT0 E1 D90 L AT500 DT500 V10")
sleep(3.5)

# 3. Avançar (500mm) | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 4. Giro de 90° à Direita | LED Amarelo + SOM DA CURVA
tocar_curva()
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

# 6a. Meia-volta de 180° no topo | LED Vermelho + SOM DA CURVA
tocar_curva()
usb.write(b"LT E1 RD50 GR0 BL0")
usb.write(b"MT0 E1 D180 R AT1000 DT1000 V10")
sleep(5.5)

# 6b. Avançar de frente (500mm) no trecho roxo | LED Vermelho
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# ==========================================
# 3. PERCURSO ROXO DE RETORNO AO INÍCIO
# ==========================================

# 7. Giro de 90° à Esquerda | LED Amarelo + SOM DA CURVA
tocar_curva()
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 L AT500 DT500 V10")
sleep(3.5)

# 8. Avançar (500mm) | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 9. Giro de 90° à Direita | LED Amarelo + SOM DA CURVA
tocar_curva()
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT500 DT500 V10")
sleep(3.5)

# 10. Avançar (500mm - desce até ao lado do Início) | LED Verde
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V10")
sleep(6.0)

# 11. Giro de 180° à Direita para alinhar no Início | LED Amarelo + SOM DA CURVA
tocar_curva()
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D180 R AT1000 DT1000 V10")
sleep(5.5)

# Finalização: Parar áudios, desligar LEDs e motores
pygame.mixer.stop()
usb.write(b"LT E0")
usb.write(b"MT0 E0")
sleep(0.5)
usb.close()
