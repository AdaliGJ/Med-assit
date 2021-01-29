#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <math.h>
#include <fstream>

using namespace std;

//Proyecto final
//Jeremy Cáceres y Adalí Garrán

//Función auxiliar 1; convertir un string en un int
int parseInt(const string& real) {

	//atoi: función predefinida para convertir de string a int
	int resultado = atoi(real.c_str());//Devuelve 0 si no es válido

	return resultado;
}
