from fastapi import FastAPI
from simulation_platform.tasks.entities.simulation_task import SimulationTask
from simulation_platform.tasks.services.task_use_cases import SimulationTaskUseCases


app = FastAPI()
task_use_cases = SimulationTaskUseCases()


@app.post("/queryTask", response_model=list[SimulationTask])
def query_task():
    return task_use_cases.query_simulation_task()
