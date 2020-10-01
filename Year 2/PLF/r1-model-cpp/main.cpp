#include "lista.h"
#include <iostream>
using namespace std;



int number_of_appearances(TElem x, PNod p) {
    int equal = 0;
    if(p == NULL)
        return 0;
    if(p->e == x)
        equal = 1;
    p = p->urm;

    return equal + number_of_appearances(x, p);
}


bool is_set(PNod p, Lista l) {
    bool equal = true;
    PNod t = l._prim;
    if(p == NULL)
        return true;
    if(number_of_appearances(p->e, t) > 1)
        equal = false;
    p = p->urm;

    return equal && is_set(p, l);
}

int distinct_count(PNod p, Lista l) {
    int equal = 0;
    PNod t = l._prim;
    if(p == NULL)
        return 0;
    if(number_of_appearances(p->e, t) == 1)
        equal = 1;
    p = p->urm;

    return equal + distinct_count(p, l);
}

int main()
{
    Lista l;
    l=creare();
    PNod p = l._prim;
    PNod t = l._prim;
    tipar(l);
    cout << is_set(p, l) << " " << distinct_count(t, l);
}




/*


 number_of_appearances(x, l1...ln)

 0, if n = 0, l is an empty list
 1 + number_of_appearances(x, l2...ln), if x == l1
 0 + number_of_appearances(x, l2...ln), otherwise


 3. a. Check if a list is a set.

  is_set(l1, ...,ln)

  true, if n = 0, l is an empty list
  is_set(li + 1...ln) && false, if number_of_appearances(li, l1...ln) > 1
                      && true, otherwise


  b. Determine the number of distinct elements from a list.

  distinct_count(l1, ..., ln)

  0, if n = 0, l is an empty list
  distinct_count(li + 1...ln) + 1, if number_of_appearances(li, l1...ln) == 1,
                              + 0, otherwise

 */