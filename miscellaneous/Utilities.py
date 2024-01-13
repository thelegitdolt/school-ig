class Utilities:
    def __init__(self, ls):
        self.ls = ls

    def get(self):
        return self.ls

    def even_count(self):
        count = 0
        for i in self.ls:
            if i % 2 == 0:
                count += 1
        return count

    def max_item(self):
        mx = None
        for i in self.ls:
            if mx is None or mx < i:
                mx = i
        return mx

    def sum(self):
        result = 0
        for i in self.ls:
            result += i
        return result

    def mean_value(self):
        return Utilities.sum(self) / len(self)

    def bubble_sort(self, start_at=0):
        if start_at < len(self.ls):
            current = start_at
            while current < len(self.ls):
                if self.ls[start_at] > self.ls[current]:
                    self.ls[start_at], self.ls[current] = self.ls[current], self.ls[start_at]
                current += 1

            self.bubble_sort(start_at + 1)

    def __len__(self):
        return list.__len__(self.ls)




