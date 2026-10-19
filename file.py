
import random

def adivina_el_numero():
    """Juego donde el usuario debe adivinar un número del 1 al 100."""
    
    numero_secreto = random.randint(1, 100)
    max_intentos = 10
    intentos = 0
    
    print("=" * 40)
    print("   ¡Adivina el número entre 1 y 100!")
    print("=" * 40)
    print(f"  Tienes {max_intentos} intentos para ganar.")
    print("=" * 40)
    
    while intentos < max_intentos:
        restante = max_intentos - intentos
        print(f"\nIntentos restantes: {restante}")
        
        try:
            intento = int(input("Tu intento: "))
        except ValueError:
            print("   Por favor, ingresa un número válido.")
            continue
        
        # Validar rango
        if intento < 1 or intento > 100:
            print("   El número debe estar entre 1 y 100.")
            continue
        
        intentos += 1
        
        # Comprobar resultado
        if intento == numero_secreto:
            print("\n" + "=" * 40)
            print(f"   ¡FELICIDADES! ¡Lo lograste en {intentos} intento(s)!")
            print("=" * 40)
            return
        elif intento < numero_secreto:
            print("    El número secreto es MAYOR.")
        else:
            print("    El número secreto es MENOR.")
    
    # Se acabaron los intentos
    print("\n" + "=" * 40)
    print(f"   Se acabaron los intentos.")
    print(f"  El número secreto era: {numero_secreto}")
    print("=" * 40)

if __name__ == "__main__":
    adivina_el_numero()
    
    while input("\n¿Quieres jugar de nuevo? (s/n): ").lower() != "n":
        print("\n" + "" * 20)
        adivina_el_numero()
