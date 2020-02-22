from boltiot import Bolt

class bolt_custom():
   def __init__(self,api_key=None,device_key=None):
      self.b=None
      if api_key is None and device_key is None:
         print("Non parameterized")
      else :
         self.b = Bolt(api_key,device_key)
