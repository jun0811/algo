n = int(input())

times = [input() for _ in range(n)]
times.sort()
s_hour = times[n-1][:2]
s_min = times[n-1][3:5]
end_hour = int(times[0][8:10])
end_min = int(times[0][11:]) 

start = []
end = []
for time in times:
    start.append(time[:5])
    end.append(time[8:])
if max(start) > min(end):
    print(-1)
else:
    print("{} ~ {}".format(str(max(start)),str(min(end))))

