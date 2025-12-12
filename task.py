import random

class Task:
    """Base class for all task types."""
    def __init__(self, name, arrival_time, execution_time, deadline,
                 preemptive=None, priority=None, dependency=None):
        self.name = name
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.deadline = deadline

        # Optional fields
        self.preemptive = preemptive
        self.priority = priority
        self.dependency = dependency if dependency else []

    def to_dict(self):
        """Convert object to dictionary for output."""
        return {
            "arrival_time": self.arrival_time,
            "execution_time": self.execution_time,
            "deadline": self.deadline,
            "preemptive": self.preemptive,
            "priority": self.priority,
            "dependency": self.dependency
        }


class PeriodicTask(Task):
    def __init__(self, name, arrival_time, execution_time, period, deadline,
                 preemptive=None, priority=None, dependency=None):
        super().__init__(name, arrival_time, execution_time, deadline,
                         preemptive, priority, dependency)
        self.period = period

    def to_dict(self):
        d = super().to_dict()
        d["period"] = self.period
        return d


class SporadicTask(Task):
    def __init__(self, name, arrival_time, execution_time, deadline, min_interval,
                 preemptive=None, priority=None, dependency=None):
        super().__init__(name, arrival_time, execution_time, deadline,
                         preemptive, priority, dependency)
        self.min_interval = min_interval

    def to_dict(self):
        d = super().to_dict()
        d["min_interval"] = self.min_interval
        return d


class AperiodicTask(Task):
    pass
