from libc.math cimport sin, cos, asin, sqrt
import numpy as np
cimport numpy as np

cdef HaversineDistance(double Lat1, double Lon1, double Lat2, double Lon2):
  cdef double PI = 3.1415927
  cdef double Lat1R = (Lat1* PI / 180);
  cdef double Lon1R = (Lon1* PI / 180);
  cdef double Lat2R = (Lat2* PI / 180);
  cdef double Lon2R = (Lon2* PI / 180);
  cdef double u = sin((Lat2R - Lat1R)/2);
  cdef double v = sin((Lon2R - Lon1R)/2);
  return 2.0 * 3958.8 * asin(sqrt(u * u + cos(Lat1R) * cos(Lat2R) * v * v));

