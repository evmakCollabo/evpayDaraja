from datetime import datetime

def get_time():
    time_now = datetime.now()
    formatted_time = time_now.strftime("%Y%m%d%H%M%S")
    return formatted_time