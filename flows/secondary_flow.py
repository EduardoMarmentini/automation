from prefect import flow
from tasks.calculation_task import task_2

@flow(name="secondary_automacao", log_prints=True)
def secondary_flow():
    print("Starting secondary workflow")
    print("-" * 50)
    result = task_2(10, 5)  # Chamando a task_2 com valores diferentes
    print(f"Final result from secondary_flow: {result}")
    print("-" * 50)

if __name__ == "__main__":
    secondary_flow()
