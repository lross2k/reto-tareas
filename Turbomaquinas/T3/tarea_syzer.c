/* Programación en estilo K&R C el cuál corresponde a un formato totalmente innecesario 
 * de conocer, pues se han estadarizado las formas correctas de trabajar por ISO y ANSI */

#include "demanda_caudal.h"
#include <stdio.h>

enum tipo_consumo {frio = 0, caliente, total};

int main()
{
    /* Edificio de 10 pisos, 100 apartamentos, cada apartamento tiene 2 baños con 
     * inodoro de tanque y un fregadero (service sink)
     *
     * 20 apartamentos por columna, 5 columnas de agua caliente, 5 de agua fría */

    /* const es ordinario en K&R, no keyword */
    int apartamentos = 100;
    int apt_por_col = 20;
    int pisos = 10;
    double val_grupo_baño[3] = {2.7, 1.5, 3.6};
    double val_fregadero[3] = {2.25, 2.25, 3.0};
    double tot_seccion_j = 0.0;
    double tot_seccion_t = 0.0;
    double tot_seccion_a = 0.0;
    double tot_seccion_k = 0.0;
    double tot_seccion_a4 = 0.0;
    double tot_seccion_b4 = 0.0;
    double tot_seccion_ab = 0.0;
    double tot_seccion_ab2 = 0.0;

    tot_seccion_j = (val_grupo_baño[caliente] * 2.0 + val_fregadero[caliente]) * apt_por_col;
    tot_seccion_t = (val_grupo_baño[frio] * 2.0 + val_fregadero[frio]) * apt_por_col;
    /* Debio a que A es el último piso de una columna de agua caliente, sólo 2 apt */
    tot_seccion_a = (val_grupo_baño[caliente] * 2.0 + val_fregadero[caliente]) * (apt_por_col/pisos);
    tot_seccion_k = (val_grupo_baño[frio] * 2.0 + val_fregadero[frio]) * (apt_por_col/pisos);
    tot_seccion_a4 = (val_grupo_baño[caliente] * 2.0 + val_fregadero[caliente]) * apartamentos; 
    tot_seccion_b4 = (val_grupo_baño[frio] * 2.0 + val_fregadero[frio]) * apartamentos; 
    /* Para AB se considera las ua de Hunter totales */
    tot_seccion_ab = (val_grupo_baño[total] * 2.0 + val_fregadero[total]) * apartamentos;
    /* Alternativamente AB se calcula con las ua de Hunter frio y caliente sumadas */
    tot_seccion_ab2 = tot_seccion_a4 + tot_seccion_b4;

    printf("Sección J: %.3f   GPM\n", demanda_ua_gpm(tot_seccion_j, tanque));
    printf("Sección T: %.3f   GPM\n", demanda_ua_gpm(tot_seccion_t, tanque));
    printf("Sección A: %.3f   GPM\n", demanda_ua_gpm(tot_seccion_a, tanque));
    printf("Sección K: %.3f   GPM\n", demanda_ua_gpm(tot_seccion_k, tanque));
    printf("Sección A4: %.3f  GPM\n", demanda_ua_gpm(tot_seccion_a4, tanque));
    printf("Sección B4: %.3f  GPM\n", demanda_ua_gpm(tot_seccion_b4, tanque));
    printf("Sección AB: %.3f  GPM\n", demanda_ua_gpm(tot_seccion_ab, tanque));
    printf("Asumiendo que se suman las ua de A4 y B4\n");
    printf("Sección AB: %.3f GPM\n", demanda_ua_gpm(tot_seccion_ab2, tanque));

    /* Calculos para diametro */
    return(0);
}

