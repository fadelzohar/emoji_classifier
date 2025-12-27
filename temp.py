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

