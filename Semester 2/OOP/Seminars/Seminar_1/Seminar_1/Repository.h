#pragma once
#include "Planet.h"

#define MAX_DIM 100

typedef struct
{
	Planet elems[MAX_DIM];
	int length;
}Repository;


Repository* createRepository();
void destroyRepository(Repository* repo);

/*
	Search a planet in the repository.
	Input: repo - pointer to Repository
		   p - Planet to search
	Output: 1 - if the planet was found
			0 - otherwise
*/

int findPlanet(Repository* repo, Planet p);

/*
	Adds a planet to the repository.
	Input: repo - pointer to Repository
		   p - Planet
	Output: 1 - if the planet was not added(it already exists)
			0 - otherwise
*/

int addPlanet(Repository* repo, Planet p);