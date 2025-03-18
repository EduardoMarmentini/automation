from prefect import flow, task


@task(name="say-hello", log_prints=True)
def task_1():
    val1 = 1
    val2 = 2
    print("Hello, this is my first task, it says Hello")
    task_2(val1, val2)

@task(name="calc-value", log_prints=True)
def task_2(a, b):
    result = a + b
    print(f"Sum result: {result}")
    return result

@flow(name="automacao", log_prints=True)
def main_fn():
    print("Start workflow")
    
    print(f"Final result from task_2: {task_1()}")

if __name__ == "__main__":
    main_fn()
