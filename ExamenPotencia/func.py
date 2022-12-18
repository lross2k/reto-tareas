from math import pi, acos, degrees, radians, atan, cos, sin, tan
from math import sqrt as rsqrt
from cmath import sqrt, cosh, sinh, tanh
acosd = lambda angle: degrees(acos(angle))
atand = lambda angle: degrees(atan(angle))
mag   = lambda rect_v: rsqrt(rect_v.real**2 + rect_v.imag**2)
cosd  = lambda angle: cos(radians(angle))
tand  = lambda angle: tan(radians(angle))
ang   = lambda rect_v: atand(rect_v.imag/rect_v.real)
rect  = lambda magnitude,angle: complex(magnitude*cos(radians(angle)),magnitude*sin(radians(angle)))
prt   = lambda valor: str(mag(valor)) + "∡" + str(ang(valor)) + "°"