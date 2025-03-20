from prefect import flow
from tasks.calculation_task import task_1

@flow(name="automacao", log_prints=True)
def main_fn():
    print("Start workflow")
    result = task_1()
    print(f"Final result from task_2: {result}")

if __name__ == "__main__":
    main_fn()