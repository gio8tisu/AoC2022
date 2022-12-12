import unittest

from main import Instruction, InstructionType, execute_program


class TestExecuteProgram(unittest.TestCase):
    def test_execute_simple_example(self):
        program = [
            Instruction(InstructionType.NO_OP),
            Instruction(InstructionType.ADD_X, 3),
            Instruction(InstructionType.ADD_X, -5),
        ]
        x = execute_program(program, [1, 2, 3, 4, 5, 6])
        self.assertEqual(x, [1, 1, 1, 4, 4, -1])



if __name__ == "__main__":
    unittest.main()
