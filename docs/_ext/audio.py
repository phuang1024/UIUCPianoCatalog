from docutils.parsers.rst import Directive
from docutils import nodes


class AudioDirective(Directive):
    required_arguments = 1
    has_content = True

    def run(self):
        src = self.arguments[0]

        caption_html = ""
        if self.content:
            caption_text = " ".join(self.content)
            caption_html = f"<span class='audio-caption'>{caption_text}</span> "

        html = f"""
        <p class="audio-inline">
          {caption_html}
          <audio controls style="vertical-align: middle;">
            <source src="{src}">
          </audio>
        </p>
        """

        return [nodes.raw('', html, format='html')]


def setup(app):
    app.add_directive("audio", AudioDirective)
