def format_duration(seconds):
    def get_by_unit(seconds, unit_name, unit, next_unit):
        value = (seconds // unit) % next_unit
        if value == 0:
            return []
        elif value == 1:
            return [str(value) + ' ' + unit_name]
        else:
            return [str(value) + ' ' + unit_name + 's']

    if seconds == 0:
        return 'now'

    list = []
    list.extend(get_by_unit(seconds, 'second', 1, 60))
    list.extend(get_by_unit(seconds, 'minute', 60, 60))
    list.extend(get_by_unit(seconds, 'hour', 60 * 60, 24))
    list.extend(get_by_unit(seconds, 'day', 60 * 60 * 24, 365 ))
    list.extend(get_by_unit(seconds, 'year', 60 * 60 * 24 * 365, 1000))

    list.reverse()
    if len(list) > 1:
        last1 = list.pop()
        last2 = list.pop()
        list.append(last2 + ' and ' + last1)

    result = ', '.join(map(str, list))
    return result

print(format_duration(0))
print(format_duration(62))
print(format_duration(3662))
print(format_duration(3662 * 24 * 365 + 45896))