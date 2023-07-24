def compare_versions(ver_a, ver_b):
    components_a = list(map(int, ver_a.split('.')))
    components_b = list(map(int, ver_b.split('.')))

    for a, b in zip(components_a, components_b):
        if a > b:
            return 1
        elif a < b:
            return -1

    if len(components_a) > len(components_b):
        return 1
    elif len(components_a) < len(components_b):
        return -1

    return 0

print(compare_versions('1.10', '1.1'))
print(compare_versions("2.4.2", "2.4.2"))
print(compare_versions("0.8.5", "1.0.0"))
