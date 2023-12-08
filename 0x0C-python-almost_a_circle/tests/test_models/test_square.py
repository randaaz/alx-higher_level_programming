#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class CustomSquareTests(unittest.TestCase):
    '''Tests the Square class.'''

    def setUp(self):
        '''Tests setUp'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Tests setUp'''
        pass

    def test_c(self):
        '''Tests type of class.'''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_inher(self):
        '''Tests inherits'''
        self.assertTrue(issubclass(Square, Base))

    def test_no_args(self):
        '''Tests constructor with no arguments'''
        with self.assertRaises(TypeError) as e:
            h = Square()
        c = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), c)

    def test_C_many_args(self):
        '''Tests constructor with many arguments'''
        with self.assertRaises(TypeError) as e:
            h = Square(2, 4, 5, 2, 3)
        c = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(e.exception), c)

    def test_inst(self):
        '''instantiation.'''
        h = Square(12)
        self.assertEqual(str(type(h)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(h, Base))
        n = {'_Rectangle__height': 12, '_Rectangle__width': 12,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(h.__dict__, n)

        with self.assertRaises(TypeError) as e:
            h = Square("9")
        m = "width must be an integer"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(TypeError) as e:
            h = Square(9, "4")
        m = "x must be an integer"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(TypeError) as e:
            h = Square(9, 4, "5")
        m = "y must be an integer"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(ValueError) as e:
            h = Square(-9)
        m = "width must be > 0"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(ValueError) as e:
            h = Square(9, -4)
        m = "x must be >= 0"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(ValueError) as e:
            h = Square(9, 4, -5)
        m = "y must be >= 0"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(ValueError) as e:
            h = Square(0)
        m = "width must be > 0"
        self.assertEqual(str(e.exception), m)

    def test_inst_po(self):
        '''Tests with positional'''
        h = Square(3, 12, 13)
        n = {'_Rectangle__height': 3, '_Rectangle__width': 3,
             '_Rectangle__x': 12, '_Rectangle__y': 13, 'id': 1}
        self.assertEqual(h.__dict__, n)

        h = Square(3, 12, 13, 40)
        n = {'_Rectangle__height': 3, '_Rectangle__width': 3,
             '_Rectangle__x': 12, '_Rectangle__y': 13, 'id': 40}
        self.assertEqual(h.__dict__, n)

    def test_keyword(self):
        '''Tests with keywords'''
        h = Square(900, id=241, y=11, x=901)
        n = {'_Rectangle__height': 900, '_Rectangle__width': 900,
             '_Rectangle__x': 901, '_Rectangle__y': 11, 'id': 241}
        self.assertEqual(h.__dict__, n)

    def test__inher(self):
        '''Tests inherited'''
        Base._Base__nb_objects = 16
        h = Square(2)
        self.assertEqual(h.id, 17)

    def test_proper(self):
        '''Tests getters/setters.'''
        h = Square(5, 9)
        h.size = 16
        h.x = 902
        h.y = 903
        n = {'_Rectangle__height': 16, '_Rectangle__width': 16,
             '_Rectangle__x': 902, '_Rectangle__y': 903, 'id': 1}
        self.assertEqual(h.__dict__, n)
        self.assertEqual(h.size, 16)
        self.assertEqual(h.x, 902)
        self.assertEqual(h.y, 903)

    def _types(self):
        '''Tests invalid type.'''
        ta = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
              [4], {5}, {6: 7}, None)
        return ta

    def test_type_v(self):
        '''Tests valid type'''
        h = Square(1)
        attrs = ["x", "y"]
        for attr in attrs:
            c = "{} must be an integer".format(attr)
            for it in self._types():
                with self.assertRaises(TypeError) as e:
                    setattr(h, attr, it)
                self.assertEqual(str(e.exception), c)
        c = "width must be an integer"
        for it in self._types():
            with self.assertRaises(TypeError) as e:
                setattr(h, "width", it)
            self.assertEqual(str(e.exception), c)

    def test_val_neg_t(self):
        '''Tests more validation.'''
        h = Square(9, 4)
        attrs = ["size"]
        for attr in attrs:
            c = "width must be > 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(h, attr, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), c)

    def test_val_value_neg_e(self):
        '''Tests more validation.'''
        h = Square(9, 4)
        attrs = ["x", "y"]
        for attr in attrs:
            c = "{} must be >= 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(h, attr, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), c)

    def test_zero(self):
        '''Tests validation with zero.'''
        h = Square(9, 4)
        attrs = ["size"]
        for attr in attrs:
            c = "width must be > 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(h, attr, 0)
            self.assertEqual(str(e.exception), c)

    def test_prop(self):
        '''Tests setting/getting.'''
        h = Square(9, 4)
        attrs = ["x", "y", "width", "height"]
        for attr in attrs:
            ni = randrange(10) + 1
            setattr(h, attr, ni)
            self.assertEqual(getattr(h, attr), ni)

    def test_range_zero(self):
        '''Tests in range zero'''
        h = Square(9, 4)
        h.x = 0
        h.y = 0
        self.assertEqual(h.x, 0)
        self.assertEqual(h.y, 0)

    def test_area_no(self):
        '''Tests area with no arguments'''
        h = Square(3)
        with self.assertRaises(TypeError) as e:
            Square.area()
        c = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), c)

    def test_area(self):
        '''Tests area in valide way'''
        h = Square(3)
        self.assertEqual(h.area(), 9)
        wi = randrange(10) + 1
        h.size = wi
        self.assertEqual(h.area(), wi * wi)
        wi = randrange(10) + 1
        h = Square(wi, 7, 8, 9)
        self.assertEqual(h.area(), wi * wi)
        wi = randrange(10) + 1
        h = Square(wi, y=7, x=8, id=9)
        self.assertEqual(h.area(), wi * wi)

        Base._Base__nb_objects = 0
        c1 = Square(5)
        self.assertEqual(str(c1), "[Square] (1) 0/0 - 5")
        self.assertEqual(c1.size, 5)
        c1.size = 10
        self.assertEqual(str(c1), "[Square] (1) 0/0 - 10")
        self.assertEqual(c1.size, 10)

        with self.assertRaises(TypeError) as e:
            c1.size = "1"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            c1.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_display_no(self):
        '''Tests display with no aruments.'''
        h = Square(1)
        with self.assertRaises(TypeError) as e:
            Square.display()
        c = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), c)

    def test_display(self):
        '''Tests display in a simple way.'''
        h = Square(1)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = "#\n"
        self.assertEqual(fi.getvalue(), c)
        h.size = 3
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(fi.getvalue(), c)
        h = Square(5, 6, 7)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(fi.getvalue(), c)
        h = Square(9, 8)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(fi.getvalue(), c)
        h = Square(1, 1, 10)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """\










 #
"""
        self.assertEqual(fi.getvalue(), c)

        h = Square(5)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(fi.getvalue(), c)

        h = Square(5, 5)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """\
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(fi.getvalue(), c)

        h = Square(5, 3)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(fi.getvalue(), c)

        h = Square(5, 0, 4)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(fi.getvalue(), c)

        Base._Base__nb_objects = 0
        c1 = Square(5)
        self.assertEqual(str(c1), "[Square] (1) 0/0 - 5")
        self.assertEqual(c1.area(), 25)
        fi = io.StringIO()
        with redirect_stdout(fi):
            c1.display()
        c = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(fi.getvalue(), c)

        c2 = Square(2, 2)
        self.assertEqual(str(c2), "[Square] (2) 2/0 - 2")
        self.assertEqual(c2.area(), 4)
        fi = io.StringIO()
        with redirect_stdout(fi):
            c2.display()
        c = """\
  ##
  ##
