class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = None
class MyHashMap:
    def hash(self, key):
        return key % 10000
    def __init__(self):
        self.my_map = [ListNode() for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        cur = self.my_map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key=key, val=value)

    def get(self, key: int) -> int:
        cur = self.my_map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.my_map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)