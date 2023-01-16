from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_init(TestCase):
    """Unittests for testing the `Rectangle` class """

    def test_bases(self):
        """test for id haves and havenot bases"""
        b1 = Rectangle()
        b2 = Rectangle(None)
        b3 = Rectangle()
        self.assertEqual(b1.id,  b2.id, b3.id - 2)

    def test_unique_id(self):
        """testing the uniqueness of id's"""
        self.assertEqual(12, Base(12).id)

class TestSetup(TestCase):
    """unittest for testing files & methods of `base` class"""

    def test_base(self):
        """test for saving file in class `Base` """
        Base.save_to_file(Square(89, 2, 3, 4))
        with open("Base.json", "r") as fp:
            self.assertTrue(len(fp.read()) == 39)

    def test_rectangle(self):
        """test for saving file in class `Rectangle` """
        Rectangle.save_to_file(Rectangle(89, 2, 3, 4, 5))
        with open("Rectangle.json", "r") as fp:
            self.assertTrue(len(fp.read()) == 53)

    def test_square(self):
        """test for saving file in class `Square` """
        Base.save_to_file(Square(89, 2, 3, 4))
        with open("Square.json", "r") as fp:
            self.assertTrue(len(fp.read()) == 39)
