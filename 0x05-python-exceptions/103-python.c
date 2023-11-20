#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <floatobject.h>

/**
 * print_python_float - Prints information about a Python float object.
 * @p: PyObject representing a Python float.
 *
 */

void print_python_float(PyObject *p)
{
	double data;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	data = PyFloat_AS_DOUBLE(p);
	printf("  value: %s\n", PyOS_double_to_string(data, 'r', '0', Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_list - Prints information about a Python list
 * @p: PyObject representing a Python list
 */

void print_python_list(PyObject *p)
{
	int i;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		if (PyBytes_Check(PyList_GetItem(p, i)))
			print_python_bytes(PyList_GetItem(p, i));
		else if (PyFloat_Check(PyList_GetItem(p, i)))
			print_python_float(PyList_GetItem(p, i));
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: PyObject pointer to the bytes object
 *
 */
void print_python_bytes(PyObject *p)
{
	size_t j, l, s;
	char *st;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = PyBytes_GET_SIZE(p);
	st = PyBytes_AsString(p);
	l = s > 10 ? 10 : s;
	printf("  size: %lu\n", s);
	printf("  trying string: %s\n", st);
	printf("  first %lu bytes: ", l);
	for (j = 0; j < l; j++)
	{
		printf("%02hhx%s", st[j], j + 1 < l ? " " : "");
	}
	printf("\n");
}

