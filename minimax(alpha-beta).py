import math


def minimax(curDepth, nodeIndex,maxTurn,scores,targetDepth , alpha , beta):


    print('Depth ' , curDepth , 'nodeIndex ' , nodeIndex)
    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        best = -10000

        for i in range (0 , 2):
            best = max(best , minimax(curDepth + 1, nodeIndex * 2 + i, False, scores, targetDepth , alpha , beta))
            alpha = max(best, alpha);
            if beta <= alpha:
                return best
        return  best

    else:
        best = 10000

        for k in range(0, 2):
            best = min(best, minimax(curDepth + 1, nodeIndex * 2 + k, True, scores, targetDepth, alpha, beta))
            beta = min(best , beta);
            if beta <= alpha:
                return best
        return best


alpha = -10000
beta = 10000

scores = [3,5,2,9,12,5,23,23]

height = math.log(len(scores), 2)

print("The optimal value is : ", end="")
print(minimax(0, 0, True, scores, height , alpha , beta))