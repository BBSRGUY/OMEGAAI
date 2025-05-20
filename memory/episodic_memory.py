"""Episodic memory storage placeholder."""

class EpisodicMemory:
    def __init__(self):
        self.events = []

    def store(self, event):
        self.events.append(event)

    def retrieve(self):
        return self.events[-5:]
