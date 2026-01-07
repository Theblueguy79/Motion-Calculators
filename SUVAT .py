
s, u, v, a, t = None, None, None, None, None


def isNotNone(value):
    return value is not None

def solve_eq(x,eq): 



#Must explicitly provide None for unknown variables
def solve_motion(s=None, u=None, v=None, a=None, t=None): 
    variables = [s, u, v, a, t]
    known= []
    unknown = []
    for i in variables:
        if isNotNone(i):
            known.append(i)
        else:
            unknown.append(i)
    if len(known) <3:

        return f"Not enough variables, only {len(known)} provided: {known}"
    else:
        if s in unknown:
            if u in unknown:
                u=v-a*t
                print(f"Calculated u = {u}")
                s=u*t+0.5*a*t**2
                print(f"Calculated s = {s}")
            elif v in unknown:
                v=u+a*t
                print(f"Calculated v = {v}")
                s=v*t-0.5*a*t**2
                print(f"Calculated s = {s}")
            elif a in unknown:
                a=(v-u)/t
                print(f"Calculated a = {a}")
                s=u*t+0.5*a*t**2
                print(f"Calculated s = {s}")
            
            elif t in unknown:
                t=(v-u)/a
                print(f"Calculated t = {t}")
                s=u*t+0.5*a*t**2
                print(f"Calculated s = {s}")

            ################################################
        if u in unknown:
            if s in unknown:
                u= v-a*t
                print(f"Calculated u = {u}")
                s=u*t+0.5*a*t**2
                print(f"Calculated s = {s}")
            elif v in unknown:
                u=(s-a*t**2)/(2*t)
                print(f"Calculated u = {u}")
                v=u+a*t
                print(f"Calculated v = {v}")
            elif a in unknown:
                a=-2*(s-u*t)/t**2
                print(f"Calculated a = {a}")
                u=v-a*t
                print(f"Calculated u = {u}")
            elif t in unknown:
                u=(v**2-2*a*s)**0.5
                print(f"Calculated u = {u}")
                t=(v-u)/a
                print(f"Calculated t = {t}")
            ################################################
        if v in unknown:
            if s in unknown:
                v=(u**2+2*a*s)**0.5
                print(f"Calculated v = {v}")
                s=u*t+0.5*a*t**2
                print(f"Calculated s = {s}")
            elif u in unknown:
                u=2*(s-a*t**2)/t
                print(f"Calculated u = {u}")
                v=u+a*t
                print(f"Calculated v = {v}")
            elif a in unknown:
                a=2*(s-u*t)/t**2
                print(f"Calculated a = {a}")
                v=u+a*t
                print(f"Calculated v = {v}")
            elif t in unknown:
                v=(u**2+2*a*s)**0.5
                print(f"Calculated v = {v}")
                t=(v-u)/a
                print(f"Calculated t = {t}")
            ################################################
        if a in unknown:
            if s in unknown:
                a=(v**2-u**2)/(2*s)
                print(f"Calculated a = {a}")
                s=u*t+0.5*a*t**2
                print(f"Calculated s = {s}")
            if u in unknown:
                a=
        if t in unknown:
            if s in unknown:
                t=(-u+(u**2+2*a*s)**0.5)/a
                print(f"Calculated t = {t}")
                s=u*t+0.5*a*t**2
                print(f"Calculated s = {s}")
            if v in unknown:
                v=(u**2 + 2*a*s)**0.5
                print(f"Calculated v = {v}")
                t=(v-u)/a
                print(f"Calculated t = {t}")
            if u in unknown:
                u=(v**2 - 2*a*s)**0.5
                print(f"Calculated u = {u}")
                t=(v-u)/a
                print(f"Calculated t = {t}")
            if a in unknown:
                a=(v**2 - u**2)/(2*s)
                print(f"Calculated a = {a}")
                t=(v-u)/a
                print(f"Calculated t = {t}")
    return s, u, v, a, t
#v=u+at   No S - need v, a, t to find u
#v^2=u^2+2as  No u - need v, a, s to find u
#s=ut+0.5at^2  No v - need u, a, t to find v
#s=vt-0.5at^2  No u - need v, a, t to find u
#t=(v-u)/a  No s - need v, u, a to find t
