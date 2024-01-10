# Completa el siguiente código para simular un CPU que trabaje con registros

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
    # implementa un CPU muy siempre que ejecute las instrucciones de arriba

    def run(self, program):
        self.registers = {"Ra": 0, "Rb": 0, "Rc": 0, "Rd": 0}  # 8 registros
        self.memory = [0] * 1024
        self.registers["IP"] = 0
        self.registers["SP"] = 0
        # Leer las instruccioes hasta el final e imprimir el resultado

    def ADD(self, arg1, arg2, result):  # 'Ra', 'Rb', 'Rc'
        self.registers[result] = self.registers[arg1] + self.registers[arg2]

    def JMP(self, arg1, offset):
        self.registers["IP"] = self.registers[arg1] + offset


machine = CPU()
code = [("CONST", 10, "Ra"), ("CONST", 20, "Rb"), ("ADD", "Ra", "Rb", "Rc"), ("HALT")]
# code = [
#     ('CONST', 'Ra', 11),
#     ('CONST', 'Rb', 1),
#     ('CONST', 'Rc', 0),
#     ('CONST', 'Rd', 4), # Dirección en donde empieza el bucle
#     ('CMP', '<=', 'Rb', 'Ra', 'Rd'),
#     ('ADD', 'Rb', 'Rc', 'Rc'),
#     ('JMP', 'Rd', 0),
#     ('HALT')
# ]
machine.run(code)
