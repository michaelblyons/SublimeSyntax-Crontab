import sublime
import sublime_plugin


class HighlightCronRegions(sublime_plugin.ViewEventListener):

    SYNTAX = 'Crontab.sublime-syntax'

    @classmethod
    def is_applicable(cls, settings):
        try:
            return settings and cls.SYNTAX in settings.get('syntax', '')
        except Exception as e:
            return False

    def highlight_cron_part(self, cron_part, scope):
        self.view.add_regions(
            'cron.' + cron_part,
            self.view.find_by_selector('meta.sequence.cron.' + cron_part),
            scope,
            flags=(
                sublime.DRAW_SOLID_UNDERLINE |
                sublime.HIDE_ON_MINIMAP |
                sublime.DRAW_NO_FILL |
                sublime.DRAW_NO_OUTLINE
            )
        )

    def highlight_cron(self):
        self.highlight_cron_part('minute', 'region.redish')
        self.highlight_cron_part('hour', 'region.greenish')
        self.highlight_cron_part('day-of-month', 'region.orangish')
        self.highlight_cron_part('month', 'region.bluish')
        self.highlight_cron_part('day-of-week', 'region.yellowish')

    def on_modified_async(self):
        self.highlight_cron()

    def on_load_async(self):
        self.highlight_cron()
