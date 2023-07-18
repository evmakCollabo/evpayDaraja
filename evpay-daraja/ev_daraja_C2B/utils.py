from datetime import datetime

def get_time():
    time_now = datetime.now()
    formatted_time = time_now.strftime("%Y%m%d%H%M%S")
    print(formatted_time)
    return formatted_time
get_time()