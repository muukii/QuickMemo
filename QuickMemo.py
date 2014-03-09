import sublime, sublime_plugin, os,time
from datetime import datetime as dt


class QuickMemoCommand(sublime_plugin.WindowCommand):
    def run(self):
        settings = sublime.load_settings("QuickMemo.sublime-settings")
        save_dir_path = settings.get("memo_directory")

        tdatetime = dt.now()
        tstr = tdatetime.strftime('%Y-%m-%d-%H%M')
        file_name = save_dir_path + tstr + '.md'
        print('touch ' + file_name)
        os.system('touch ' + file_name)
        new_file_View = self.window.open_file(file_name)
        self.window.focus_view(new_file_View)
        print (new_file_View.settings().get('syntax'))



