OBJS = tarea_syzer.c demanda_caudal.c
CC = gcc
CFLAG = -Wall -Werror -pedantic -Wextra -g
INCLUDE = 
LIBS = -lm

syzer:${OBJ}
	${CC} ${CFLAGS} ${INCLUDES} -o $@ ${OBJS} ${LIBS}

clean:
	rm -f *.o

