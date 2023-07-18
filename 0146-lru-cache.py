''' https://leetcode.com/problems/lru-cache/
'''

class LRU_Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        string = f"key={self.key}, value={self.value},"
        if self.prev is not None:
            string += f" prev_key={self.prev.key}"
        if self.next is not None:
            string += f" next_key={self.next.key}"
        return string

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {} # {key: LRU_Element}
        self.least_used = None
        self.most_used = None

    def get(self, key):
        if key not in self.data:
            return -1
        # Get the data to resurn
        data_to_return = self.data[key]

        # It's the last element, no changes
        if data_to_return.next == None:
            return data_to_return.value

        if data_to_return.prev == None:
            # Adjust least_used
            self.least_used = data_to_return.next
            self.least_used.prev = None
        else:
            # Connect links to fill the gap
            data_to_return.prev.next, data_to_return.next.prev = data_to_return.next, data_to_return.prev

        # And move current element to teh most used
        data_to_return.next = None
        self.most_used.next = data_to_return
        data_to_return.prev = self.most_used
        self.most_used = data_to_return
        return data_to_return.value  

    def put(self, key, value):
        # Key exists: Get it (to bump) and replace value
        if key in self.data:
            self.get(key)
            self.most_used.value = value
        # Add new key
        else:
            element = LRU_Element(key, value)

            # Set up Most used
            if self.most_used is None:
                self.most_used = element
            else:
                element.prev = self.most_used
                self.most_used.next = element
                self.most_used = element

            # Setup Least used
            if self.least_used is None:
                self.least_used = element


            self.data[key] = element
            # Remove one item if needed
            if len(self.data) > self.capacity:
                if self.least_used.next is not None:
                    new_least_used = self.least_used.next
                else:
                    new_least_used = element
                new_least_used.prev = None
                del self.data[self.least_used.key]
                self.least_used = new_least_used


    def __str__(self):
        string = f"LRU of {self.capacity}\n"
        string += "Data:\n"
        for key, value in self.data.items():
            string += f"{key}: {value}\n"
        string += f"least_used: {self.least_used}\n"
        string += f"most_used: {self.most_used}\n"
        return string

def main():
    size = 2
    commands = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
    parameters = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    # size = 3
    # commands = ["put", "put", "put", "get", "get", "get", "put", "put"]
    # parameters = [[1, 1], [2, 2],[3, 3], [2], [1], [3], [1, 4], [10, 10]]


    cache = LRUCache(size)

    for command, parameter in zip(commands, parameters):
        #print(f"{command}({parameter})")
        if command == "put":
            cache.put(parameter[0], parameter[1])
            result = None
        elif command == "get":
            result = cache.get(parameter[0])
        print(f"{command}({parameter}) = {result}")
        #print(cache)



if __name__ == "__main__":
    main()