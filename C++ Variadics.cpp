// Enter your code for reversed_binary_value<bool...>()

#include <vector>
#include "math.h"
#include <initializer_list>
#include <stdarg.h>

template <bool...digits>
int reverse(int count,...)
{
    va_list ap;
    int j;
    double sum = 0;
    va_start(ap, count); /* Requires the last fixed parameter (to get the address) */
    for (j = 0; j < count; j++)
    {
        sum += va_arg(ap, int)*pow(2,j); /* Increments ap to the next argument. */
    }
    //cout<<sum<<endl;
    va_end(ap);
    return sum;
}

template <bool...digits>
int reversed_binary_value(...)
{
    return reverse(sizeof...(digits), digits...);
}
