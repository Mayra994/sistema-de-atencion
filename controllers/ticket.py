from collections import deque

class Ticket:
    def __init__(self, numero_ticket, nombre_cliente, tipo_problema, prioridad, tiempo_estimado):
        self.numero_ticket = numero_ticket
        self.nombre_cliente = nombre_cliente
        self.tipo_problema = tipo_problema
        self.prioridad = prioridad  # 'Prioritaria' o 'Normal'
        self.tiempo_estimado = tiempo_estimado  # en minutos

    def __str__(self):
        return (f"[Ticket #{self.numero_ticket}] Cliente: {self.nombre_cliente} | "
                f"Problema: {self.tipo_problema} | Prioridad: {self.prioridad} | "
                f"Tiempo Est.: {self.tiempo_estimado} min")


class SistemaAtencionTickets:
    def __init__(self):
        # Principio FIFO usando deque (cola)
        self.fila_prioritaria = deque()
        self.fila_normal = deque()
        self.contador_ticket = 1
        
        # Estadísticas
        self.total_atendidos_prioritaria = 0
        self.total_atendidos_normal = 0
        self.tiempo_total_atencion = 0

    
    def registrar_ticket(self, nombre_cliente, tipo_problema, prioridad, tiempo_estimado):
        
        prioridad_clean = prioridad.strip().capitalize()
        if prioridad_clean not in ['Prioritaria', 'Normal']:
            print("❌ Prioridad no válida. Debe ser 'Prioritaria' o 'Normal'.")
            return

        ticket = Ticket(
            numero_ticket=self.contador_ticket,
            nombre_cliente=nombre_cliente,
            tipo_problema=tipo_problema,
            prioridad=prioridad_clean,
            tiempo_estimado=int(tiempo_estimado)
        )
        self.contador_ticket += 1

        if prioridad_clean == 'Prioritaria':
            self.fila_prioritaria.append(ticket)
            print(f"✅ Ticket #{ticket.numero_ticket} registrado en la Fila Prioritaria.")
        else:
            self.fila_normal.append(ticket)
            print(f"✅ Ticket #{ticket.numero_ticket} registrado en la Fila Normal.")

    
    def atender_siguiente_ticket(self):
        ticket_a_atender = None

        if len(self.fila_prioritaria) > 0:
            ticket_a_atender = self.fila_prioritaria.popleft()
            self.total_atendidos_prioritaria += 1
        elif len(self.fila_normal) > 0:
            ticket_a_atender = self.fila_normal.popleft()
            self.total_atendidos_normal += 1
        else:
            print("\n⚠️ No hay tickets pendientes en ninguna fila.")
            return

        self.tiempo_total_atencion += ticket_a_atender.tiempo_estimado
        print(f"\n🔔 Atendiendo actual: {ticket_a_atender}")

    
    def consultar_siguiente_ticket(self):
        print("\n--- CONSULTAR SIGUIENTE TICKET ---")
        if len(self.fila_prioritaria) > 0:
            print(f"Próximo a atender (Fila Prioritaria): {self.fila_prioritaria[0]}")
        elif len(self.fila_normal) > 0:
            print(f"Próximo a atender (Fila Normal): {self.fila_normal[0]}")
        else:
            print("No hay tickets pendientes para atender.")

    
    def mostrar_filas(self):
        print("\n=== ESTADO ACTUAL DE LAS FILAS ===")
        print("--- Fila Prioritaria ---")
        if self.fila_prioritaria:
            for t in self.fila_prioritaria:
                print(f"  -> {t}")
        else:
            print("  (Fila vacía)")

        print("--- Fila Normal ---")
        if self.fila_normal:
            for t in self.fila_normal:
                print(f"  -> {t}")
        else:
            print("  (Fila vacía)")

    def mostrar_estadisticas(self):
        total_atendidos = self.total_atendidos_prioritaria + self.total_atendidos_normal
        promedio_tiempo = (self.tiempo_total_atencion / total_atendidos) if total_atendidos > 0 else 0
        pendientes = len(self.fila_prioritaria) + len(self.fila_normal)

        print("\n=== ESTADÍSTICAS DE ATENCIÓN ===")
        print(f"1. Total de tickets atendidos: {total_atendidos}")
        print(f"   - De Fila Prioritaria: {self.total_atendidos_prioritaria}")
        print(f"   - De Fila Normal: {self.total_atendidos_normal}")
        print(f"2. Tiempo estimado acumulado de resolución: {self.tiempo_total_atencion} minutos")
        print(f"3. Tiempo promedio de resolución por ticket atendido: {promedio_tiempo:.2f} minutos")
        print(f"4. Total de tickets pendientes en cola: {pendientes}")



def menu():
    sistema = SistemaAtencionTickets()

   

    while True:
        print("\n" + "="*40)
        print(" SISTEMA DE ATENCIÓN DE TICKETS DE SOPORTE ")
        print("="*40)
        print("1) Registrar ticket")
        print("2) Atender el siguiente ticket")
        print("3) Consultar siguiente ticket")
        print("4) Mostrar las filas")
        print("5) Obtener estadísticas")
        print("6) Salir")
        
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR NUEVO TICKET ---")
            nombre = input("Nombre del cliente: ")
            problema = input("Breve descripción del problema: ")
            prioridad = input("Prioridad (Normal / Prioritaria): ")
            try:
                tiempo = int(input("Tiempo estimado de solución (minutos): "))
                sistema.registrar_ticket(nombre, problema, prioridad, tiempo)
            except ValueError:
                print("❌ Error: El tiempo estimado debe ser un número entero.")

        elif opcion == "2":
            sistema.atender_siguiente_ticket()

        elif opcion == "3":
            sistema.consultar_siguiente_ticket()

        elif opcion == "4":
            sistema.mostrar_filas()

        elif opcion == "5":
            sistema.mostrar_estadisticas()

        elif opcion == "6":
            print("\n¡Gracias por utilizar el sistema de soporte!")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()