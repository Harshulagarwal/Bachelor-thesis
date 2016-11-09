import numpy as np
from sets import Set
import copy
import Programming.TensorFlow.configuration as conf


def filterAndCreateTrainSet(validation_names, test_names, images, labels, names):
    size = 0
    print('LEN: '+str(len(Set(names))))
    for i in range(images.shape[0]):
        if (names[i] not in validation_names) and (names[i] not in test_names):
            images[size] = images[i]
            labels[size] = labels[i]
            names[size] = names[i]
            size += 1
    perm = np.arange(size)
    np.random.shuffle(perm)
    images = images[perm]
    labels = labels[perm]
    names = names[perm]
    print('LEN: '+str(len(Set(names))))
    return images, labels, names


def getPermutation(permutation_index, labels, validation_size, test_size):
    num_of_images_total = len(labels)
    if permutation_index >= 10 or permutation_index < 0:
        raise ValueError('Permutation index should not be larger than 9 and lower than 0')
    perm = np.arange(num_of_images_total)
    for i in range(permutation_index + 1):
        np.random.shuffle(perm)

    percentage = validation_size / float(num_of_images_total)
    counts = np.array(percentage * np.bincount(np.array(labels, dtype=int)), dtype=int)
    to_add = validation_size - sum(counts)
    for i in np.arange(counts.shape[0])[:to_add]:
        counts[i] += 1
    a = np.zeros(0, dtype=int)
    b = np.zeros(0, dtype=int)
    c = np.zeros(0, dtype=int)
    d = np.zeros(0, dtype=int)
    counts_tmp = np.copy(counts)
    for t in perm:
        if counts[labels[t]] > 0:
            counts[labels[t]] -= 1
            a = np.append(a, t)
        else:
            b = np.append(b, t)
    counts = counts_tmp
    print(counts)
    for t in b:
        if counts[labels[t]] > 0:
            counts[labels[t]] -= 1
            c = np.append(c, t)
        else:
            d = np.append(d, t)

    print (np.append(a, np.append(c, d)))
    return np.append(a, np.append(c, d))


def getOriginalDatasetSize(data):
    divide_by = 8 if conf.EXTENDED_DATASET else 1
    original_dataset_size = data.size() / divide_by
    return original_dataset_size


def process(full_data, permutation_index):
    original_set_size = getOriginalDatasetSize(full_data)
    TEST_SIZE = int(original_set_size * (conf.TEST_PERCENTAGE / 100.0))
    VALIDATION_SIZE = int(original_set_size * (conf.VALIDATION_PERCENTAGE / 100.0))

    perm2 = getPermutation(permutation_index, full_data.labels[:original_set_size], VALIDATION_SIZE, TEST_SIZE)

    original_data = copy.deepcopy(full_data).applyPermutation(perm2)
    test_data = original_data.createData(0, TEST_SIZE)
    validation_data = original_data.createData(TEST_SIZE, TEST_SIZE + VALIDATION_SIZE)

    if conf.EXTENDED_DATASET:
        train_images, train_labels, train_names = filterAndCreateTrainSet(validation_data.names, test_data.names, full_data.images, full_data.labels,
                                                                          full_data.names)
    else:
        train_data = full_data.createData(TEST_SIZE + VALIDATION_SIZE, full_data.size())
        train_images, train_labels, train_names = train_data.images, train_data.labels, train_data.names

    return train_images, train_labels, validation_data.images, validation_data.labels, test_data.images, test_data.labels
