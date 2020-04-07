import serial
import time
from json import loads, JSONDecodeError
from matplotlib import pyplot as plt
import matplotlib.animation as animation


class Axis:
    def __init__(self, name, data):
        self.name = name
        self.x = data[0]
        self.y = data[1]
        self.z = data[2]


class SensorData:
    def __init__(self, data):
        self.time = str(data["accelerometer"]) + "ms"
        self.acc = Axis("accelerometer", data["accelerometer"])
        self.gyro = Axis("gyro", data["gyro"])
        self.mag = Axis("magnetometer", data["magnetometer"])


baudrate = 115200
port = 'COM3'
ser = serial.Serial(port, baudrate)

plt.style.use('fivethirtyeight')

fig_gyro_x = plt.figure()
gyro_x_ax = fig_gyro_x.add_subplot(1, 1, 1)
gyro_x_xs = []
gyro_x_ys = []

fig_gyro_y = plt.figure()
gyro_y_ax = fig_gyro_y.add_subplot(1, 1, 1)
gyro_y_xs = []
gyro_y_ys = []

fig_gyro_z = plt.figure()
gyro_z_ax = fig_gyro_z.add_subplot(1, 1, 1)
gyro_z_xs = []
gyro_z_ys = []


def refresh():
    this_data = ser.readline()
    try:
        print(this_data)
        dict_data = loads(this_data[:-2].decode().replace("'", '"'))
        return SensorData(dict_data)
    except JSONDecodeError:
        return None


def animate(i, xs, ys):
    data = refresh()
    if data is not None:

        ##########  Gyro x

        y = data.gyro.x
        x = time.time()
        gyro_x_xs.append(x)
        gyro_x_ys.append(y)

        gyro_x_ax.clear()
        gyro_x_ax.plot(gyro_x_xs, gyro_x_ys, label="Gyro X Axis")

        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title("Gyro X axis")
        plt.ylabel('Gyro Amount')
        plt.legend()

        ##########  End Gyro X

        ##########  Gyro y

        y = data.gyro.y
        x = time.time()
        gyro_y_xs.append(x)
        gyro_y_ys.append(y)

        gyro_y_ax.clear()
        gyro_y_ax.plot(gyro_y_xs, gyro_y_ys, label="Gyro Y Axis")

        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title("Gyro Y axis")
        plt.ylabel('Gyro Amount')
        plt.legend()

        ##########  End Gyro y

        ##########  Gyro z

        y = data.gyro.z
        x = time.time()
        gyro_z_xs.append(x)
        gyro_z_ys.append(y)

        gyro_z_ax.clear()
        gyro_z_ax.plot(gyro_z_xs, gyro_z_ys, label="Gyro Z Axis")

        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title("Gyro Z axis")
        plt.ylabel('Gyro Amount')
        plt.legend()

        ##########  End Gyro z


ani_x = animation.FuncAnimation(fig_gyro_x, animate, fargs=(gyro_x_xs, gyro_x_ys))
ani_y = animation.FuncAnimation(fig_gyro_y, animate, fargs=(gyro_y_xs, gyro_y_ys))
ani_z = animation.FuncAnimation(fig_gyro_z, animate, fargs=(gyro_z_xs, gyro_z_ys))

plt.show()

#print(f'{dict_data["time"]}| {dict_data["accelerometer"]}| {dict_data["gyro"]}| {dict_data["magnetometer"]}|\n')
