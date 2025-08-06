from src.core.llm.prompts.base_prompt import BasePrompt

class TaskRegistry:
    def __init__(self):
        self._prompts = BasePrompt.registry

    def get_task(self, task_name):
        """ Get task by name """
        if not task_name or not task_name.strip():
            raise ValueError("Task name can not be empty")
        if task_name not in self._prompts:
            raise ValueError(f"Task {task_name} is not registered")
        return self._prompts[task_name]
    
    def get_all_tasks(self):
        """ Get list of all tasks """
        return list(self._prompts.values())