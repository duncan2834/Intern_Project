from src.core.llm.prompts.important_task import ImportantTask

class TaskRegistry:
    def __init__(self):
        self._prompts = {}
        self.register(ImportantTask())
    
    def register(self, task):
        """ Register prompt for each kind of task """
        self._prompts[task.name] = task

    def get_task(self, task_name):
        """ Get task by name """
        return self._prompts[task_name]
    
    def get_all_tasks(self):
        """ Get list of all tasks """
        return list(self._prompts.values())