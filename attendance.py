from functools import lru_cache


class Attendance:
    def __init__(self, total_classes, miss_allowed):
        """
        :param total_classes: the total no of classes that are going to be there
        :param miss_allowed: maximum (consecutive days + 1) allowed to miss
        """
        if total_classes < miss_allowed or total_classes < 0 or miss_allowed < 0:
            raise Exception("Invalid Inputs")
        self.total_classes = total_classes
        self.miss_allowed = miss_allowed

    def calculate_ways_to_attend_classes(self):
        return self._calculate_attendance(self.total_classes, 0)

    def calculate_ways_to_miss_grad_day(self):
        return self._calculate_attendance(self.total_classes - 1, 1)

    @lru_cache(maxsize=None)
    def _calculate_attendance(self, total_classes, missed):
        if self.miss_allowed == missed:
            return 0
        if total_classes == 0:
            return 1
        return self._calculate_attendance(total_classes - 1, 0) + self._calculate_attendance(total_classes - 1,
                                                                                             missed + 1)
