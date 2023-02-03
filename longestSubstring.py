def LongestSubstring(str):
    ambassadors = []
    times = 0
    for i in str:
        if i not in ambassadors:
            ambassadors.append(i)
            times += 1

    print(times)

LongestSubstring("pwwkew")
