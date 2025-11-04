def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    mapping_s, mapping_t = {}, {}
    for c1, c2 in zip(s, t):
        if mapping_s.get(c1, c2) != c2 or mapping_t.get(c2, c1) != c1:
            return False
        mapping_s[c1] = c2
        mapping_t[c2] = c1
    return True

print(is_isomorphic("egg", "add"))  # True
print(is_isomorphic("foo", "bar"))  # False
