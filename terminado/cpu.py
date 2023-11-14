# Este es el ejercicio terminado en Python

# ('ADD', 'Ra', 'Rb', 'Rc')
# ('SUB', 'Ra', 'Rb', 'Rc')
# ('MUL', 'Ra', 'Rb', 'Rc')
# ('DIV', 'Ra', 'Rb', 'Rc')
# ('INC', 'Ra')
# ('DEC', 'Ra')
# ('CMP', 'op', 'Ra', 'Rb', 'Rc')  # op = {<, >, <=, >=, ==, !=}
# ('CONST', value, 'Ra')
# ('LOAD', 'Rs', 'Rd', offset)  # Simulando nuestra RAM
# ('STORE', 'Rs', 'Rd', offset)  # Simulando nuestra RAM
# ('JMP', 'Rd', offset)  # Mueve el IP a la dirección de memoria
# ('HALT')


class CPU:
    def run(self, program):
        self.registers = {
            "Ra": 0,
            "Rb": 0,
            "Rc": 0,
            "Rd": 0,
            "Re": 0,
            "Rf": 0,
            "Rg": 0,
            "Rh": 0,
        }  # 8 registros

        # Para Pythonistas:
        # self.registers = {f"R{a}": 0 for a in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]}
        self.memory = [0] * 1024  # 1024 bytes

        # Instruction Pointer, en qué instrucción vamos
        self.registers["IP"] = 0

        # Stack Pointer, en qué posición de la memoria comenzamos a guardar cosas
        self.registers["SP"] = 0

        while True:
            # Obtener la instrucción actual
            instruction = program[self.registers["IP"]]
            print(instruction)

            # Incrementar el IP
            self.registers["IP"] += 1

            # Obtener el nombre de la instrucción
            name = instruction[0]

            # Ejecutar la instrucción
            if name == "ADD":
                self.ADD(instruction[1], instruction[2], instruction[3])
            elif name == "SUB":
                self.SUB(instruction[1], instruction[2], instruction[3])
            elif name == "MUL":
                self.MUL(instruction[1], instruction[2], instruction[3])
            elif name == "DIV":
                self.DIV(instruction[1], instruction[2], instruction[3])
            elif name == "INC":
                self.INC(instruction[1])
            elif name == "DEC":
                self.DEC(instruction[1])
            elif name == "CMP":
                self.CMP(instruction[1], instruction[2], instruction[3], instruction[4])
            elif name == "CONST":
                self.CONST(instruction[1], instruction[2])
            elif name == "LOAD":
                self.LOAD(instruction[1], instruction[2], instruction[3])
            elif name == "STORE":
                self.STORE(instruction[1], instruction[2], instruction[3])
            elif name == "JMP":
                self.JMP(instruction[1], instruction[2])
            elif name == "HALT":
                self.HALT()
                break
            else:
                raise Exception(f"Instrucción no soportada {name}")

            # Para Pythonistas:
            # getattr(self, name)(*args)

        return self.registers

        # Leer las instrucciones hasta el final e imprimir el resultado

    def ADD(self, arg1, arg2, result):  # 'Ra', 'Rb', 'Rc'
        self.registers[result] = self.registers[arg1] + self.registers[arg2]

    def SUB(self, arg1, arg2, result):
        self.registers[result] = self.registers[arg1] - self.registers[arg2]

    def MUL(self, arg1, arg2, result):
        self.registers[result] = self.registers[arg1] * self.registers[arg2]

    def DIV(self, arg1, arg2, result):
        self.registers[result] = self.registers[arg1] / self.registers[arg2]

    def INC(self, arg1):
        self.registers[arg1] += 1

    def DEC(self, arg1):
        self.registers[arg1] -= 1

    def CMP(self, op, arg1, arg2, result):
        if op == "<":
            self.registers[result] = self.registers[arg1] < self.registers[arg2]
        elif op == ">":
            self.registers[result] = self.registers[arg1] > self.registers[arg2]
        elif op == "<=":
            self.registers[result] = self.registers[arg1] <= self.registers[arg2]
        elif op == ">=":
            self.registers[result] = self.registers[arg1] >= self.registers[arg2]
        elif op == "==":
            self.registers[result] = self.registers[arg1] == self.registers[arg2]
        elif op == "!=":
            self.registers[result] = self.registers[arg1] != self.registers[arg2]
        else:
            raise Exception("Operador no soportado")

    def CONST(self, value, arg1):
        self.registers[arg1] = value

    def LOAD(self, rs, rd, offset):
        self.registers[rd] = self.memory[rs + offset]

    def STORE(self, rs, rd, offset):
        self.memory[rs + offset] = self.registers[rd]

    def JMP(self, arg1, offset):
        self.registers["IP"] = self.registers[arg1] + offset

    def HALT(self):
        print("El programa ha terminado")


machine = CPU()
code = [
    ("CONST", 10, "Ra"),
    ("CONST", 20, "Rb"),
    ("ADD", "Ra", "Rb", "Rc"),
    ("HALT",),
]

print(machine.run(code))
