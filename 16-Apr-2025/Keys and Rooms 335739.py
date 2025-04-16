# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dq = deque(rooms[0])
        visited = [0 for i in range(len(rooms))]
        visited[0] = 1

        count = 1
        while dq:
            flag = False
            for i in range(len(dq)):
                temp = dq.popleft()
                for i in range(temp):
                    if visited[temp] == 0 :
                        count += 1
                        visited[temp] = 1
                        dq.extend(rooms[temp])
                
                
                # print(dq,visited,count)
        
        return True if count == len(rooms) else False



