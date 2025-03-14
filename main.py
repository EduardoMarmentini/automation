from prefect import flow, task


@flow(name="trabalhehome", log_prints=True)
def main_fn():
    print("Abra cadraba")
    task_1()

    @task(name="fumabeck", log_prints=True)
    def task_2():
        print("Segunda tarefa, fuma o beck")

    task_2()

@task(name="bolabeck", log_prints=True)
def task_1():
    print("Primeira tarefa, bola o beck")


if __name__ == "__main__":
    main_fn()