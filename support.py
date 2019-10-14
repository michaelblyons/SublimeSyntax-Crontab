import sublime
import sublime_plugin


class HighlightCronRegions(sublime_plugin.ViewEventListener):

    SYNTAX = 'crontab.sublime-syntax'

    @classmethod
    def is_applicable(cls, settings):
        try:
            return (settings and
                    settings.get('syntax', '').lower().endswith(cls.SYNTAX))
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

    def on_load(self):
        self.highlight_cron()

    def on_hover(self, point, hover_zone):
        meta_scope = 'meta.string.cron-expression'

        if ((hover_zone != sublime.HOVER_TEXT or not
             self.view.match_selector(point, meta_scope))):
            return

        expression_region = [r for r in self.view.find_by_selector(meta_scope)
                             if r.contains(point)][0]
        cron_text = self.view.substr(expression_region)

        try:
            # lazy load this package since it may not be needed
            # additionally, in case of issues with it, we still get
            # the rest of the functionality
            from .cron_descriptor import cron_descriptor
            cron_explanation = cron_descriptor.get_description(cron_text)
        except ImportError:
            cron_explanation = "Error with cron-descriptor package"
        except Exception as e:
            cron_explanation = 'Could not parse cron expression'

        html = '''
            <body id="explain-cron">
                <div>{}</div>
            </body>
        '''.format(cron_explanation)

        self.view.show_popup(html, sublime.HIDE_ON_MOUSE_MOVE_AWAY,
                             location=point, max_width=512, max_height=60)
