import sublime, sublime_plugin

class KeepCenterListener(sublime_plugin.EventListener):
  def on_modified(self, view):
    sel = view.sel()
    if len(sel) is 1 and sel[0].empty():
      view.show_at_center(view.sel()[0].begin())
    