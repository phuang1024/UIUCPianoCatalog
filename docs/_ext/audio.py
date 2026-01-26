from docutils.parsers.rst import Directive
from docutils import nodes


class AudioDirective(Directive):
    required_arguments = 1

    def run(self):
        src = self.arguments[0]
        html = f"""
        <audio controls>
          <source src="{src}">
        </audio>
        """
        return [nodes.raw('', html, format='html')]


def setup(app):
    app.add_directive("audio", AudioDirective)
