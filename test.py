import gettext

en = gettext.translation('base', localedir='locales', languages=['en'])
en.install()
_ = en.gettext
player = "x"
formatted_text = _("Spieler {player} ist dran!".format(player = "test"))
print(formatted_text)
formatted_text = _("Spieler {player} ist dran!").format(player="Test")

print(formatted_text)