from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre_completo: str):
        self._nombre_completo = nombre_completo.strip()

    @property
    def nombre_completo(self):
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, nuevo_nombre):
        self._nombre_completo = nuevo_nombre.strip()

    @abstractmethod
    def mostrar_informacion(self):
        pass


class ContactoApoderado:
    def __init__(self, telefono="", correo=""):
        self._telefono = telefono.strip()
        self._correo = correo.strip()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        self._correo = valor.strip()

    def mostrar(self):
        telefono = self._telefono if self._telefono else "No registrado"
        correo = self._correo if self._correo else "No registrado"
        return f"Teléfono: {telefono} | Correo: {correo}"


class Estudiante(Persona):
    def __init__(
        self,
        nombre_completo: str,
        curso: str,
        notas: list,
        nombre_apoderado: str,
        contacto_apoderado: ContactoApoderado,
        faltas: int,
        anotaciones_positivas: int,
        anotaciones_negativas: int
    ):
        super().__init__(nombre_completo)
        self._curso = curso.strip()
        self._notas = notas
        self._nombre_apoderado = nombre_apoderado.strip()
        self._contacto_apoderado = contacto_apoderado
        self._faltas = faltas
        self._anotaciones_positivas = anotaciones_positivas
        self._anotaciones_negativas = anotaciones_negativas

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, valor):
        self._curso = valor.strip()

    @property
    def notas(self):
        return self._notas

    @property
    def nombre_apoderado(self):
        return self._nombre_apoderado

    @property
    def contacto_apoderado(self):
        return self._contacto_apoderado

    @property
    def faltas(self):
        return self._faltas

    @property
    def anotaciones_positivas(self):
        return self._anotaciones_positivas

    @property
    def anotaciones_negativas(self):
        return self._anotaciones_negativas

    def promedio_notas(self):
        if len(self._notas) == 0:
            return 0.0
        return sum(self._notas) / len(self._notas)

    def evaluar_riesgo(self):
        """
        Criterios sugeridos:
        - Riesgo académico: promedio menor a 4.0
        - Riesgo por faltas/anotaciones negativas:
          faltas >= 8 o anotaciones negativas >= 3
        """
        riesgo_academico = self.promedio_notas() < 4.0
        riesgo_convivencia = self._faltas >= 8 or self._anotaciones_negativas >= 3

        if riesgo_academico and riesgo_convivencia:
            return "Riesgo académico y riesgo por faltas/anotaciones negativas."
        elif riesgo_academico:
            return "Riesgo académico."
        elif riesgo_convivencia:
            return "Riesgo por faltas/anotaciones negativas."
        else:
            return "No presenta riesgo."

    def mostrar_informacion(self):
        notas_formateadas = ", ".join([str(nota) for nota in self._notas]) if self._notas else "Sin notas"
        promedio = f"{self.promedio_notas():.2f}"

        info = (
            f"Nombre completo: {self.nombre_completo}\n"
            f"Curso: {self._curso}\n"
            f"Notas: {notas_formateadas}\n"
            f"Promedio: {promedio}\n"
            f"Nombre apoderado: {self._nombre_apoderado}\n"
            f"Contacto apoderado: {self._contacto_apoderado.mostrar()}\n"
            f"Faltas: {self._faltas}\n"
            f"Anotaciones positivas: {self._anotaciones_positivas}\n"
            f"Anotaciones negativas: {self._anotaciones_negativas}\n"
            f"Evaluación de riesgo: {self.evaluar_riesgo()}"
        )
        return info


class RegistroEscolar:
    def __init__(self):
        self._estudiantes = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self._estudiantes.append(estudiante)

    def buscar_estudiante(self, nombre_completo: str, curso: str):
        nombre_completo = nombre_completo.strip().lower()
        curso = curso.strip().lower()

        for estudiante in self._estudiantes:
            if (
                estudiante.nombre_completo.lower() == nombre_completo
                and estudiante.curso.lower() == curso
            ):
                return estudiante
        return None

    def listar_estudiantes(self):
        return self._estudiantes


