import math


def minimax(curDepth, nodeIndex,maxTurn,scores,targetDepth):


    print('Depth ' , curDepth , 'nodeIndex ' , nodeIndex)
    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        x = minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth)
        y = minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)

        print('Max of  ', x , y  , max(x , y))

        return max(x , y)

    else:
        x = minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth)
        y = minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)

        print('Min of  ', x, y, min(x, y))
        return min(x , y)

scores = [3,5,2,9,12,5,23,23]

height = math.log(len(scores), 2)

print("The optimal value is : ", end="")
print(minimax(0, 0, True, scores, height))