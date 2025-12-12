import json
from task_generator import TaskSetGenerator

generator = TaskSetGenerator(use_dependency=False, use_preemption=False, use_priority=False)
task_set = generator.generate_task_set(5, 6, 8)


print(json.dumps(task_set, indent=4))


