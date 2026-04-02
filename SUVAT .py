#s, u, v, a, t = None, None, None, None, None
rounding = 4
class distance:
  def __init__(self, value=0):
    self.value = value
    s=0
  def u(self, v, a, t, u=None):
    # s = ut + 0.5at² (excludes v)
    s = round(v*t - 0.5*a*t**2,rounding)
    u = round(v - a*t,rounding)
    self.value = s
    return f"s = {s}, u = {u}"
  def v(self, u, a, t, v=None):
    # s = ut + 0.5at² (excludes v)
    s = round(u*t + 0.5*a*t**2,rounding)
    v = round(u + a*t,rounding)
    self.value = s
    return f"s = {s}, v = {v}"
  def a(self, u, v, t, a=None):
    # s = (u + v)/2 * t (excludes a)
    s = round((u + v) * t / 2,rounding)
    a = (v - u) / t
    self.value = s
    return f"s = {s}, a = {a}"
  def t(self, u, v, a, t=None):
    # s = (v² - u²)/(2a) (excludes t)
    s = round((v**2 - u**2) / (2 * a),rounding)
    t = round((v - u) / a,rounding)
    self.value = s
    return f"s = {s}, t = {t}"

class initial_velocity:
  def __init__(self, value=0):
    self.value = value
    u=0
  def s(self, v, a, t, s=None):
    # u = v - at (excludes s)
    u = round(v - a*t, rounding)
    s = round(u*t + 0.5*a*t**2, rounding)
    self.value = u
    return f"u = {u}, s = {s}"
  def v(self, s, a, t, v=None):
    # u = (s - 0.5at²)/t (excludes v)
    u = round((s - 0.5*a*t**2) / t, rounding)
    v = round(u + a*t,rounding)
    self.value = u
    return f"u = {u}, v = {v}"
  def a(self, s, v, t, a=None):
    # u = (2s - vt)/t (excludes a)
    u = round((2*s - v*t) / t, rounding)
    a = round((v - u) / t, rounding)
    self.value = u
    return f"u = {u}, a = {a}"
  def t(self, s, v, a, t=None):
    # u = v - at (excludes s)
    # Using v² = u² + 2as to find t
    u = round((v**2 - 2*a*s)**0.5, rounding)
    t = round((v - u) / a,rounding)
    self.value = u
    return f"u = {u}, t = {t}"

class final_velocity:
  def __init__(self, value=0):
    self.value = value
    v=0
  def s(self, u, a, t, s=None):
    # v = u + at (excludes s)
    v = round(u + a*t,rounding)
    s = round(u*t + 0.5*a*t**2, rounding)
    self.value = v
    return f"v = {v}, s = {s}"
  def u(self, s, a, t, u=None):
    # v = (s + 0.5at²)/t (excludes u)
    v = round((s + 0.5*a*t**2) / t, rounding)
    u = round(v - a*t, rounding)
    self.value = v
    return f"v = {v}, u = {u}"
  def a(self, s, u, t, a=None):
    # v = (2s - ut)/t (excludes a)
    v = round((2*s - u*t) / t, rounding)
    a = round((v - u) / t, rounding)
    self.value = v
    return f"v = {v}, a = {a}"
  def t(self, s, u, a, t=None):
    # v = √(u² + 2as) (excludes t)
    v = round((u**2 + 2*a*s)**0.5, rounding)
    t = round((v - u) / a,rounding)
    self.value = v
    return f"v = {v}, t = {t}"

class acceleration:
  def __init__(self, value=0):
    self.value = value
    a=0
  def s(self, u, v, t, s=None):
    # a = (v - u)/t (excludes s)
    a = round((v - u) / t, rounding)
    s = round((u + v) * t / 2, rounding)
    self.value = a
    return f"a = {a}, s = {s}"
  def u(self, s, v, t, u=None):
    # a = 2(s - vt)/t² (excludes u)
    a = round(2 * (s - v*t) / t**2, rounding)
    u = round(v - a*t, rounding)
    self.value = a
    return f"a = {a}, u = {u}"
  def v(self, s, u, t, v=None):
    # a = 2(s - ut)/t² (excludes v)
    a = round(2 * (s - u*t) / t**2, rounding)
    v = round(u + a*t,rounding)
    self.value = a
    return f"a = {a}, v = {v}"
  def t(self, s, u, v, t=None):
    # a = (v² - u²)/(2s) (excludes t)
    a = round((v**2 - u**2) / (2 * s),rounding)
    t = round((v - u) / a,rounding)
    self.value = a
    return f"a = {a}, t = {t}"

