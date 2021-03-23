from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import Dimension, HSplit, Layout, ScrollablePane
from prompt_toolkit.widgets import Frame, Label, TextArea

import user

my_user = user.User("madaspe")

repos = my_user.user.get_repos()
repos_name = []

for rep in repos:
    repos_name.append(Frame(TextArea(text=rep.full_name, width=Dimension())))

root_container = Frame(
        ScrollablePane(
            HSplit(
                repos_name
                )
            )
    )

layout = Layout(container=root_container)

kb = KeyBindings()

@kb.add("c-c")
def exit(event):
    get_app().exit()


kb.add("tab")(focus_next)
kb.add("s-tab")(focus_previous)

application = Application(layout=layout, key_bindings=kb, full_screen=True)
application.run()



