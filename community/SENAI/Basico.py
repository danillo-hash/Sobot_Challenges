import math

class NavegacaoVirtualSemSensores:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0 # Orientação inicial (0 radianos / apontando para o eixo X)

    def mover_distancia_por_tempo(self, velocidade_linear, tempo):
        distancia = velocidade_linear * tempo
        self.x += distancia * math.cos(self.theta)
        self.y += distancia * math.sin(self.theta)
        print(f"[Avanço] Distância: {distancia:.2f}m | Posição Virtual -> X: {self.x:.2f}, Y: {self.y:.2f}")

    def girar_por_tempo(self, velocidade_angular, tempo):
        delta_angulo = velocidade_angular * tempo
        self.theta += delta_angulo
        angulo_graus = math.degrees(self.theta) % 360
        print(f"[Giro] Rotação realizada | Orientação Atual: {angulo_graus:.2f}°")

    def andar_um_metro(self, velocidade_linear=1.0):
        # Tempo necessário para percorrer 1 metro
        tempo = 1.0 / velocidade_linear
        self.mover_distancia_por_tempo(velocidade_linear, tempo)

    def girar_90_graus(self, velocidade_angular=math.radians(90)):
        # Se a velocidade angular for 90°/s (pi/2 rad/s), leva 1 segundo para girar 90°
        tempo = (math.pi / 2) / velocidade_angular
        self.girar_por_tempo(velocidade_angular, tempo)

    def fazer_trajeto_quadrado(self):
        """
        Executa o desafio do quadrado perfeito de 1 metro usando apenas controle temporal.
        """
        print("=== INICIANDO O DESAFIO: TRAJETO EM QUADRADO ===")
        
        for i in range(1, 5):
            print(f"\n--- Passo {i}: Andando 1 metro ---")
            self.andar_um_metro(velocidade_linear=1.0)
            
            print(f"--- Passo {i}: Girando 90 graus ---")
            self.girar_90_graus()
            
        print("\n=== DESAFIO CONCLUÍDO! (Retorno estimado à origem) ===")

# ==========================================
# Executando o Desafio
# ==========================================
robo = NavegacaoVirtualSemSensores()
robo.fazer_trajeto_quadrado()
