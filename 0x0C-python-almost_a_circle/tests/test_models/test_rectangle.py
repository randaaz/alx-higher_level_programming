#!/usr/bin/python3
'''Rectangle unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class CustomRectangleTests(unittest.TestCase):
    '''CustomRectangleTests'''

    def setUp(self):
        '''Tests setUp'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''tests tearDown'''
        pass

    def test_c(self):
        '''Tests the type of class'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_inher(self):
        '''Tests if class inherits onther class'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_no_args(self):
        '''Tests tearDown'''
        with self.assertRaises(TypeError) as e:
            h = Rectangle()
        c = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(e.exception), c)

    def test_many_args(self):
        '''Tests  test_many_args'''
        with self.assertRaises(TypeError) as e:
            h = Rectangle(9, 4, 5, 2, 3, 8)
        c = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(e.exception), c)

    def test__one_args(self):
        '''Tests test_many_args.'''
        with self.assertRaises(TypeError) as e:
            h = Rectangle(1)
        c = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), c)

    def test_inst(self):
        '''instantiation.'''
        h = Rectangle(10, 20)
        self.assertEqual(str(type(h)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(h, Base))
        n = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(h.__dict__, n)

        with self.assertRaises(TypeError) as e:
            h = Rectangle("1", 2)
        m = "width must be an integer"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(TypeError) as e:
            h = Rectangle(9, "4")
        m = "height must be an integer"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(TypeError) as e:
            h = Rectangle(9, 4, "5")
        m = "x must be an integer"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(TypeError) as e:
            h = Rectangle(9, 4, 5, "2")
        m = "y must be an integer"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(ValueError) as e:
            h = Rectangle(-9, 4)
        m = "width must be > 0"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(ValueError) as e:
            h = Rectangle(9, -4)
        m = "height must be > 0"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(ValueError) as e:
            h = Rectangle(0, 4)
        m = "width must be > 0"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(ValueError) as e:
            h = Rectangle(9, 0)
        m = "height must be > 0"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(ValueError) as e:
            h = Rectangle(9, 4, -5)
        m = "x must be >= 0"
        self.assertEqual(str(e.exception), m)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(9, 4, 5, -2)
        m = "y must be >= 0"
        self.assertEqual(str(e.exception), m)

    def test_inst_p(self):
        '''Tests  test_many_args'''
        h = Rectangle(3, 12, 13, 40)
        n = {'_Rectangle__height': 12, '_Rectangle__width': 3,
             '_Rectangle__x': 13, '_Rectangle__y': 40, 'id': 1}
        self.assertEqual(h.__dict__, n)

        h = Rectangle(3, 12, 13, 40, 16)
        n = {'_Rectangle__height': 12, '_Rectangle__width': 3,
             '_Rectangle__x': 13, '_Rectangle__y': 40, 'id': 16}
        self.assertEqual(h.__dict__, n)

    def test_inst_kw(self):
        '''Tests with keywords '''
        h = Rectangle(900, 400, id=249, y=11, x=909)
        n = {'_Rectangle__height': 400, '_Rectangle__width': 900,
             '_Rectangle__x': 909, '_Rectangle__y': 11, 'id': 249}
        self.assertEqual(h.__dict__, n)

    def test_id_inher(self):
        '''Tests inherted with id.'''
        Base._Base__nb_objects = 16
        h = Rectangle(4, 2)
        self.assertEqual(h.id, 17)

    def test_prop(self):
        '''Tests getters/setters.'''
        h = Rectangle(5, 9)
        h.width = 100
        h.height = 101
        h.x = 102
        h.y = 103
        n = {'_Rectangle__height': 101, '_Rectangle__width': 100,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(h.__dict__, n)
        self.assertEqual(h.width, 100)
        self.assertEqual(h.height, 101)
        self.assertEqual(h.x, 102)
        self.assertEqual(h.y, 103)

    def _types(self):
        '''Tests invaled type'''
        tup = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
               [4], {5}, {6: 7}, None)
        return tup

    def test_type1(self):
        '''Tests validation type.'''
        h = Rectangle(9, 4)
        attrs = ["x", "y", "width", "height"]
        for attr in attrs:
            c = "{} must be an integer".format(attr)
            for invalid_type in self._types():
                with self.assertRaises(TypeError) as e:
                    setattr(h, attr, invalid_type)
                self.assertEqual(str(e.exception), c)

    def test_val_v_neg_t(self):
        '''Tests test_val_v_neg_gt.'''
        h = Rectangle(9, 4)
        attrs = ["width", "height"]
        for attr in attrs:
            c = "{} must be > 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(h, attr, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), c)

    def test_val_v_neg_e(self):
        '''Tests test_val_v_neg_e'''
        h = Rectangle(9, 4)
        attrs = ["x", "y"]
        for attr in attrs:
            c = "{} must be >= 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(h, attr, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), c)

    def test__val_zero(self):
        '''Tests validation with zero.'''
        h = Rectangle(9, 4)
        attrs = ["width", "height"]
        for attr in attrs:
            c = "{} must be > 0".format(attr)
            with self.assertRaises(ValueError) as e:
                setattr(h, attr, 0)
            self.assertEqual(str(e.exception), c)

    def test_S_G_pro(self):
        '''Tests setting/getting.'''
        h = Rectangle(9, 4)
        attrs = ["x", "y", "width", "height"]
        for attr in attrs:
            na = randrange(10) + 1
            setattr(h, attr, na)
            self.assertEqual(getattr(h, attr), na)

    def test_range_zero(self):
        '''Tests with zero.'''
        h = Rectangle(9, 4)
        h.x = 0
        h.y = 0
        self.assertEqual(h.x, 0)
        self.assertEqual(h.y, 0)

    # ----------------- Tests for #4 ------------------------
    def test_area_no(self):
        '''Tests area method in invalid way.'''
        r = Rectangle(3, 8)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_area(self):
        '''Tests area method in valide way.'''
        h = Rectangle(3, 8)
        self.assertEqual(h.area(), 24)
        wi = randrange(10) + 1
        hi = randrange(10) + 1
        h.width = wi
        h.height = hi
        self.assertEqual(h.area(), wi * hi)
        wi = randrange(10) + 1
        hi = randrange(10) + 1
        h = Rectangle(wi, hi, 7, 8, 9)
        self.assertEqual(h.area(), wi * hi)
        wi = randrange(10) + 1
        hi = randrange(10) + 1
        h = Rectangle(wi, hi, y=7, x=8, id=9)
        self.assertEqual(h.area(), wi * hi)

        h1 = Rectangle(5, 4)
        self.assertEqual(h1.area(), 20)

        h2 = Rectangle(4, 12)
        self.assertEqual(h2.area(), 48)

        h3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(h3.area(), 56)

    # ----------------- Tests for #5 & #7 ------------------------
    def test_display(self):
        '''Tests display.'''
        h = Rectangle(1, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        c = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), c)

    def test_display_s(self):
        '''Tests display in simple way'''
        h = Rectangle(1, 1)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = "#\n"
        self.assertEqual(fi.getvalue(), c)
        h.width = 3
        h.height = 5
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(fi.getvalue(), c)
        h = Rectangle(5, 6, 7, 8)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """







       #####
       #####
       #####
       #####
       #####
       #####
"""
        self.assertEqual(fi.getvalue(), c)
        h = Rectangle(9, 8)
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
"""
        self.assertEqual(fi.getvalue(), c)
        h = Rectangle(1, 1, 10, 10)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """\










          #
