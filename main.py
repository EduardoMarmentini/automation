from prefect import flow, task

val1 = 1
val2 = 2

@task(name="say-hello", log_prints=True)
def task_1():
    print("Hello, this is my first task, it says Hello")

@task(name="calc-value", log_prints=True)
def task_2(a, b):
    result = a + b
    print(f"Sum result: {result}")
    return result

@flow(name="my-first-flow", log_prints=True)
def main_fn():
    print("Start workflow")
    
    task_1()
    result = task_2(val1, val2)  

    print(f"Final result from task_2: {result}")

if __name__ == "__main__":
    main_fn()
