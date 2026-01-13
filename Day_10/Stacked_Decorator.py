def bold(new):
    def wrapper(): return "<b>" + new() + "</b>"
    return wrapper

def italic(new):
    def wrapper(): return "<i>" + new() + "</i>"
    return wrapper

@bold
@italic
def text(): return "BoldItalic"

@italic
@bold
def text1(): return "ItalicBold"

print(text())
print(text1())