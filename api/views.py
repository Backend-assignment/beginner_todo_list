
from django.http import HttpResponse, JsonResponse,HttpRequest
# Create your views here.
def get_all_task(request:HttpRequest):
    """
    Get all task

    Args:
        request (HttpRequest): Get request

    Returns:
        JsonRespones: List of all task
    """
    pass

def get_task(request:HttpRequest, id:int):
    """
    Get task by id

    Args:
        request (HttpRequest): Get request
        id (int): Task id

    Returns:
        JsonRespones: Task
    """
    pass

def create_task(request:HttpRequest):
    """
    Create task

    Args:
        request (HttpRequest): Post request

    Returns:
        JsonRespones: Task
    """
    pass

def update_task(request:HttpRequest, id:int):
    """
    Update task

    Args:
        request (HttpRequest): POST request
        id (int): Task id

    Returns:
        JsonRespones: Task
    """
    pass


def delete_task(request:HttpRequest, id:int):
    """
    Delete task

    Args:
        request (HttpRequest): GET request
        id (int): Task id

    Returns:
        JsonRespones: Task
    """
    pass


def get_all_completed_task(request:HttpRequest):
    """
    Get all completed task

    Args:
        request (HttpRequest): Get request

    Returns:
        JsonRespones: List of all completed task
    """
    pass

def get_all_incompleted_task(request:HttpRequest):
    """
    Get all incompleted task

    Args:
        request (HttpRequest): Get request

    Returns:
        JsonRespones: List of all incompleted task
    """
    pass

def complete_task(request:HttpRequest, id:int):
    """
    Complete task

    Args:
        request (HttpRequest): GET request
        id (int): Task id

    Returns:
        JsonRespones: Task
    """
    pass
