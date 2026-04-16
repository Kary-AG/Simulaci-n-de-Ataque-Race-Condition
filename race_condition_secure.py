import threading
import time

balance = 100.0
# Creamos un candado (mutex) para proteger el recurso compartido
balance_lock = threading.Lock()

def secure_withdraw(amount, user_name):
    """
    Función SEGURA contra Race Conditions.
    Utiliza un candado (mutex) para hacer la operación atómica.
    """
    global balance
    print(f"---> {user_name} quiere retirar ${amount}.")
    
    # La sección crítica está protegida por el candado
    with balance_lock:
        # Solo UN hilo puede ejecutar esto a la vez
        print(f"    {user_name} adquirió el candado. Verificando saldo (${balance})...")
        if balance >= amount:
            time.sleep(0.01)  # La pausa ya NO es un problema
            balance -= amount
            print(f"    {user_name} retiró ${amount}. Nuevo saldo: ${balance}")
        else:
            print(f"    {user_name} NO pudo retirar. Saldo insuficiente (${balance})")
    # El candado se libera automáticamente al salir del bloque 'with'

if __name__ == "__main__":
    print("\n=== SIMULACIÓN EN ENTORNO SEGURO (CON LOCKS) ===")
    print(f"Saldo inicial: ${balance}")
    print("Dos usuarios intentan retirar $100 CADA UNO.\n")
    
    amount = 100.0
    t1 = threading.Thread(target=secure_withdraw, args=(amount, "Usuario 1"))
    t2 = threading.Thread(target=secure_withdraw, args=(amount, "Usuario 2"))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(f"\n--- RESULTADO FINAL SEGURO ---")
    print(f"Saldo final: ${balance}")
    print("✅ ATAQUE FRUSTRADO: Solo un usuario pudo retirar el dinero.")