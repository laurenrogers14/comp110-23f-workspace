"""Class to store a message (operator overload, union types, default parameters)."""

class Message:

    to: str
    content: str
    important: bool

    def __init__(self, recipient: str, message_content: str, importance_flag: bool):
        """Constructor."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    def __str__(self) -> str:
        output: str =f"Message to {self.to}:\n"
        output += f"Important? {self.important}:\n"
        output += f'"{self.content}"'
        return output

    def __mul__ (self, factor: int): # returns nothing because we are modifying an existing object
        """Multiplication operator overload."""
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + copy_val


msg: Message = Message("erin", "Great job!", False)
msg * 1000
msg_to_myself: Message = Message("me", "Dp your 110 homework!", True)
print(f"My message is {msg}")
print(msg)
