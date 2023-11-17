import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
mat = loadmat('/media/mmohseni/ubuntu/storage/UCI/uci2_dataset/signal_fold_0.mat')
print(mat.keys())

input = mat['signal']
output = mat['abp_signal']
print('done')
sp = mat['SP']
plt.hist(sp, bins=50, range=(sp.min(), sp.max()))
plt.title('Histogram of sp Tensor')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# def f(input, output):
#     i = input[0, :]
#     o = output[0, :]
#
#     # Normalize the input and output signals
#     i_norm = (i - np.min(i)) / (np.max(i) - np.min(i)) * 100
#     o_norm = (o - np.min(o)) / (np.max(o) - np.min(o)) * 100
#
#     # Calculate the error signal
#     error = np.abs(i_norm - o_norm)
#
#     # Create a figure with two subplots
#     fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
#
#     # Plot the input and output signals in the first subplot
#     ax1.plot(i_norm, label='Input', color='blue')
#     ax1.plot(o_norm, label='Output', color='red')
#     ax1.legend()
#
#     # Plot the error signal in the second subplot
#     ax2.plot(error, label='Error', color='green')
#     ax2.legend()
#
#     # Set the axis labels
#     ax1.set_ylabel('Signal')
#     ax2.set_xlabel('Time')
#     ax2.set_ylabel('Error')
#     # Show the figure
#     plt.show()
#
# def f2(input, output):
#     i = input[0, :]
#     o = output[0, :]
#
#     # Normalize the input and output signals
#     i_norm = (i - np.min(i)) / (np.max(i) - np.min(i)) * 100
#     o_norm = (o - np.min(o)) / (np.max(o) - np.min(o)) * 100
#
#     # Calculate the autocorrelation of the input and output signals
#     autocorr_i = np.correlate(i_norm, i_norm, mode='full')
#     autocorr_o = np.correlate(o_norm, o_norm, mode='full')
#
#     # Plot the autocorrelation functions
#     plt.plot(autocorr_i, label='Input', color='blue')
#     plt.plot(autocorr_o, label='Output', color='red')
#     plt.legend()
#     plt.show()
#
# if __name__ == '__main__':
#     f2(input, output)
#     print('Done')