class time:
  def __init__(self, value=0):
    self.value = value
    t=0
  def s(self, u, v, a, s=None):
    # t = (v - u)/a (excludes s)
    t = round((v - u) / a, rounding)
    s = round((v**2 - u**2) / (2 * a), rounding)
    self.value = t
    return f"t = {t}, s = {s}"    
  def u(self, s, v, a, u=None):
    # t = (v - u)/a (excludes s)
    # Using v² = u² + 2as to find u
    u = round((v**2 - 2*a*s)**0.5, rounding)
    t = round((v - u) / a,rounding)
    self.value = t
    return f"t = {t}, u = {u}"
  def v(self, s, u, a, v=None):
    # t = (v - u)/a (excludes s)
    # Using v² = u² + 2as to find v
    v = round((u**2 + 2*a*s)**0.5,rounding)
    t = round((v - u) / a,rounding)
    self.value = t
    return f"t = {t}, v = {v}"
  def a(self, s, u, v, a=None):
    # t = 2s/(u + v) (excludes a)
    t = round((2 * s) / (u + v),rounding)
    a = round((v**2 - u**2) / (2 * s),rounding)
    self.value = t
    return f"t = {t}, a = {a}"



def isNotNone(value):
    return value is not None

def solve_motion(s=None, u=None, v=None, a=None, t=None):
    unknown = [s, u, v, a, t]
    unknown_two = unknown.copy()
    known = []
    for i in unknown_two:
        if isNotNone(i):
            known.append(i)
            unknown.remove(i)
    if len(known) != 3:
      return "Please input exactly 3 variables, no more no less"
    if t != None:
      if t==0:
        return "Time cannot be zero"
      if t <0:
        return "Time cannot be negative"
    if s in unknown:
      dis = distance()
      if u in unknown:
        return dis.u(v, a, t)
      if v in unknown:
        return dis.v(u, a, t)
      if a in unknown:
        return dis.a(u, v, t)
      if t in unknown:
        return dis.t(u, v, a)
    if u in unknown:
      init = initial_velocity()
      if s in unknown:
        return init.s(v,a,t)
      if v in unknown:
        return init.v(s,a,t)
      if a in unknown:
        return init.a(s,v,t)
      if t in unknown:
        return init.t(s,v,a) 
    if v in unknown:
      final = final_velocity()
      if s in unknown:
        return final.s(u,a,t)
      if u in unknown:
        return final.u(s,a,t)
      if a in unknown:
        return final.a(s,u,t)
      if t in unknown:
        return final.t(s,u,a)
    if a in unknown:
      accel = acceleration()
      if s in unknown:
        return accel.s(u,v,t)
      if u in unknown:
        return accel.u(s,v,t)
      if t in unknown:
        return accel.t(s,u,v)
      if v in unknown:
        return accel.v(s,u,t)
    if t in unknown:
      ti = time()
      if s in unknown:
        return ti.s(u,v,a)
      if u in unknown:
        return ti.u(s,v,a)
      if v in unknown:
        return ti.v(s,u,a)
      if a in unknown:
        return ti.a(s,u,v)

#print(solve_motion(s=50,v=6,t=13))   
"""
def solve_u(s,v,a,t):
  solve_motion(s,None,v,a,t)
def solve_s(u,v,a,t):
  solve_motion(None,u,v,a,t)
def solve_v(s,u,a,t):
  solve_motion(s,u,None,a,t)
def solve_a(s,u,v,t):
  solve_motion(s,u,v,None,t)
def solve_t(s,u,v,a):
  solve_motion(s,u,v,a,None)


print(solve_u(32,2,12,None))
"""
