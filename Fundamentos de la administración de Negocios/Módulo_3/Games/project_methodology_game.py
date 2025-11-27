import random

class ProjectMethodologyGame:
    def __init__(self):
        self.methodologies = {
            "Agile/Scrum": [
                "Tests products in the field and regularly implements improvements",
                "Receptive to change",
                "Teams share responsibility for managing their own work",
                "Time is organized into 'Sprints' with a set list of deliverables",
                "Planning happens in short iterations to deliver value quickly"
            ],
            "Waterfall": [
                "Change is often difficult to manage once the project begins",
                "Follows a mostly linear path through the project phases",
                "Project phases are clearly defined. They typically do not overlap or repeat",
                "Project manager is an active leader who prioritizes and assigns tasks to the team",
                "Project deliverables and plans are well-established and documented early on"
            ],
            "Lean Six Sigma": [
                "Uses the 5S quality tool",
                "Ideal for fixing complex or high-risk problems",
                "Aims to eliminate 8 areas of waste",
                "Primarily uses a Kanban scheduling system to manage production"
            ]
        }
        
        self.score = 0
        self.total_questions = 0
    
    def display_welcome(self):
        print("🎯 BIENVENIDO AL JUEGO: ADIVINA LA METODOLOGÍA")
        print("=" * 50)
        print("Tendrás que adivinar qué metodología de gestión")
        print("de proyectos se describe en cada característica.")
        print("Opciones: Agile/Scrum, Waterfall, Lean Six Sigma")
        print("=" * 50)
        print()
    
    def ask_question(self):
        methodology = random.choice(list(self.methodologies.keys()))
        characteristic = random.choice(self.methodologies[methodology])
        
        print(f"🔍 Característica: {characteristic}")
        print()
        
        options = list(self.methodologies.keys())
        random.shuffle(options)
        
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        print()
        
        while True:
            try:
                user_choice = int(input("Tu respuesta (1-3): "))
                if 1 <= user_choice <= 3:
                    break
                else:
                    print("❌ Por favor, ingresa un número entre 1 y 3")
            except ValueError:
                print("❌ Por favor, ingresa un número válido")
        
        user_answer = options[user_choice - 1]
        
        if user_answer == methodology:
            print("✅ ¡CORRECTO! Has adivinado bien.")
            self.score += 1
        else:
            print(f"❌ INCORRECTO. La respuesta era: {methodology}")
        
        self.total_questions += 1
        print(f"📊 Puntuación actual: {self.score}/{self.total_questions}")
        print("-" * 50)
        print()
    
    def play_game(self):
        self.display_welcome()
        
        while True:
            self.ask_question()
            
            continue_playing = input("¿Quieres continuar jugando? (s/n): ").lower()
            if continue_playing != 's':
                break
        
        self.display_final_score()
    
    def display_final_score(self):
        print("=" * 50)
        print("🎮 RESUMEN FINAL DEL JUEGO")
        print("=" * 50)
        print(f"📊 Puntuación final: {self.score}/{self.total_questions}")
        
        percentage = (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0
        
        if percentage >= 80:
            print("🏆 ¡Excelente! Eres un experto en metodologías de gestión de proyectos.")
        elif percentage >= 60:
            print("👍 ¡Muy bien! Tienes buen conocimiento de las metodologías.")
        elif percentage >= 40:
            print("💡 Bien, pero puedes mejorar. Sigue practicando.")
        else:
            print("📚 Sigue estudiando las metodologías de gestión de proyectos.")
        
        print("=" * 50)

if __name__ == "__main__":
    game = ProjectMethodologyGame()
    game.play_game()
