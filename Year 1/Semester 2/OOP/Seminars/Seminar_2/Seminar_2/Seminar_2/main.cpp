#include <iostream>
#include "DynamicVector.h"
#include <crtdbg.h>
int main() {
	DynamicVector<int> v{ 5 };
	v.add(1);
	v.add(2);
	v.add(3);
	for (DynamicVector::iterator it = v.begin(); it != v.end(); ++it)
		std::cout << *it<<'\n';
	_CrtDumpMemoryLeaks();
	return 0;
}