"""
        self.assertEqual(fi.getvalue(), c)

        h = Rectangle(5, 5)
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

        h = Rectangle(5, 3, 5)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """\
     #####
     #####
     #####
"""
        self.assertEqual(fi.getvalue(), c)

        h = Rectangle(5, 3, 0, 4)
        fi = io.StringIO()
        with redirect_stdout(fi):
            h.display()
        c = """\




#####
#####
#####
"""
        self.assertEqual(fi.getvalue(), c)

        # ----------------- Tests for #6 ------------------------

    def test_str_no_a(self):
        '''Tests __str___ with no arguments.'''
        h = Rectangle(3, 4)
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        c = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), c)

    def test_str(self):
        '''Tests __str__ in vaild way.'''
        h = Rectangle(3, 4)
        c = '[Rectangle] (1) 0/0 - 3/4'
        self.assertEqual(str(h), c)
        h = Rectangle(1, 1, 1)
        c = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(h), c)
        h = Rectangle(3, 4, 5, 6)
        c = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(h), c)

        Base._Base__nb_objects = 0
        h1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(h1), "[Rectangle] (12) 2/1 - 4/6")

        h2 = Rectangle(5, 5, 1)
        self.assertEqual(str(h2), "[Rectangle] (1) 1/0 - 5/5")

        # ----------------- Tests for #8 & #9 ------------------------
    def test_no_a_update(self):
        '''Tests with no arguments.'''
        h = Rectangle(3, 4)
        with self.assertRaises(TypeError) as e:
            Rectangle.update()
        c = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), c)

        n = h.__dict__.copy()
        h.update()
        self.assertEqual(h.__dict__, n)

    def test_update(self):
        '''Tests update in valid way.'''
        h = Rectangle(5, 2)
        n = h.__dict__.copy()

        h.update(10)
        n["id"] = 10
        self.assertEqual(h.__dict__, n)

        h.update(10, 5)
        n["_Rectangle__width"] = 5
        self.assertEqual(h.__dict__, n)

        h.update(10, 5, 17)
        n["_Rectangle__height"] = 17
        self.assertEqual(h.__dict__, n)

        h.update(10, 5, 17, 20)
        n["_Rectangle__x"] = 20
        self.assertEqual(h.__dict__, n)

        h.update(10, 5, 17, 20, 25)
        n["_Rectangle__y"] = 25
        self.assertEqual(h.__dict__, n)

    def test_update_not(self):
        '''Tests update with bad aruments.'''
        h = Rectangle(5, 2)
        n = h.__dict__.copy()

        h.update(10)
        n["id"] = 10
        self.assertEqual(h.__dict__, n)

        with self.assertRaises(ValueError) as e:
            h.update(10, -5)
        c = "width must be > 0"
        self.assertEqual(str(e.exception), c)

        with self.assertRaises(ValueError) as e:
            h.update(10, 5, -17)
        c = "height must be > 0"
        self.assertEqual(str(e.exception), c)

        with self.assertRaises(ValueError) as e:
            h.update(10, 5, 17, -20)
        c = "x must be >= 0"
        self.assertEqual(str(e.exception), c)

        with self.assertRaises(ValueError) as e:
            h.update(10, 5, 17, 20, -25)
        c = "y must be >= 0"
        self.assertEqual(str(e.exception), c)

    def test_update_kw(self):
        '''Tests update with keyword.'''
        h = Rectangle(5, 2)
        n = h.__dict__.copy()

        h.update(id=10)
        n["id"] = 10
        self.assertEqual(h.__dict__, n)

        h.update(width=5)
        n["_Rectangle__width"] = 5
        self.assertEqual(h.__dict__, n)

        h.update(height=17)
        n["_Rectangle__height"] = 17
        self.assertEqual(h.__dict__, n)

        h.update(x=20)
        n["_Rectangle__x"] = 20
        self.assertEqual(h.__dict__, n)

        h.update(y=25)
        n["_Rectangle__y"] = 25
        self.assertEqual(h.__dict__, n)

    def test_update_kw2(self):
        '''Tests with keyword.'''
        h = Rectangle(5, 2)
        n = h.__dict__.copy()

        h.update(id=10)
        n["id"] = 10
        self.assertEqual(h.__dict__, n)

        h.update(id=10, width=5)
        n["_Rectangle__width"] = 5
        self.assertEqual(h.__dict__, n)

        h.update(id=10, width=5, height=17)
        n["_Rectangle__height"] = 17
        self.assertEqual(h.__dict__, n)

        h.update(id=10, width=5, height=17, x=20)
        n["_Rectangle__x"] = 20
        self.assertEqual(h.__dict__, n)

        h.update(id=10, width=5, height=17, x=20, y=25)
        n["_Rectangle__y"] = 25
        self.assertEqual(h.__dict__, n)

        h.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(h.__dict__, n)

        Base._Base__nb_objects = 0
        h1 = Rectangle(12, 12, 12, 12)
        self.assertEqual(str(h1), "[Rectangle] (1) 12/12 - 12/12")

        h1.update(height=1)
        self.assertEqual(str(h1), "[Rectangle] (1) 12/12 - 12/1")

        h1.update(width=1, x=2)
        self.assertEqual(str(h1), "[Rectangle] (1) 2/12 - 1/1")

        h1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(h1), "[Rectangle] (89) 3/1 - 2/1")

        h1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(h1), "[Rectangle] (89) 1/3 - 4/2")

        Base._Base__nb_objects = 0
        h1 = Rectangle(12, 12, 12, 12)
        self.assertEqual(str(h1), "[Rectangle] (1) 12/12 - 12/12")

        h1.update(89)
        self.assertEqual(str(h1), "[Rectangle] (89) 12/12 - 12/12")

        h1.update(89, 2)
        self.assertEqual(str(h1), "[Rectangle] (89) 12/12 - 2/12")

        h1.update(89, 2, 3)
        self.assertEqual(str(h1), "[Rectangle] (89) 12/12 - 2/3")

        h1.update(89, 2, 3, 4)
        self.assertEqual(str(h1), "[Rectangle] (89) 4/12 - 2/3")

        h1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(h1), "[Rectangle] (89) 4/5 - 2/3")

    # ----------------- Tests for #13 ------------------------
    def test_to_dicti(self):
        '''Tests to_dictionary method'''
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        c = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), c)

        h = Rectangle(1, 4)
        n = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 4}
        self.assertEqual(h.to_dictionary(), n)

        h = Rectangle(1, 2, 3, 4, 5)
        n = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(h.to_dictionary(), n)

        h.x = 10
        h.y = 20
        h.width = 30
        h.height = 40
        n = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(h.to_dictionary(), n)

        h1 = Rectangle(10, 2, 1, 9)
        h1_dictionary = h1.to_dictionary()
        h2 = Rectangle(1, 1)
        h2.update(**h1_dictionary)
        self.assertEqual(str(h1), str(h2))
        self.assertNotEqual(h1, h2)


if __name__ == "__main__":
    unittest.main()
