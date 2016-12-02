def rotate_to_first_in_deque_and_pop(input_deque, predicate):
    """
    Finds the first item in the deque that satisfies the condition by rotating through the deque using popleft().
    Faster than doing a sort on the deque.
    """
    for _ in xrange(0, len(input_deque)):
        item = input_deque.popleft()
        if predicate(item):
            return item
        input_deque.append(item)  # Move the item to the end
    return None


def pop_first_from_list_or_end(input_list, predicate):
    for i in xrange(len(input_list)-1, -1, -1):
        if predicate(input_list[i]):
            return input_list.pop(i)
    return input_list.pop()


def count_if(input_list, predicate):
    c = 0
    for item in input_list:
        if predicate(item):
            c += 1
    return c


def convert_dictionary(d, keyConverter, valueConverter):
    new_dict = {}
    for key, value in d.iteritems():
        new_dict[keyConverter(key) if keyConverter else key] = valueConverter(value) if valueConverter else value
    return new_dict
