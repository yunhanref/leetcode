class Solution:
    def CircleJudge(self, moves:str):
        string = moves.lower()
        y_axis = 0
        x_axis = 0
        unknown = False
        for i in string:
            if i == "u":
                y_axis += 1
            elif i == "d":
                y_axis -= 1
            elif i == "l":
                x_axis -= 1
            elif i == "r":
                x_axis += 1
            else:
                print(f"unknown command {i}")
                unknown = True
                break
        coordinates = [x_axis,y_axis]
        print(coordinates)
        return True if coordinates == [0,0] and not unknown else False
sol = Solution()
print(sol.CircleJudge("UDRL"))