def pedir_entero_no_negativo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Debe ser un número igual o mayor que 0.")
                continue
            return valor
        except ValueError:
            print("Ingrese un número entero válido.")


def pedir_notas():
    while True:
        texto = input("Ingrese las notas separadas por coma (ej: 4.5,5.0,6.2): ").strip()
        if texto == "":
            return []

        try:
            notas = [float(nota.strip()) for nota in texto.split(",") if nota.strip() != ""]
            if len(notas) == 0:
                print("Debe ingresar al menos una nota.")
                continue
            return notas
        except ValueError:
            print("Formato inválido. Use números separados por coma.")


def crear_contacto():
    print("\nTipo de contacto del apoderado:")
    print("1. Teléfono")
    print("2. Correo")
    print("3. Ambos")

    while True:
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            telefono = input("Ingrese teléfono: ")
            return ContactoApoderado(telefono=telefono, correo="")
        elif opcion == "2":
            correo = input("Ingrese correo: ")
            return ContactoApoderado(telefono="", correo=correo)
        elif opcion == "3":
            telefono = input("Ingrese teléfono: ")
            correo = input("Ingrese correo: ")
            return ContactoApoderado(telefono=telefono, correo=correo)
        else:
            print("Opción inválida. Intente nuevamente.")


def registrar_estudiante(registro: RegistroEscolar):
    print("\n--- Registro de estudiante ---")
    nombre = input("Nombre completo: ")
    curso = input("Curso: ")
    notas = pedir_notas()
    nombre_apoderado = input("Nombre del apoderado: ")
    contacto = crear_contacto()
    faltas = pedir_entero_no_negativo("Número de faltas: ")
    positivas = pedir_entero_no_negativo("Anotaciones positivas: ")
    negativas = pedir_entero_no_negativo("Anotaciones negativas: ")

    estudiante = Estudiante(
        nombre_completo=nombre,
        curso=curso,
        notas=notas,
        nombre_apoderado=nombre_apoderado,
        contacto_apoderado=contacto,
        faltas=faltas,
        anotaciones_positivas=positivas,
        anotaciones_negativas=negativas
    )

    registro.registrar_estudiante(estudiante)
    print("\nEstudiante registrado correctamente.")


def buscar_estudiante(registro: RegistroEscolar):
    print("\n--- Búsqueda de estudiante ---")
    nombre = input("Ingrese nombre completo: ")
    curso = input("Ingrese curso: ")

    estudiante = registro.buscar_estudiante(nombre, curso)

    if estudiante:
        print("\nEstudiante encontrado:\n")
        print(estudiante.mostrar_informacion())
    else:
        print("\nNo se encontró ningún estudiante con ese nombre y curso.")


def listar_estudiantes(registro: RegistroEscolar):
    print("\n--- Lista de estudiantes ---")
    estudiantes = registro.listar_estudiantes()

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for i, estudiante in enumerate(estudiantes, start=1):
        print(f"\nEstudiante {i}")
        print("-" * 30)
        print(estudiante.mostrar_informacion())


def evaluar_riesgo_estudiante(registro: RegistroEscolar):
    print("\n--- Evaluación de riesgo ---")
    nombre = input("Ingrese nombre completo: ")
    curso = input("Ingrese curso: ")

    estudiante = registro.buscar_estudiante(nombre, curso)

    if estudiante:
        print("\nResultado de riesgo:")
        print(estudiante.evaluar_riesgo())
    else:
        print("\nNo se encontró ningún estudiante con ese nombre y curso.")


def menu():
    registro = RegistroEscolar()

    while True:
        print("\n==============================")
        print("   SISTEMA DE REGISTRO ESCOLAR")
        print("==============================")
        print("1. Registrar estudiante")
        print("2. Buscar estudiante")
        print("3. Listar estudiantes")
        print("4. Evaluar riesgo de un estudiante")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_estudiante(registro)
        elif opcion == "2":
            buscar_estudiante(registro)
        elif opcion == "3":
            listar_estudiantes(registro)
        elif opcion == "4":
            evaluar_riesgo_estudiante(registro)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente otra vez.")


if __name__ == "__main__":
    menu()
