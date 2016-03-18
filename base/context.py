from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from pkas.ui import Interactive, load_kv
from base.ui import PKButton

load_kv('base', 'context.kv')



# TODO: Adapter Pattern for ContextTabs
#  (using factory / recycler)


class ContextTab(PKButton):
  pass
  # def __init__(self, **kwargs):
  #   super().__init__(**kwargs)
    



class ContextTabRow(BoxLayout):
  pass  
  # def __init__(self, **kwargs):
  #   super().__init__(**kwargs)




class ContextView(Interactive, RelativeLayout):
  pass  
  # def __init__(self, **kwargs):
  #   super().__init__(**kwargs)
