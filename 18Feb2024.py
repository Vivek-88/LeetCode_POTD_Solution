from ast import List


class Solution:
    def mostBooked(self, m: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        n = len(meetings)
        room = [[0, 0] for _ in range(m)]

        for meet in meetings:
            idx = -1
            for i in range(m):
                if room[i][0] <= meet[0]:
                    idx = i
                    break
                else:
                    if idx == -1 or room[i][0] < room[idx][0]:
                        idx = i
            room[idx][0] = max(meet[1], room[idx][0] + (meet[1] - meet[0]))
            room[idx][1] += 1

        ans = 0
        # print(room)
        for i in range(1, m):
            if room[i][1] > room[ans][1]:
                ans = i
        return ans