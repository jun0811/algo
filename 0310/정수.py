def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    stack = [begin]
    if target not in words:
        return 0
    else:
        while stack:
            s = stack.pop()
            if s == target:
                break
            for i in range(len(words)):
                # 한개의 알파벳만 다른경우
                cnt = 0
                for j in range(len(words[i])):
                    if words[i][j] != s[j]:
                        cnt += 1
                if cnt == 1:
                    if visited[i] !=0: continue
                    visited[i] = 1
                    stack.append(words[i])
            print(stack)
            answer +=1
                    
    return answer
solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])