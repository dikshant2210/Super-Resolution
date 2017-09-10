from keras.layers import Input, Activation, BatchNormalization, Conv2D, UpSampling2D
from keras.models import Model
from keras.optimizers import Adam
from keras.losses import mean_squared_error
from models.losses import dice_loss


def gun_256(input_size):
    num_classes = 1
    inputs = Input(shape=(input_size, input_size, 3))
    # 256

    up0 = UpSampling2D((2, 2))(inputs)
    conv0 = Conv2D(64, (3, 3), padding='same')(up0)
    conv0 = BatchNormalization()(conv0)
    conv0 = Activation('relu')(conv0)
    conv0 = Conv2D(64, (3, 3), padding='same')(conv0)
    conv0 = BatchNormalization()(conv0)
    conv0 = Activation('relu')(conv0)
    conv0 = Conv2D(64, (3, 3), padding='same')(conv0)
    conv0 = BatchNormalization()(conv0)
    conv0 = Activation('relu')(conv0)
    conv0 = Conv2D(64, (3, 3), padding='same')(conv0)
    conv0 = BatchNormalization()(conv0)
    conv0 = Activation('relu')(conv0)
    # 512

    up1 = UpSampling2D((2, 2))(conv0)
    conv1 = Conv2D(64, (3, 3), padding='same')(up1)
    conv1 = BatchNormalization()(conv1)
    conv1 = Activation('relu')(conv1)
    conv1 = Conv2D(64, (3, 3), padding='same')(conv1)
    conv1 = BatchNormalization()(conv1)
    conv1 = Activation('relu')(conv1)
    conv1 = Conv2D(64, (3, 3), padding='same')(conv1)
    conv1 = BatchNormalization()(conv1)
    conv1 = Activation('relu')(conv1)
    conv1 = Conv2D(64, (3, 3), padding='same')(conv1)
    conv1 = BatchNormalization()(conv1)
    conv1 = Activation('relu')(conv1)
    # 1024

    classify = Conv2D(num_classes, (1, 1), activation='sigmoid')(conv1)
    model = Model(inputs=inputs, outputs=classify)
    model.compile(optimizer=Adam(lr=0.0001), loss=mean_squared_error, metrics=[dice_loss])

    return model
