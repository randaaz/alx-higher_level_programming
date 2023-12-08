#!/usr/bin/python3
'''CustomClassTests unit tests Module.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class CustomClassTests(unittest.TestCase):
    '''Tests the CustomClassTests class.'''

    def setUp(self):
        '''Tests setUp'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Tests tearDown'''
        pass

    def test_has_attribute(self):
        '''Tests test_has_attribute'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_initial_value(self):
        '''Tests test_initial_value'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instance_creation(self):
        '''Tests test_instance_creation'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_constructor(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        m = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), m)

    def test_c_args_2(self):
        '''Tests constructor signature with 2 notself args.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        m = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), m)

    def test_c_i(self):
        '''Tests test_c_i'''
        n1 = Base()
        n2 = Base()
        self.assertEqual(n1.id + 1, n2.id)

    def test_class_and_instance_id1(self):
        '''Tests test_class_and_instance_id1'''
        n = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), n.id)

    def test_class_and_instance_id2(self):
        '''Tests test_class_and_instance_id2'''
        n = Base()
        n = Base("bar")
        n = Base(99)
        n = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), n.id)

    def test_G_c_i_in(self):
        '''test_G_c_i_in'''
        j = 99
        n = Base(j)
        self.assertEqual(n.id, j)

    def test_G_c_i_s(self):
        '''Tests test_G_c_i_s'''
        j = "helloword"
        n = Base(j)
        self.assertEqual(n.id, j)

    def test_G_i_kw(self):
        '''Tests test_G_i_kw'''
        j = 441
        n = Base(id=j)
        self.assertEqual(n.id, j)

    def test_to_json_str(self):
        '''Tests to_json_string'''
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        c = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), c)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        n = [{'x': 301, 'y': 40567, 'width': 534543, 'id': 144422,
             'height': 52520}]
        self.assertEqual(len(Base.to_json_string(n)),
                         len(str(n)))
        n = [{'x': 9, 'y': 4, 'width': 5, 'id': 2, 'height': 3}]
        self.assertEqual(len(Base.to_json_string(n)),
                         len(str(n)))
        n = [{"helloworld": 161616}]
        self.assertEqual(Base.to_json_string(n),
                         '[{"helloworld": 161616}]')

        n = [{"helloworld": 161919}, {"efg": 456}, {"HY": 0}]
        self.assertEqual(Base.to_json_string(n),
                         '[{"helloworld": 161919}, {"efg": 456}, {"HY": 0}]')

        n = [{'x': 9, 'y': 4, 'width': 5, 'id': 2, 'height': 3},
             {'x': 901, 'y': 40945, 'width': 594549, 'id': 344422,
             'height': 52520}]
        self.assertEqual(len(Base.to_json_string(n)),
                         len(str(n)))
        n = [{}]
        self.assertEqual(Base.to_json_string(n),
                         '[{}]')
        n = [{}, {}]
        self.assertEqual(Base.to_json_string(n),
                         '[{}, {}]')

        h1 = Rectangle(12, 7, 4, 8)
        dicti = h1.to_dictionary()
        json_dicti = Base.to_json_string([dicti])
        dicti = str([dicti])
        dicti = dicti.replace("'", '"')
        self.assertEqual(dicti, json_dicti)

        h1 = Rectangle(12, 7, 4, 8)
        h2 = Rectangle(9, 4, 5, 2)
        h3 = Rectangle(4, 5, 2, 3)
        dicti = [h1.to_dictionary(), h2.to_dictionary(),
                 h3.to_dictionary()]
        json_dicti = Base.to_json_string(dicti)
        dicti = str(dicti)
        dicti = dicti.replace("'", '"')
        self.assertEqual(dicti, json_dicti)

        h1 = Square(12, 7, 4)
        dicti = h1.to_dictionary()
        json_dicti = Base.to_json_string([dicti])
        dicti = str([dicti])
        dicti = dicti.replace("'", '"')
        self.assertEqual(dicti, json_dicti)

        h1 = Square(12, 7, 4)
        h2 = Square(9, 4, 5)
        h3 = Square(4, 5, 2)
        dicti = [h1.to_dictionary(), h2.to_dictionary(),
                 h3.to_dictionary()]
        json_dicti = Base.to_json_string(dicti)
        dicti = str(dicti)
        dicti = dicti.replace("'", '"')
        self.assertEqual(dicti, json_dicti)

    def test_from_json_str(self):
        '''Tests to_json_str'''
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        c = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(e.exception), c)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        c = '[{"x": 9, "y": 4, "width": 5, "id": 2, "height": 3}, \
{"x": 901, "y": 40945, "width": 594549, "id": 344422, "height": 52520}]'
        n = [{'x': 9, 'y': 4, 'width': 5, 'id': 2, 'height': 3},
             {'x': 901, 'y': 40945, 'width': 594549, 'id': 344422,
             'height': 52520}]
        self.assertEqual(Base.from_json_string(c), n)

        n = [{}, {}]
        c = '[{}, {}]'
        self.assertEqual(Base.from_json_string(c), n)
        n = [{}]
        c = '[{}]'
        self.assertEqual(Base.from_json_string(c), n)

        n = [{"helloworld": 181818}, {"efg": 945}, {"HY": 0}]
        c = '[{"helloworld": 181818}, {"efg": 945}, {"HY": 0}]'
        self.assertEqual(Base.from_json_string(c), n)

        n = [{"helloworld": 181818}]
        c = '[{"helloworld": 181818}]'
        self.assertEqual(Base.from_json_string(c), n)

        n = [{'x': 9, 'y': 4, 'width': 5, 'id': 2, 'height': 3}]
        c = '[{"x": 9, "y": 4, "width": 5, "id": 2, "height": 3}]'
        self.assertEqual(Base.from_json_string(c), n)

        n = [{'x': 901, 'y': 40945, 'width': 594549, 'id': 344422,
             'height': 52520}]
        c = '[{"x": 901, "y": 40945, "width": 594549, "id": 344422, \
"height": 52520}]'
        self.assertEqual(Base.from_json_string(c), n)

        l_n = [
            {'id': 81, 'width': 12, 'height': 2},
            {'id': 7, 'width': 9, 'height': 7}
        ]
        l_o = Rectangle.from_json_string(
            Rectangle.to_json_string(l_n))
        self.assertEqual(l_n, l_o)

    def test_s_to_file(self):
        '''Tests save_to_file'''
        import os
        h1 = Rectangle(12, 7, 4, 8)
        h2 = Rectangle(4, 2)
        Rectangle.save_to_file([h1, h2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        h2 = Rectangle(4, 2)
        Rectangle.save_to_file([h2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        h2 = Square(1)
        Square.save_to_file([h2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    def test_create(self):
        '''Tests test_create'''
        h1 = Rectangle(5, 3, 9)
        h1_dicti = h1.to_dictionary()
        h2 = Rectangle.create(**h1_dicti)
        self.assertEqual(str(h1), str(h2))
        self.assertFalse(h1 is h2)
        self.assertFalse(h1 == h2)

    def test_load_f_f(self):
        '''Tests test_load_f_f'''
        h1 = Rectangle(12, 7, 4, 8)
        h2 = Rectangle(4, 2)
        l_n = [h1, h2]
        Rectangle.save_to_file(l_n)
        l_o = Rectangle.load_from_file()
        self.assertNotEqual(id(l_n[0]), id(l_o[0]))
        self.assertEqual(str(l_n[0]), str(l_o[0]))
        self.assertNotEqual(id(l_n[1]), id(l_o[1]))
        self.assertEqual(str(l_n[1]), str(l_o[1]))

        c1 = Square(3)
        c2 = Square(7, 1, 9)
        l_n = [c1, c2]
        Square.save_to_file(l_n)
        l_o = Square.load_from_file()
        self.assertNotEqual(id(l_n[0]), id(l_o[0]))
        self.assertEqual(str(l_n[0]), str(l_o[0]))
        self.assertNotEqual(id(l_n[1]), id(l_o[1]))
        self.assertEqual(str(l_n[1]), str(l_o[1]))


if __name__ == "__main__":
    unittest.main()
