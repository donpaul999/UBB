#include "Planet.h"
#include <string.h>
#include <assert.h>

Planet createPlanet(char name[], char type[], double distance)
{
	Planet p;
	strcpy(p.name, name);
	strcpy(p.type, type);
	p.distanceFromEarth = distance;
	return p;
}

double getDistance(Planet p)
{
	return p.distanceFromEarth;
}

char* getName(Planet* p)
{
	return p->name;
}


void testPlanet() {
	Planet p;
	p = createPlanet("Pluto", "small", 123254.2);
	assert(getDistance(p) == 123254.2);
	assert(!strcmp(getName(&p),"Pluto"));
}

