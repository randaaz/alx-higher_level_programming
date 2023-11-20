#include <Python.h>
#include <stdio.h>
#include <floatobject.h>

/**
 * print_python_float - Prints information about a Python float object.
 * @p: PyObject representing a Python float.
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

	data = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %.*g\n", 16, data);
}

/**
 * print_python_list - Prints information about a Python list
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	int i;
	PyObject *item;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: PyObject pointer to the bytes object
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

	s = ((PyVarObject *)p)->ob_size;
	st = ((PyBytesObject *)p)->ob_sval;
	l = s + 1 > 10 ? 10 : s + 1;

	printf("  size: %lu\n", s);
	printf("  trying string: %s\n", st);
	printf("  first %lu bytes: ", l);

	for (j = 0; j < l; j++)
	{
		printf("%02hhx%s", st[j], j + 1 < l ? " " : "");
	}

	printf("\n");
}


