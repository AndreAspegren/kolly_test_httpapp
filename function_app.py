import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    
    name = req.params.get('name')

    if name: 
        return func.HttpResponse(
            f"Testing123 {name}",
            status_code=200
        )
    else: 
        return func.HttpResponse(
            f"Hei du",
        )
