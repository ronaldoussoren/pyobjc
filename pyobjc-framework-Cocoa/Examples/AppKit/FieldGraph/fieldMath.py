from math import pi, sin, cos, hypot, sqrt

# Math functions

def degToRad(deg):
    return (deg/180.0)*pi

def radToDeg(rad):
    return (rad/pi)*180.0

def polarToRect(polar):
    r = polar[0]
    theta = polar[1]
    return (r*cos(theta), r*sin(theta))

def bessel(z, t=0.00001):
    j = 1
    jn = 1
    zz4 = z*z/4
    for k in range(1, 100):
        jn *= -1 * zz4 / (k*k)
        j += jn

        if jn < 0:
            if jn > t:
                break
        else:
            if jn < t:
                break
    return j
