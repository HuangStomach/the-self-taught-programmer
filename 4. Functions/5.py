def c(x):
    try:
        float(x)
    except (ValueError):
        print("Error")