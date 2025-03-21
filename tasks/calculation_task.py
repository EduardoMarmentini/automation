from prefect import task

@task(name="say-hello", log_prints=True)
def task_1():
    val1 = 1
    val2 = 2
    print("Hello, this is my first task, it says Hello")
    print("-" * 50)
    return task_2(val1, val2)  # Retorna o resultado

@task(name="calc-value", log_prints=True)
def task_2(a, b):
    result = a + b
    print(f"Sum result: {result}")
    print("-" * 50)
    return result