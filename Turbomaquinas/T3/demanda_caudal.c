#include "demanda_caudal.h"
#include <math.h>

/* Calculo de demanda en L/s a partir de unidades accesorio 
 * (función originalmente escrita en Scilab */
double demanda_de_ua(ua, predom)
    double ua;
    int predom;
{
    double caudal_demanda = 0.0;
    if (ua > 1200.0)
    {
        caudal_demanda = 0.121 * pow(ua,0.676);
    }
    else
    {
        if (predom == fluxometro)
        {
            if (ua > 150)
            {
			    caudal_demanda = 0.0122 * ua + 3.37 - 2.15 * pow(10,-6) * ua*ua;
            }
			else
            {
			    caudal_demanda = 0.68 * pow(ua,0.4);
            }
        }
        else if (predom == tanque)
        {
            if (ua > 100)
            {
                caudal_demanda = 0.0145 * ua + 1.39 - 2.83 * pow(10,-6) * ua*ua;
            }
			else
            {
			    caudal_demanda = 0.68 * pow(ua,0.4);
            }
        }
    }
    return(caudal_demanda);
}

double lps_a_gpm(lps)
    double lps;
{
    return(lps * 15.8503231);
}

double demanda_ua_gpm(ua, predom)
    double ua;
    int predom;
{
    return(lps_a_gpm(demanda_de_ua(ua, predom)));
}

