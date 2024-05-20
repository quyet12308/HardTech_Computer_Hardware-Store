from datetime import datetime, timedelta
from pytz import timezone
import datetime

# from datetime import datetime, timedelta
import pytz

# from datetime import timedelta


def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t


def gettime3():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    t = local_time.strftime("%Y_%m_%d")
    return t


def gettime4():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    t = local_time.strftime("%Y-%m-%d")
    return t


def convert_utc_to_utc7(utc_time):
    # Chuyển chuỗi thời gian UTC thành đối tượng datetime
    datetime_utc = datetime.datetime.strptime(utc_time, "%Y-%m-%d %H:%M:%S")

    # Tạo một đối tượng timedelta đại diện cho sự chênh lệch giữa UTC và UTC+7
    utc_offset = timedelta(hours=7)

    # Chuyển đổi thời gian từ UTC sang UTC+7
    datetime_utc7 = datetime_utc + utc_offset

    # Định dạng lại chuỗi thời gian theo định dạng "%Y-%m-%d %H:%M:%S"
    utc7_time = datetime_utc7.strftime("%Y-%m-%d %H:%M:%S")

    return utc7_time


def add_time_to_datetime(datetime_str=None, days=0, hours=0, minutes=0, seconds=0):
    if days == 0 and hours == 0 and minutes == 0 and seconds == 0:
        return {
            "status": False,
            "message": "Nhập vào ít nhất 1 tham số thời gian để cộng",
        }

    if datetime_str is None:
        dt = datetime.datetime.now()  # Lấy thời gian hiện tại
    else:
        try:
            dt = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return {
                "status": False,
                "message": "Định dạng chuỗi thời gian không chính xác",
            }

    delta = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    new_dt = dt + delta
    new_datetime_str = new_dt.strftime("%Y-%m-%d %H:%M:%S")

    return {"status": True, "message": new_datetime_str}


def convert_to_datetime(time_string):
    datetime_object = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
    return datetime_object


# def check_time_range(created_time, now_time, minute):
#     # Chuyển đổi chuỗi thời gian thành đối tượng datetime
#     created_datetime = datetime.datetime.strptime(created_time, "%Y-%m-%d %H:%M:%S")
#     now_datetime = datetime.datetime.strptime(now_time, "%Y-%m-%d %H:%M:%S")

#     # Tính toán khoảng thời gian giữa hai thời điểm
#     time_difference = now_datetime - created_datetime

#     # Chuyển đổi số phút thành đối tượng timedelta
#     minute_delta = datetime.timedelta(minutes=minute)


#     # So sánh khoảng thời gian với tham số phút
#     if time_difference >= minute_delta:
#         return False
#     else:
#         return True
def check_time_range(created_time, now_time, minute):
    try:
        # Chuyển đổi chuỗi thời gian thành đối tượng datetime
        created_datetime = datetime.datetime.strptime(created_time, "%Y-%m-%d %H:%M:%S")
        now_datetime = datetime.datetime.strptime(now_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return "format false"
        # raise ValueError("Định dạng thời gian không hợp lệ")

    # Tính toán khoảng thời gian giữa hai thời điểm
    time_difference = now_datetime - created_datetime

    # Chuyển đổi số phút thành đối tượng timedelta
    minute_delta = datetime.timedelta(minutes=minute)

    # So sánh khoảng thời gian với tham số phút
    if time_difference >= minute_delta:
        return False
    else:
        return True


def check_time_range2(date1, date2, days):
    # Chuyển đổi hai chuỗi thời gian thành đối tượng datetime
    date1_obj = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2_obj = datetime.datetime.strptime(date2, "%Y-%m-%d")

    # Tính khoảng thời gian giữa hai ngày
    time_delta = date2_obj - date1_obj

    # Kiểm tra xem khoảng thời gian có vượt quá 3 ngày hay không
    if time_delta > timedelta(days=days):
        return True
    else:
        return False


# a = check_time_range2(date1="2023-11-01",date2="2023-11-03",days=3)
# print(a)


def check_availability(time1, time2, days):
    # Chuyển đổi chuỗi thời gian thành đối tượng datetime
    time1 = datetime.datetime.strptime(time1, "%Y-%m-%d")
    time2 = datetime.datetime.strptime(time2, "%Y-%m-%d")

    # Tính toán thời gian kết thúc (time1 + days)
    end_time = time1 + timedelta(days=days)

    # Kiểm tra nếu time2 nằm ngoài phạm vi time1 + days
    if time2 < time1 or time2 > end_time:
        return True
    else:
        return False


# a = check_availability(time1="2023-11-01",time2="2023-11-05",days=3)
# print(a)

# created_time = "2023-09-14 10:01:00"
# now_time = "2023-09-14 10:04:59"
# minute = 3

# result = check_time_range(created_time, now_time, minute)
# print(result)  # True nếu khoảng thời gian không vượt qua tham số minute, False nếu vượt qua

# print(gettime3())


# expected_timezone = timezone("Asia/Ho_Chi_Minh")
# current_timezone = timezone("2024-03-24 23:13:32")
# print(current_timezone)

# datetime_str = "2024-05-19 10:30:00"
# # new_datetime_str = add_time_to_datetime(datetime_str, hours=2, minutes=30)
# new_datetime_str = add_time_to_datetime(
#     datetime_str,
# )
# print(new_datetime_str)

# result = add_time_to_datetime(hours=2)
# print(result)

# utc_time = "2024-05-20 08:30:00"
# utc7_time = convert_utc_to_utc7(utc_time)
# print(utc7_time)
