import Programming.configuration as conf

FC1_FEATURES = 1300
BASE_LEARNING_RATE = 0.0001
DECAY_RATE = 0.6
MOMENTUM = 0.95
DROPOUT_PROBABILITY = 0.6
CROSS_VALIDATION_ITERATIONS = 5
DECAY_STEP_X_TIMES_TRAIN_SIZE = 8
C1_FEATURES = 1300
CON_FIRST_STRIDE = 2
CONV_FIRST_FILTER_SIZE = 5
CONV_SECOND_FILTER_SIZE = 5
CONV_FIRST_DEPTH = 75
POOL_FIRST_SIZE = 2
CONV_SECOND_DEPTH = 150
POOL_SEC_SIZE = 2
EVAL_BATCH_SIZE = 151
EVAL_FREQUENCY = 30
VALIDATION_FREQUENCY = 5
USE_TEST_DATA = False
TRAIN_VALIDATION_CONDITION = 2
BATCH_SIZE = 100
NUM_CHANNELS = 3

SCALE = 2
IMAGE_WIDTH = 16 * SCALE
if conf.CROPPED_VERSION:
    IMAGE_HEIGHT = 16 * SCALE
    SOURCE_FOLDER_NAME = "../Datasets/Cropped datasets/" + conf.SUB_FOLDER + "Dataset_" + str(IMAGE_WIDTH) + "_" + str(
        IMAGE_HEIGHT) + "/"
else:
    IMAGE_HEIGHT = 12 * SCALE
    SOURCE_FOLDER_NAME = "../Datasets/Original datasets/Dataset_" + str(IMAGE_WIDTH) + "_" + str(IMAGE_HEIGHT) + "/"

