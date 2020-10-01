#pragma once
#include "Song.h"

typedef Song TElem;

class DynamicVector
{
private:
	int capacity;
	int size;
	TElem* elems;
public:
	DynamicVector(int capacity = 10);
	~DynamicVector();
	DynamicVector(const DynamicVector& vector);
	DynamicVector& operator=(const DynamicVector& vectorToBeCopied);
	void add(const TElem& elem);
private:
	void resize();

public:
	class iterator {
	private:
		TElem* ptr;
	public:
		iterator(TElem* ptr);
		bool operator!=(const iterator& it);
		iterator operator++();
		iterator operator++(int i);
	};
	typename iterator begin();
	typename iterator end();
};


