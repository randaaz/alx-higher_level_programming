#include <Python.h>

/**
 * print_python_list_info - Prints information about a Python list
 * @p: PyObject representing a Python list
 */

void print_python_list_info(PyObject *p)
{
	int  volume, assign, j;
	PyObject *o;

	volume = Py_SIZE(p);
	assign = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python list = %d\n", volume);
	printf("[*] Allocated = %d\n", assign);

	for (j = 0; j < volume; j++)
	{
		printf("Element %d: ", j);

		o = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
