#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <floatobject.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: PyObject pointer to the bytes object
 *
 */
void print_python_bytes(PyObject *p)
{
	size_t j, l, s;
	char *sr;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyVarObject *)p)->ob_size;
	sr =  ((PyBytesObject *)p)->ob_sval;
	l = s + 1 > 10 ? 10 : s + 1;
	printf("  size: %lu\n", s);
	printf("  trying string: %s\n", sr);
	printf("  first %lu bytes: ", l);
	for (j = 0; j < l; j++)
		printf("%02hhx%s", sr[j], j + 1 < l ? " " : "");
	printf("\n");
}
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
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	data = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n",
			PyOS_double_to_string(data, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
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
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		printf("Element %d: %s\n", i,
				((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
		else if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "float"))
			print_python_float(((PyListObject *)p)->ob_item[i]);
	}
}

