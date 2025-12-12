import json
from task_generator import TaskSetGenerator

generator = TaskSetGenerator(use_dependency=True, use_preemption=True, use_priority=True)
task_set = generator.generate_task_set(5, 6, 8)


print(json.dumps(task_set, indent=4, separators=(',', ': ')))



