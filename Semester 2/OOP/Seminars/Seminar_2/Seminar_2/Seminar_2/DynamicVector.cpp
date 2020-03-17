#include "DynamicVector.h"

DynamicVector::DynamicVector(int capacity)
{
	this->capacity = capacity;
	this->size = 0;
	this->elems = new TElem[this->capacity];
}

DynamicVector::~DynamicVector()
{
	delete[] this->elems;
}

DynamicVector::DynamicVector(const DynamicVector& vector)
{
	this->capacity = vector.capacity;
	this->size = vector.size;
	this->elems = new TElem[this->capacity];
	for (int i = 0; i <= this->size; ++i)
		this->elems[i] = vector.elems[i];

}

DynamicVector& DynamicVector::operator=(const DynamicVector& vectorToBeCopied)
{
	if (this == &vectorToBeCopied)
		return *this;
	this->capacity = vectorToBeCopied.capacity;
	this->size = vectorToBeCopied.size;
	delete[] this->elems;
	this->elems = new TElem[this->capacity];
	for (int i = 0; i <= this->size; ++i)
		this->elems[i] = vectorToBeCopied.elems[i];
	return *this;

}

void DynamicVector::add(const TElem& elem)
{
	if (this->size == this->capacity)
		this->resize();
	this->elems[this->size++] = elem;
}

void DynamicVector::resize()
{
	this->capacity *= 2;
	TElem* aux = new TElem[this->capacity];
	for (int i = 0; i <= this->size; ++i)
		aux[i] = this->elems[i];
	delete[] this->elems;
	this->elems = aux;
