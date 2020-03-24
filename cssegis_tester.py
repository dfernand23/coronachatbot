from coronachatbot.daq.data import CSSE

data = CSSE()

slice = data.time_slice('1/22/20', 5)

print(slice)

