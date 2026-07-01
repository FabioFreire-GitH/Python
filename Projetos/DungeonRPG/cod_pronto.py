import time
import sys

def efeito_pergaminho(texto, atraso=0.05):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    print() # Pula uma linha no final

# Exemplo de uso:
mensagem = "Ah, aventureiro... Você finalmente chegou! Leia com atenção..."
efeito_pergaminho(mensagem)


import time
import sys
import random

# Função do efeito de pergaminho
def pergaminho(texto, atraso=0.03):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    print()
    time.sleep(0.5) # Pequena pausa dramática após a frase

# Configurações iniciais dos personagens
jogador_hp = 100
npc_hp = 100
npc_nome = "Cavaleiro Negro"

pergaminho(f"⚔️ O duelo começou! Você enfrenta o temível {npc_nome}! ⚔️\n")

# Loop principal do combate
while jogador_hp > 0 and npc_hp > 0:
    # --- TURNO DO JOGADOR ---
    pergaminho("\n👉 Seu turno! Escolha sua ação:")
    print("1. Ataque Espada (Dano: 10-25)")
    print("2. Curar (Recupera: 15-30 HP)")
    
    escolha = input("Digite 1 ou 2: ")
    print("-" * 40)

    if escolha == "1":
        dano_jogador = random.randint(10, 25)
        npc_hp -= dano_jogador
        pergaminho(f"💥 Você avança e golpeia! Causa {dano_jogador} de dano no {npc_nome}.")
    elif escolha == "2":
        cura = random.randint(15, 30)
        jogador_hp += cura
        pergaminho(f"🧪 Você bebe uma poção! Recupera {cura} de vida.")
    else:
        pergaminho("❌ Você hesitou e perdeu a chance de atacar!")

    # Verifica se o NPC morreu
    if npc_hp <= 0:
        break

    # --- TURNO DO NPC ---
    pergaminho(f"\n⚡ Turno do {npc_nome}...")
    dano_npc = random.randint(8, 22)
    jogador_hp -= dano_npc
    pergaminho(f"⚔️ O {npc_nome} contra-ataca e te causa {dano_npc} de dano!")

    # Exibe o status atual da batalha
    print("=" * 40)
    pergaminho(f"📊 STATUS ATUAL | Seu HP: {max(0, jogador_hp)} | HP do {npc_nome}: {max(0, npc_hp)}")
    print("=" * 40)

# --- FIM DO COMBATE ---
print("\n" + "#" * 40)
if jogador_hp > 0:
    pergaminho(f"🏆 VITÓRIA! Você derrotou o {npc_nome} e sobreviveu ao duelo!")
else:
    pergaminho(f"💀 DERROTA... O {npc_nome} foi implacável. Você caiu em combate.")
print("#" * 40)
