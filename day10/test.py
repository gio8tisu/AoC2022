import unittest

from main import Instruction, InstructionType, draw_pixel, execute_program_part_1


class TestExecuteProgram(unittest.TestCase):
    def test_execute_simple_example(self):
        program = [
            Instruction(InstructionType.NO_OP),
            Instruction(InstructionType.ADD_X, 3),
            Instruction(InstructionType.ADD_X, -5),
        ]
        x = execute_program_part_1(program, [1, 2, 3, 4, 5, 6])
        self.assertEqual(x, [1, 1, 1, 4, 4, -1])



class TestDrawPixel(unittest.TestCase):
    def test_draw_pixel_on_sprite_1(self):
        draw = draw_pixel(1, 1)
        self.assertEqual(draw, "#")

    def test_draw_pixel_on_sprite_0(self):
        draw = draw_pixel(0, 1)
        self.assertEqual(draw, "#")

    def test_draw_pixel_on_sprite_2(self):
        draw = draw_pixel(2, 2)
        self.assertEqual(draw, "#")

    def test_draw_pixel_off_sprite(self):
        draw = draw_pixel(2, 10)
        self.assertEqual(draw, ".")

    def test_draw_pixel_on_sprite_clock_40(self):
        draw = draw_pixel(39, 40)
        self.assertEqual(draw, "#\n")

    def test_draw_pixel_off_sprite_clock_41(self):
        draw = draw_pixel(1, 41)
        self.assertEqual(draw, "#")

    def test_draw_pixel_off_sprite_clock_40(self):
        draw = draw_pixel(20, 41)
        self.assertEqual(draw, ".")

    def test_draw_pixel_on_sprite_clock_80(self):
        draw = draw_pixel(39, 80)
        self.assertEqual(draw, "#\n")

    def test_draw_pixel_on_sprite_clock_81(self):
        draw = draw_pixel(1, 81)
        self.assertEqual(draw, "#")

    def test_draw_pixel_off_sprite_clock_81(self):
        draw = draw_pixel(20, 81)
        self.assertEqual(draw, ".")


if __name__ == "__main__":
    unittest.main()
