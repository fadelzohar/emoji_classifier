"""

Build New project help you classify text in document as types we created
  ==> types
    // string
    // emoji smile
    // emoji angry
    // emoji happy

"""

"""
Build Item interface for all future types
"""
class Item:
    content: any
    type_id: int

    def __init__(self, content: str):
        self.content = content

    def display(self):
        print(self.content)

    def get_content(self):
        return self.content

    def set_type_id(self, type_id: int):
        self.type_id = type_id
        return self


class ItemText(Item):

    def __init__(self, content: str):
        super().__init__(content)

class ItemEmoji(Item):

    def __init__(self, content: str):
        super().__init__(content)


class Handler:
    next = None

    def handle(self, text: str):
        pass

    def set_next(self, next):
        self.next = next
        return self


class TextMediator:
    item: Item = None

    def set_mediator_type(self, item: Item):
        self.item = item

class EmojiHandler(Handler):
    mediator: TextMediator = None

    def __init__(self, mediator: TextMediator):
        self.mediator = mediator

    def handle(self, text: str):
        if text == "emoji":
            self.mediator.set_mediator_type(ItemEmoji(text))
        elif self.next != None:
            self.next.handle(text)

class TextHandler(Handler):
    mediator: TextMediator = None

    def __init__(self, mediator: TextMediator):
        self.mediator = mediator

    def handle(self, text: str):
        if text != "emoji":
            self.mediator.set_mediator_type(ItemText(text))
        elif self.next != None:
            self.next.handle(text)
            self.mediator.set_mediator_type(None)
class Document(Item):
    items: list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item.set_type_id(self.search_for_right_type_id))

    def remove_item(self, item: Item):
        self.items.remove(item)

    def search_for_type_id(self, index: int):
        for item in self.items:
            if item.type_id == index:
                return True
        return False

    def search_for_right_type_id(self):
        for index in range(1, len(self.item) + 1):
            if self.search_for_type_id(index) == False:
                return index
        return index
