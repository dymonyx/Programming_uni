def countdown(func):
    import time
    def wrapped(*args, **kwargs):  # зачем??
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time taken to ordering is {round(end - start, 2)}sec.")

    return wrapped