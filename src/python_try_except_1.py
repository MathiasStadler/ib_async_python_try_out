import traceback

try:
    # your code goes here
    print("Performing an action which may throw an exception.")
    x = 2/0

except Exception as e:
    # print(e)
    # traceback.print_exc()
    print("error: ",e)
    print("error file info: ",e.__traceback__.tb_frame)
    print("error line#: ",e.__traceback__.tb_lineno)