# Python program to test
# internet speed

import speedtest


st = speedtest.Speedtest()

print('{:.2f}'.format(st.download() / 1024 / 1024))