from fastapi import FastAPI
from sql_query import question_1, question_2, question_3, question_4, question_5
from maps_data.DigitalHunter_map import plot_map_with_geometry


app = FastAPI()


@app.get("/Priority")
def query1():
    return question_1()


@app.get("/Analysis-of-collection sources")
def query2():
    return question_2()


@app.get("/Finding-new-targets")
def query3():
    return question_2()


@app.get("/Identifying-awakened-sleeping-cells")
def query4():
    return question_3()


@app.get("/Visualization-of-a-target-trajectory:")
def vizual(func):
    func = plot_map_with_geometry(question_5())
    return func
