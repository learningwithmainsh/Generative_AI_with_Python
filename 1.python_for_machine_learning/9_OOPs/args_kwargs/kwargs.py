def api_call(endpoint, **kwargs):
    print(f"Calling {endpoint} with Following parameters:")
    for key, value in kwargs.items():
        print(f"{key}:{value}")
api_call("getuser", userid=101, fields="name,email")
api_call("getorder", status="shipped", page=2)