from fastapi.responses import JSONResponse

def make_response(status_code, results):
    response = {
        'code': status_code,
        'results': results
    }
    return JSONResponse(status_code=status_code, content=response)

def make_error(status_code, sub_code, error):
    response = {
        'meta': {
            'code': status_code,
            'sub_code': sub_code,
            'message': error
        }
    }
    return JSONResponse(status_code=status_code, content=response)
