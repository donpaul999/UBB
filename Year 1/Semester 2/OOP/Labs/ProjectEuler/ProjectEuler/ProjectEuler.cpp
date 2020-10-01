#include <stdio.h>
#include <math.h>
bool isprime(long long int num) {
    long long int i;
    if (num == 2)
        return 1;
    if (num % 2 == 0 || num < 2)
        return 0;
    for (i = 3; i * i < num; i += 2)
        if (num % i == 0)
            return 0;
    return 1;
}
int main()
{
    int f = 1, s = 2, sum = 0, i;
    long long int num = sqrt(600851475143), number = 600851475143;
    for (i = num; i >= 3; i -= 2) {
        if (number % i == 0)
            if (isprime(number))
                break;
            
    }
    printf("%d", number);
    return 0;
}

