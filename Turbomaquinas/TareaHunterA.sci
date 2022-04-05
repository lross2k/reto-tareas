// Calculos para Tarea Hunter A
// @author Luis Ross

// Funciones usadas
// Interpolacion lineal
function y = interpLin(x, x0, x1, y0, y1);
    y = y0 + (y1 - y0)/(x1 - x0) * (x - x0);
end;
// Convertir de litros por segundo a galones por minuto
function gpm = lpsAGpm(Lps);
	gpm = Lps * 60.0/3.785;
end;
// Calculo de demanda en L/s a partir de unidades accesorio
function caudalDemanda = demandaDeUA(ua, predom);
    if ua > 1200 then;
        caudalDemanda = 0.121 * ua ^ 0.676;
    else;
        if predom == "fluxometro" then;
            if ua > 150 then;
			    caudalDemanda = 0.0122 * ua + 3.37 - 2.15 * 10^(-6) * ua^2;
			elseif ua < 150 then;
			    caudalDemanda = 0.68 * ua^0.4;
			end;
        elseif predom == "tanque" then;
            if ua > 100 then;
			    caudalDemanda = 0.0145 * ua + 1.39 - 2.83 * 10^(-6) * ua^2;
			elseif ua < 100 then;
			    caudalDemanda = 0.68 * ua^0.4;
			end;
        end;
    end;
end;

// Definicion de variables
inodoro    = 26; // fluxometro
lavatorio  = 26;
tina       = 8;
ducha      = 18;
fregadero  = 0;
grifo      = 1;  // "Service Sink"
gruposBath = 0;  // Cantidad de grupos de baño

// Agrupar baños completos, estos pueden tener 3 o 4 piezas
// Grupos de 4 piezas
while tina>0
	gruposBath = gruposBath + 1;
	tina       = tina - 1;
	lavatorio  = lavatorio - 1;
	inodoro    = inodoro - 1;
	//ducha      = ducha - 1;
end
// Grupos de 3 piezas
while ducha>0
	gruposBath = gruposBath + 1;
	lavatorio  = lavatorio - 1;
	inodoro    = inodoro - 1;
	ducha      = ducha - 1;
end

// Resolver parte 1 de la tarea
disp("Seccion 1)");

// Mostrar los valores resultantes
disp("Grupos de 3 y 4: "      + string(gruposBath));
disp("Lavatorios restantes: " + string(lavatorio));
disp("Inodoros restantes: "   + string(inodoro));
disp("Grifos restantes: "     + string(grifo));
disp("Duchas restantes: "     + string(ducha));
disp("Tinas restantes: "      + string(tina));

// Si no quedan piezas para agrupar baños de 3 o 4 piezas
// sanitarias, sumar los efectos de las piezas individuales
// esto nos dará mayores unidades de consumo

// Usando la tabla de Hunter actualizado se asignan los 
// valores de cargas totales primero
grupoBathValveTotalUC = 8.0; // Bath group flush valve total
lavatorioPubTotalUC   = 2.0; // Se asume que es publico
inodoroTotalUC        = 2.0; // Bidet
grifoTotalUC          = 3.0;

// Se suman las unidades de consume para todos los valores
unidadesConsumoTotales = grupoBathValveTotalUC * gruposBath + ..
                         lavatorioPubTotalUC * lavatorio    + ..
                         inodoroTotalUC * inodoro           + ..
                         grifoTotalUC * grifo;

// Mostrar unidades de consumo totales resultantes
disp("Unidades de consumo totales: " + string(unidadesConsumoTotales));

// Caudal probable, resultado debe ser interpolado
// caudalProbable = interpLin(179, 160, 180, 5.27, 5.50);
// disp("Caudal probable: " + string(caudalProbable));

// Demanda segun la tabla 6.4 de unidades accesorio
demandaTotal = demandaDeUA(unidadesConsumoTotales, "fluxometro");
disp("Demanda total: " + string(demandaTotal) + " L/s");

// Convertir de L/s a GPM
disp("Demanda total: " + string(lpsAGpm(demandaTotal)) + " GPM");

// Resolver parte 2 de la tarea
disp("Seccion 2)");

// Multiplicar por ocho las unidades accesorio, con esto se calcula 
// de nuevo la demanda pico usando la tabla 6.4
demandaTotal = demandaDeUA(8 * unidadesConsumoTotales, "fluxometro");
disp("Demanda total: " + string(demandaTotal) + " L/s");
disp("Demanda total: " + string(lpsAGpm(demandaTotal)) + " GPM");

// Resolver parte 3 de la tarea
disp("Seccion 3)");

// Se vuelve a calcular el caudal total pero con valores agua caliente
// los inodoros no requiere de agua caliente
grupoBathValveHotUC = 8.0; // Bath group flush valve total
lavatorioPubHotUC   = 2.0; // Se asume que es publico
grifoHotUC          = 3.0;

// Se suman las unidades de consume para todos los valores
unidadesConsumoHot = grupoBathValveHotUC * gruposBath + ..
                     lavatorioPubHotUC * lavatorio    + ..
                     grifoHotUC * grifo;

// Demanda segun la tabla 6.4 de unidades accesorio
demandaHot = demandaDeUA(8 * unidadesConsumoHot, "fluxometro");
disp("Demanda agua caliente: " + string(demandaHot) + " L/s");
disp("Demanda agua caliente: " + string(lpsAGpm(demandaHot)) + " GPM");