"""
        self.assertEqual(fi.getvalue(), c)

        c3 = Square(3, 1, 3)
        self.assertEqual(str(c3), "[Square] (3) 1/3 - 3")
        self.assertEqual(c3.area(), 9)
        fi = io.StringIO()
        with redirect_stdout(fi):
            c3.display()
        c = """\



 ###
 ###
 ###
"""
        self.assertEqual(fi.getvalue(), c)

    def test_args_str(self):
        '''Tests __str__ with no arguments.'''
        h = Square(3, 4)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        c = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), c)

    def test_str(self):
        '''Tests __str__ in a valid way.'''
        h = Square(3)
        c = '[Square] (1) 0/0 - 3'
        self.assertEqual(str(h), c)
        h = Square(1, 1)
        c = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(h), c)
        h = Square(3, 4, 5)
        c = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(h), c)
        h = Square(10, 20, 30, 40)
        c = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(h), c)

    def test_update_no(self):
        '''Tests update with no aruments.'''
        h = Square(3, 4)
        with self.assertRaises(TypeError) as e:
            Square.update()
        c = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), c)

        n = h.__dict__.copy()
        h.update()
        self.assertEqual(h.__dict__, n)

    def test_update(self):
        '''Tests update with vailde args'''
        h = Square(5, 2)
        n = h.__dict__.copy()

        h.update(10)
        n["id"] = 10
        self.assertEqual(h.__dict__, n)

        h.update(10, 5)
        n["_Rectangle__height"] = 5
        n["_Rectangle__width"] = 5
        self.assertEqual(h.__dict__, n)

        h.update(10, 5, 20)
        n["_Rectangle__x"] = 20
        self.assertEqual(h.__dict__, n)

        h.update(10, 5, 20, 25)
        n["_Rectangle__y"] = 25
        self.assertEqual(h.__dict__, n)

    def test_update_b(self):
        '''Tests update with bad arguments.'''
        h = Square(5, 2)
        n = h.__dict__.copy()

        h.update(10)
        n["id"] = 10
        self.assertEqual(h.__dict__, n)

        with self.assertRaises(ValueError) as e:
            h.update(12, -3)
        c = "width must be > 0"
        self.assertEqual(str(e.exception), c)

        with self.assertRaises(ValueError) as e:
            h.update(12, 3, -17)
        c = "x must be >= 0"
        self.assertEqual(str(e.exception), c)

        with self.assertRaises(ValueError) as e:
            h.update(12, 3, 17, -43)
        c = "y must be >= 0"
        self.assertEqual(str(e.exception), c)

    def test_update_kw(self):
        '''Tests with keywords.'''
        h = Square(5, 2)
        n = h.__dict__.copy()

        h.update(id=10)
        n["id"] = 10
        self.assertEqual(h.__dict__, n)

        h.update(size=17)
        n["_Rectangle__height"] = 17
        n["_Rectangle__width"] = 17
        self.assertEqual(h.__dict__, n)

        h.update(x=20)
        n["_Rectangle__x"] = 20
        self.assertEqual(h.__dict__, n)

        h.update(y=25)
        n["_Rectangle__y"] = 25
        self.assertEqual(h.__dict__, n)

    def test_update_kw2(self):
        '''Tests update  with two keywords.'''
        h = Square(5, 2)
        n = h.__dict__.copy()

        h.update(id=10)
        n["id"] = 10
        self.assertEqual(h.__dict__, n)

        h.update(id=10, size=5)
        n["_Rectangle__height"] = 5
        n["_Rectangle__width"] = 5
        self.assertEqual(h.__dict__, n)

        h.update(id=10, size=5, x=20)
        n["_Rectangle__x"] = 20
        self.assertEqual(h.__dict__, n)

        h.update(id=10, size=5, x=20, y=25)
        n["_Rectangle__y"] = 25
        self.assertEqual(h.__dict__, n)

        h.update(y=25, id=10, x=20, size=5)
        self.assertEqual(h.__dict__, n)

        Base._Base__nb_objects = 0
        c1 = Square(5)
        self.assertEqual(str(c1), "[Square] (1) 0/0 - 5")

        c1.update(11)
        self.assertEqual(str(c1), "[Square] (11) 0/0 - 5")

        c1.update(1, 4)
        self.assertEqual(str(c1), "[Square] (1) 0/0 - 4")

        c1.update(1, 4, 5)
        self.assertEqual(str(c1), "[Square] (1) 5/0 - 4")

        c1.update(1, 2, 3, 4)
        self.assertEqual(str(c1), "[Square] (1) 3/4 - 2")

        c1.update(x=12)
        self.assertEqual(str(c1), "[Square] (1) 12/4 - 2")

        c1.update(size=7, y=1)
        self.assertEqual(str(c1), "[Square] (1) 12/1 - 7")

        c1.update(size=7, id=89, y=1)
        self.assertEqual(str(c1), "[Square] (89) 12/1 - 7")

    def test_to_dicti(self):
        '''Tests to_dictionary function'''
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        c = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), c)

        h = Square(1)
        n = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(h.to_dictionary(), n)

        h = Square(9, 2, 3, 4)
        n = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(h.to_dictionary(), n)

        h.x = 12
        h.y = 40
        h.size = 50
        n = {'x': 12, 'y': 40, 'size': 50, 'id': 4}
        self.assertEqual(h.to_dictionary(), n)

        c1 = Square(10, 2, 1)
        c1_dicti = c1.to_dictionary()
        c2 = Square(1, 1)
        c2.update(**c1_dicti)
        self.assertEqual(str(c1), str(c2))
        self.assertNotEqual(c1, c2)


if __name__ == "__main__":
    unittest.main()
