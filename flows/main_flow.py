from prefect import flow
from tasks.generation import consult_information

@flow(name="generation_rel_finan", log_prints=True)
def main_fn():
    print("Start workflow")
    print("-" * 50);
    consult_information()
    
if __name__ == "__main__":
    main_fn()