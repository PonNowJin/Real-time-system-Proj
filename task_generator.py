from task import PeriodicTask, SporadicTask, AperiodicTask
import random

class TaskSetGenerator:
    def __init__(
        self,
        use_preemption=False,
        use_priority=False,
        use_dependency=False
    ):
        self.use_preemption = use_preemption
        self.use_priority = use_priority
        self.use_dependency = use_dependency
        
        self.all_task_names = []

    # -------------------------
    # helper: advance options
    # -------------------------
    def _add_optional_fields(self, all_task_names):
        preemptive = None
        priority = None
        dependencies = []

        # Preemption
        if self.use_preemption:
            preemptive = random.choice([True, False])

        # Priority
        if self.use_priority:
            priority = random.randint(1, 10)

        # Dependency (0 ~ 2 個)
        if self.use_dependency and all_task_names:

            # 20% 機率有依賴
            if random.random() < 0.2:
                dep_count = random.randint(1, min(2, len(all_task_names)))

                # 隨機挑選多個不同的依賴項
                dependencies = random.sample(all_task_names, dep_count)

        return preemptive, priority, dependencies



    # -------------------------
    # generate periodic tasks
    # -------------------------
    def generate_periodic(self, n):
        tasks = {}

        for i in range(1, n+1):
            name = f"p{i}"
            self.all_task_names.append(name)
            
            arrival = random.randint(0, 50)
            exec_time = random.randint(1, 5)
            period = period = random.randint(5, 25)
            deadline = random.randint(exec_time + 1, period)

            preemptive, priority, dep = self._add_optional_fields(self.all_task_names[:-1])

            t = PeriodicTask(
                name, arrival, exec_time, period, deadline,
                preemptive, priority, dep
            )
            tasks[name] = t.to_dict()

        return tasks

    # -------------------------
    # generate sporadic tasks
    # -------------------------
    def generate_sporadic(self, n):
        tasks = {}

        for i in range(1, n+1):
            name = f"s{i}"
            self.all_task_names.append(name)

            arrival = random.randint(0, 50)
            exec_time = random.randint(1, 5)
            deadline = arrival + random.randint(exec_time + 5, 20)
            interval = random.randint(5, 12)

            preemptive, priority, dep = self._add_optional_fields(self.all_task_names[:-1])

            t = SporadicTask(
                name, arrival, exec_time, deadline, interval,
                preemptive, priority, dep
            )
            tasks[name] = t.to_dict()

        return tasks

    # -------------------------
    # generate aperiodic tasks
    # -------------------------
    def generate_aperiodic(self, n):
        tasks = {}

        for i in range(1, n+1):
            name = f"a{i}"
            self.all_task_names.append(name)

            arrival = random.randint(0, 50)
            exec_time = random.randint(1, 5)
            deadline = arrival + random.randint(exec_time + 5, 30)

            preemptive, priority, dep = self._add_optional_fields(self.all_task_names[:-1])

            t = AperiodicTask(
                name, arrival, exec_time, deadline,
                preemptive, priority, dep
            )
            tasks[name] = t.to_dict()

        return tasks

    # --------------------------------
    # generate FULL task set
    # --------------------------------
    def generate_task_set(self, np=3, ns=2, na=2):
        return {
            "periodic": self.generate_periodic(np),
            "sporadic": self.generate_sporadic(ns),
            "aperiodic": self.generate_aperiodic(na)
        }
