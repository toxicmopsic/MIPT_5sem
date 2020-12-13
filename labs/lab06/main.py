class Dict(object):
    def __init__(self, *args, **kwargs):
        size=1000
        self.storage = [[] for _ in range(size)]
        self.size = size
        self.length = 0
        if kwargs:
            for key, value in kwargs.items():
                self.__setitem__(key, value)

    def __setitem__(self, key, value):
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if key == ele[0]:
                ele[1] = value
                break
        else:
            self.storage[storage_idx].append([key, value])
            self.length += 1

    def __getitem__(self, key):
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if ele[0] == key:
                return ele[1]
        raise KeyError('Key {} dont exist'.format(key))

    def __delitem__(self, key):
        storage_idx = hash(key) % self.size
        for sub_lst in self.storage[storage_idx]:
            if key == sub_lst[0]:
                self.storage[storage_idx].remove(sub_lst)
                self.length -= 1
                return
        raise KeyError('Key {} dont exist'.format(key))

    def __contains__(self, key):
        storage_idx = hash(key) % self.size
        for item in self.storage[storage_idx]:
            if item[0] == key:
                return True
        return False

    def __len__(self):
        return self.length

    def __iterate_kv(self):
        for sub_lst in self.storage:
            if not sub_lst:
                continue
            for item in sub_lst:
                yield item

    def __iter__(self):
        for key_var in self.__iterate_kv():
            yield key_var[0]

    def __add__(self, data):
        return Dict(**self, **data)

    def keys(self):
        return self.__iter__()

    def values(self):
        for key_var in self.__iterate_kv():
            yield key_var[1]

    def items(self):
        return self.__iterate_kv()

    def get(self, key):
        try:
            return self.__getitem__(key)
        except KeyError:
            return None

    def add(data1, data2):
        return Dict(**data1, **data2)

    def from_default(data):
        return Dict(**data)

    def __str__(self):
        res = []
        for ele in self.storage:
            for key_value in ele:
                if isinstance(key_value[0], str):
                    key_str = '\'{}\''.format(key_value[0])
                else:
                    key_str = '{}'.format(key_value[0])
                if isinstance(key_value[1], str):
                    value_str = '\'{}\''.format(key_value[1])
                else:
                    value_str = '{}'.format(key_value[1])

                res.append('{}: {}'.format(key_str, value_str))
        key_value_pairs_str = '{}'.format(', '.join(res))
        return '{' + key_value_pairs_str + '}'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    data = Dict()

    data['johnny'] = 'depp'
    data['margot'] = 'robbie'
    print(data)
    # {'johnny': 'depp', 'margot': 'robbie'}

    print(len(data))
    # 2

    for name, family_name in data.items():
        print(name, family_name)
    # johnny depp
    # margot robbie

    del data['johnny']
    print(len(data))
    # 1

    print('margot' in data)
    # True

    data1 = Dict()
    print(data1)
    # {}

    data2 = Dict(color='red', state='aggressive')
    print(data2)
    # {'color': 'red', 'state': 'aggressive'}

    data1 = Dict(a=1)
    data2 = Dict(b=2)

    print(data1 + data2)
    # {'a': 1, 'b': 2}

    print(data1 + {'b': 2})
    # {'a': 1, 'b': 2}

    print(Dict.add(data1, data2))
    # {'a': 1, 'b': 2}

    print(Dict.from_default({'time': '1:21', 'doing': 'writing hw'}))
    # {'time': '1:21', 'doing': 'writing hw'}
