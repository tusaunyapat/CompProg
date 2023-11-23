def reverse(d):
    r = {}
    for key in d:
        value = d[key]
        r[value] = key
    return r

def keys(d, v):
    ans = []
    for key in d:
        if d[key] == v:
            ans.append(key)
    return ans

exec(input().strip())