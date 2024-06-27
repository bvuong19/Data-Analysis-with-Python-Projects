import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    calculations = {'mean': [],
                    'variance': [],
                    'standard deviation': [],
                    'max': [],
                    'min': [],
                    'sum': []
                    }
    np_array = np.array(list)

    list_mean = np.mean(np_array)
    list_variance = np.var(np_array)
    list_standard_deviation = np.std(np_array)
    list_max = np.max(np_array)
    list_min = np.min(np_array)
    list_sum = np.sum(np_array)

    np_array = np.reshape(np.array(list), (3,3))

    calculations['mean'].append(np.mean(np_array, axis=0).tolist())
    calculations['mean'].append(np.mean(np_array, axis=1).tolist())
    calculations['mean'].append(list_mean)

    calculations['variance'].append(np.var(np_array, axis=0).tolist())
    calculations['variance'].append(np.var(np_array, axis=1).tolist())
    calculations['variance'].append(list_variance)

    calculations['standard deviation'].append(np.std(np_array, axis=0).tolist())
    calculations['standard deviation'].append(np.std(np_array, axis=1).tolist())
    calculations['standard deviation'].append(list_standard_deviation)

    calculations['max'].append(np.max(np_array, axis=0).tolist())
    calculations['max'].append(np.max(np_array, axis=1).tolist())
    calculations['max'].append(list_max)

    calculations['min'].append(np.min(np_array, axis=0).tolist())
    calculations['min'].append(np.min(np_array, axis=1).tolist())
    calculations['min'].append(list_min)

    calculations['sum'].append(np.sum(np_array, axis=0).tolist())
    calculations['sum'].append(np.sum(np_array, axis=1).tolist())
    calculations['sum'].append(list_sum)

    return calculations
