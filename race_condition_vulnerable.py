import threading
import time

# Recurso compartido
balance = 100.0

def vulnerable_withdraw(amount, user_name):
    """
    Función VULNERABLE a Race Condition.
    No utiliza ningún mecanismo de bloqueo.
    """
    global balance
    print(f"---> {user_name} está verificando el saldo...")
    
    # PUNTO CRÍTICO VULNERABLE
    if balance >= amount:
        # Pequeña pausa para forzar la condición de carrera
        time.sleep(0.01)
        print(f"{user_name} puede retirar. Procesando...")
        balance -= amount
        print(f"{user_name} retiró ${amount}. Saldo restante: ${balance}")
    else:
        print(f"{user_name} NO pudo retirar. Saldo insuficiente (${balance})")

if __name__ == "__main__":
    print("=== SIMULACIÓN DE ATAQUE: CONDICIÓN DE CARRERA ===")
    print(f"Saldo inicial: ${balance}")
    print("Dos atacantes intentan retirar $100 CADA UNO al mismo tiempo.\n")
    
    amount = 100.0
    t1 = threading.Thread(target=vulnerable_withdraw, args=(amount, "Atacante 1"))
    t2 = threading.Thread(target=vulnerable_withdraw, args=(amount, "Atacante 2"))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(f"\n--- RESULTADO FINAL ---")
    print(f"Saldo final después del ataque: ${balance}")
    print("💥 ATAQUE EXITOSO: ¡Se retiraron $200 teniendo solo $100!")