from __future__ import annotations

import sublime
from sublime_plugin import ViewEventListener


class HighlightCronRegions(ViewEventListener):

    SYNTAX_ENDING: str = 'Crontab.sublime-syntax'
    SETTINGS_FILE: str = 'Crontab.sublime-settings'

    @classmethod
    def is_applicable(cls, settings: sublime.Settings) -> bool:
        try:
            syntax = settings.get('syntax')
            return (isinstance(syntax, str)
                    and syntax.endswith(cls.SYNTAX_ENDING))
        except Exception:
            return False

    def highlight_cron_part(self, cron_part: str, scope: str) -> None:
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
        settings = sublime.load_settings(self.SETTINGS_FILE)
        color_map: dict[str, str] = settings.get('cron_highlight_colors')
        for cron_part, scope in color_map.items():
            self.highlight_cron_part(cron_part, scope)

    def on_modified_async(self):
        if sublime.load_settings(self.SETTINGS_FILE).get(
                'cron_highlight_enabled'):
            self.highlight_cron()

    def on_load_async(self):
        if sublime.load_settings(self.SETTINGS_FILE).get(
                'cron_highlight_enabled'):
            self.highlight_cron()

    def on_hover(self, point: int, hover_zone: sublime.HoverZone):
        meta_scope = 'meta.string.cron-expression'

        if ((hover_zone != sublime.HOVER_TEXT or not
             self.view.match_selector(point, meta_scope))):
            return

        expression_region = [r for r in self.view.find_by_selector(meta_scope)
                             if r.contains(point)][0]
        cron_text = self.view.substr(expression_region)

        try:
            # Lazy load this package, since it may not be needed.
            # Additionally, in case of issues with it, we still get
            # the rest of the functionality.
            from .cron_descriptor import cron_descriptor
            cron_explanation: str = cron_descriptor.get_description(cron_text)
        except ImportError:
            cron_explanation = "Error with cron-descriptor package"
        except Exception:
            cron_explanation = 'Could not parse cron expression'

        html = '''
            <body id="explain-cron">
                <div>{}</div>
            </body>
        '''.format(cron_explanation)

        self.view.show_popup(html, sublime.HIDE_ON_MOUSE_MOVE_AWAY,
                             location=point, max_width=512, max_height=60)
