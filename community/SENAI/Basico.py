#!/usr/bin/python3
"""
Solis Robot - SoBot
Challenge 002 - SOBOT FORK LIFT (Código Corrigido e Completo)

Empresa: Solis Tecnologia
"""

from time import sleep
import serial

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO DA PORTA SERIAL
# ---------------------------------------------------------------------------
# Define a porta serial com timeout adequado para a leitura dos sensores
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1, dsrdtr=False)
usb.flush()  # Limpa o buffer de dados serial

def send_cmd(command_str):
    """Envia um comando formatado para a placa principal do SoBot"""
    usb.write(f"{command_str}\n".encode('utf-8'))
    sleep(0.05)

def set_led(r, g, b):
    """Ajusta a cor da fita LED RGB do SoBot"""
    send_cmd(f"LT E1 RD{r} GR{g} BL{b}")

def set_lift(angle):
    """
    Aciona o servo/motor do Módulo Garfo Elevador (Porta SV1)
    angle: 20 (Garfo Baixo / Pousado) | 110 (Garfo Alto / Suspenso)
    """
    send_cmd(f"SV1 P{angle}")
    sleep(1.5)  # Aguarda a conclusão do movimento mecânico

def enable_motors(enable=True):
    """Habilita (E1) ou desabilita (E0) os motores de tração"""
    status = "E1" if enable else "E0"
    send_cmd(f"MT0 {status}")

def drive_direct(left_speed, right_speed):
    """Define a velocidade contínua das rodas esquerda e direita"""
    send_cmd(f"MT0 V1 L{left_speed} R{right_speed}")

def stop_motors():
    """Para a movimentação do robô imediatamente"""
    drive_direct(0, 0)
    sleep(0.1)

def read_sensors():
    """
    Requisita e lê o estado dos sensores IV da placa seguidora de linha.
    Retorna: (sensor_esquerdo, sensor_direito, sensor_marcador_lateral)
    1 = Fita Preta Detetada | 0 = Superfície Clara
    """
    send_cmd("SE")
    line = usb.readline().decode('utf-8', errors='ignore').strip()
    
    s_left, s_right, s_marker = 0, 0, 0
    if "SE" in line or ":" in line:
        parts = line.split()
        for part in parts:
            if "S1:" in part:
                s_left = int(part.split(":")[1])
            elif "S2:" in part:
                s_right = int(part.split(":")[1])
            elif "S3:" in part:
                s_marker = int(part.split(":")[1])
    return s_left, s_right, s_marker

def follow_line_step(base_speed=100):
    """
    Executa o ajuste de trajetória na linha preta principal.
    Retorna True quando o sensor lateral (S3) lê o marcador de fita.
    """
    s_left, s_right, s_marker = read_sensors()
    
    # Correção de direção baseada nos sensores frontais
    if s_left == 1 and s_right == 0:
        drive_direct(40, base_speed)         # Ajusta para a esquerda
    elif s_left == 0 and s_right == 1:
        drive_direct(base_speed, 40)         # Ajusta para a direita
    else:
        drive_direct(base_speed, base_speed) # Avança em frente
        
    return (s_marker == 1)

# ---------------------------------------------------------------------------
# FLUXO DE EXECUÇÃO DA MISSÃO COMPLETA
# ---------------------------------------------------------------------------
def main():
    print("A iniciar o Desafio 002 - SOBOT FORK LIFT...")
    
    try:
        # 1. INICIALIZAÇÃO DO SISTEMA
        enable_motors(True)
        set_led(50, 0, 0)    # LED Vermelho: Preparação
        set_lift(20)         # Assegura o garfo na posição inferior
        sleep(1.0)

        # 2. RECOLHA NO PONTO INICIAL (Collect Point)
        set_led(50, 25, 0)   # LED Laranja: A recolher a carga
        # Avança 150 mm para introduzir o garfo sob o palete
        send_cmd("MT0 E1 D150 AT1500 DT1500 V10")
        sleep(2.5)
        
        # Eleva o garfo para suspender a carga[cite: 1, 2]
        set_lift(110)
        sleep(1.0)

        # 3. NAVEGAÇÃO DE IDA (Seguir Linha até ao Deposit Point)[cite: 1, 2]
        set_led(0, 50, 0)    # LED Verde: Em transporte
        print("A seguir a linha até ao Ponto de Depósito...")
        
        while True:
            marker_reached = follow_line_step(base_speed=110)
            if marker_reached:
                print("Marcador do Ponto de Depósito detetado!")
                stop_motors()
                break
            sleep(0.03)

        # 4. DEPÓSITO DA CARGA (Deposit Point)[cite: 1, 2]
        set_led(50, 50, 0)   # LED Amarelo: Descarga
        set_lift(20)         # Baixa o garfo para pousar o palete no chão[cite: 1, 2]
        sleep(1.0)
        
        # Recua 150 mm para retirar o garfo de baixo do palete[cite: 1, 2]
        send_cmd("MT0 E1 D-150 AT1500 DT1500 V10")
        sleep(2.5)
        
        # Executa rotação de 180° para alinhar com o sentido de regresso[cite: 1, 2]
        send_cmd("MT0 E1 D180 R AT3000 DT3000 V10")
        sleep(3.5)

        # 5. PERCURSO DE REGRESSO (Seguir Linha até ao Start Point)[cite: 1, 2]
        set_led(0, 50, 50)   # LED Ciano: A regressar
        print("A regressar à linha de partida...")
        
        while True:
            marker_reached = follow_line_step(base_speed=110)
            if marker_reached:
                print("Marcador de Partida detetado! Missão Concluída.")
                stop_motors()
                break
            sleep(0.03)

        # 6. FINALIZAÇÃO
        set_led(0, 0, 0)      # Desliga os LEDs
        enable_motors(False)  # Desativa a alimentação dos motores
        print("Desafio 002 concluído com sucesso!")

    except KeyboardInterrupt:
        print("\nMissão interrompida pelo utilizador.")
        stop_motors()
        enable_motors(False)
        usb.close()

if __name__ == "__main__":
    main()
