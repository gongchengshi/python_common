import pickle


def unpickle_set(path):
    if path is None:
        return set()

    try:
        with open(path, 'rb') as in_file:
            return pickle.load(in_file)
    except IOError:
        pass

    return set()


def pickle_set(set_obj, path):
    with open(path, 'wb') as out_file:
        pickle.dump(set_obj, out_file)
