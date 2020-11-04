import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

x  = [i+1 for i in [49, 69, 89, 99, 119, 129, 149, 159, 169, 179, 189, 199]]

y0 = [58.59199905395508, 61.84199905395508, 64.51599884033203, 65.81999969482422, 67.67400360107422, 68.50599670410156, 70.23600006103516, 70.5979995727539, 71.552001953125, 72.2760009765625, 72.76799774169922, 73.09200286865234]

y1 = [58.65599822998047, 62.64400100708008, 65.26599884033203, 66.0979995727539, 68.09400177001953, 68.77400207519531, 70.43800354003906, 70.91400146484375, 71.69200134277344, 72.13999938964844, 72.64600372314453, 73.48200225830078]

y2 = [57.9640007019043, 61.58399963378906, 63.619998931884766, 65.05999755859375, 66.98400115966797, 67.69599914550781, 68.91799926757812, 69.65799713134766, 70.55400085449219, 71.18000030517578, 71.41000366210938, 71.98400115966797]

y3 = [55.46799850463867, 58.736000061035156, 61.09199905395508, 62.358001708984375, 63.055999755859375, 64.69200134277344, 66.5479965209961, 67.14199829101562, 67.7239990234375, 68.39600372314453, 68.85199737548828, 69.35600280761719]

z0 = [57.981998443603516, 61.487998962402344, 63.83599853515625, 65.19400024414062, 67.04399871826172, 67.78199768066406, 69.27200317382812, 69.91200256347656, 70.5199966430664, 71.13999938964844, 71.75399780273438, 72.34200286865234]

z1 = [59.5099983215332, 62.99599838256836, 65.63800048828125, 66.61599731445312, 68.45800018310547, 69.50800323486328, 70.64199829101562, 71.58399963378906, 72.30599975585938, 72.9739990234375, 73.5979995727539, 73.83799743652344]

z2 = [56.88600158691406, 60.880001068115234, 63.49399948120117, 64.05000305175781, 66.12999725341797, 67.12000274658203, 68.68800354003906, 69.26200103759766, 70.3239974975586, 70.947998046875, 71.56600189208984, 71.99400329589844]

z3 = [56.874000549316406, 59.24800109863281, 62.077999114990234, 62.65399932861328, 64.81800079345703, 64.93599700927734, 66.6259994506836, 67.89399719238281, 68.58000183105469, 69.04000091552734, 69.78399658203125, 69.43599700927734]

plt.plot(x, [sum(i)*0.5 for i in zip(y0, z0)], 'gs-', label='Dropout rate: 0')
plt.plot(x, [sum(i)*0.5 for i in zip(y1, z1)], 'yo-', label='Dropout rate: 5%')
plt.plot(x, [sum(i)*0.5 for i in zip(y2, z2)], 'b*-', label='Dropout rate: 10%')
plt.plot(x, [sum(i)*0.5 for i in zip(y3, z3)], 'r^-', label='Dropout rate: 20%')


plt.xlabel('Epoch')
plt.ylabel('Accuracy')

plt.legend()
plt.show()

# print(plt.style.available)