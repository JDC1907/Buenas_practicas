class Student:
    def __init__(self, id, name):
        if not id or not name:
            raise ValueError("ID and name cannot be empty.")
        self.id = id
        self.name = name
        self.gradez = []
        self.isPassed = False
        self.honor = False
        self.letter = None  # Inicializar variable para reporte

    def addGrade(self, g):
        # Validar tipo numérico y rango 0-100
        if not isinstance(g, (int, float)):
            print(f"Warning: Grade '{g}' is invalid and will be skipped.")
            return
        if g < 0 or g > 100:
            print(
                f"Warning: Grade '{g}' is out of valid range (0-100). Skipped."
            )
            return
        self.gradez.append(g)

    def calcAverage(self):
        if not self.gradez:
            return 0
        total = sum(self.gradez)
        avg = total / len(self.gradez)
        return avg

    def getLetterGrade(self):
        avg = self.calcAverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def checkHonor(self):
        avg = self.calcAverage()
        self.honor = avg >= 90  # Booleano según promedio >=90

    def checkPassFail(self):
        avg = self.calcAverage()
        self.isPassed = avg >= 60  # Booleano según promedio >=60

    def deleteGrade(self, value_or_index):
        """
        Permite eliminar una calificación por valor o índice:
        - Si es int y válido, se elimina por índice.
        - Si es float/int, se elimina por valor.
        - Maneja errores si no existe o índice fuera de rango.
        """
        # Intentamos tratar como índice
        if isinstance(value_or_index, int):
            try:
                del self.gradez[value_or_index]
                print(f"Deleted grade at index {value_or_index}.")
                return
            except IndexError:
                print(f"Error: Index {value_or_index} out of range.")
                return
        # Intentamos eliminar por valor
        if isinstance(value_or_index, (int, float)):
            if value_or_index in self.gradez:
                self.gradez.remove(value_or_index)
                print(f"Deleted grade with value {value_or_index}.")
            else:
                print(f"Error: Grade value {value_or_index} not found.")
        else:
            print(
                "Error: Invalid argument for deleteGrade. Must be int (index) "
                "or float/int (value)."
            )

    def report(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.gradez)}")
        avg = self.calcAverage()
        print(f"Average Grade: {avg:.2f}")
        self.letter = self.getLetterGrade()
        print(f"Final Grade (Letter): {self.letter}")
        print(f"Passed: {'Yes' if self.isPassed else 'No'}")
        print(f"Honor Student: {'Yes' if self.honor else 'No'}")


def startrun():
    try:
        a = Student("x", "John Doe")
    except ValueError as e:
        print(e)
        return

    a.addGrade(100)
    a.addGrade("Fifty")  # Mensaje de advertencia, no agregado
    a.addGrade(85)
    a.addGrade(75)
    a.addGrade(55)

    a.checkHonor()
    a.checkPassFail()

    a.deleteGrade(5)       # Intento borrar índice no válido, muestra error
    a.deleteGrade(75)      # Borra calificación por valor
    a.deleteGrade(100)     # Borra calificación por valor
    a.deleteGrade("Test")  # Argumento inválido

    a.report()


startrun()
