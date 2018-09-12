#!/usr/bin/env python3

class LinkedList:
    def _init_(self):
        self.nodes = []

    def append(self, node):
        self.nodes.append(node)

    def get(self, value):
        for node in self.nodes:
            if node.get() == value:
                return node

        return None

class Node:
    def _init_(self, value, next=None):
        self.value = value
        self.next = next

    def get(self):
        return self.value

    def next_node(self):
        return self.next
