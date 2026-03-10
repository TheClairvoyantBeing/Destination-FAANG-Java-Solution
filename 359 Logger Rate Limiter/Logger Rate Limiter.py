# Leetcode Link: https://leetcode.com/problems/logger-rate-limiter/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design a logger that receives messages with timestamps. shouldPrintMessage returns true
# if the message hasn't been printed in the last 10 seconds.
# ---------- Approach ----------
# Hash map: message -> last print timestamp. Allow if not seen or >= 10 seconds elapsed.
# Time: O(1) | Space: O(n)
class Logger:
    def __init__(self):
        self.msg_dict = {}
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg_dict or timestamp - self.msg_dict[message] >= 10:
            self.msg_dict[message] = timestamp
            return True
        return False
