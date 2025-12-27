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



