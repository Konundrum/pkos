from kivy.config import Config
Config.set('kivy', 'exit_on_escape', 0)

from pkas.app import PKApp
from base.root import PKOSRoot



class PKOS(PKApp):
  

  def build(self):
    return PKOSRoot()
    
    
    
  def build_config(self, config):
    config.setdefaults('keybinds', {
      'left': '["a", "left"]',
      'right': '["d", "right"]',
      'up': '["w", "up"]',
      'down': '["s", "down"]',
      'toggle_overlay': '["`"]',
      'select': '["space"]',
      'delve': '["e", "enter"]',
      'ascend': '["q", "shift enter"]',
      'toggle_menu' : '["escape"]',

      'tab' : '["ctrl tab", "ctrl pagedown"]',
      'untab' : '["ctrl shift tab", "ctrl pageup"]',
      'close_tab' : '["ctrl w"]',
      'new_tab' : '["ctrl t"]',
      'shift_up' : '["ctrl shift pageup"]',
      'shift_down' : '["ctrl shift pagedown"]',

    })



if __name__ == '__main__':
  app = PKOS()
  app.run()
  