#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints information about a Python list
 * @p: PyObject representing a Python list
 */

void print_python_list(PyObject *p)
{
	int volume, assign, j;
	const char *t;
	PyListObject *l = (PyListObject *)p;
	PyVarObject *v = (PyVarObject *)p;

	volume = v->ob_size;
	assign = l->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", volume);
	printf("[*] Allocated = %d\n", assign);

	for (j = 0; j < volume; j++)
	{
		t = l->ob_item[j]->ob_type->tp_name;
		printf("Element %d: %s\n", j, t);
		if (strcmp(t, "bytes") == 0)
			print_python_bytes(l->ob_item[j]);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: PyObject pointer to the bytes object
 *
 */
void print_python_bytes(PyObject *p)
{
	unsigned char j, volume;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		volume = 10;
	else
		volume = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", volume);
	for (j = 0; j < volume; j++)
	{
		printf("%02hhx", bytes->ob_sval[j]);
		if (j == (volume - 1))
			printf("\n");
		else
			printf(" ");
	}
}
