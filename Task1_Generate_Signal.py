import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

from CompareSignals1 import SignalSamplesAreEqual

def generate_signal():
    Stype = signal_type_entry.get()
    A = float(amplitude_entry.get())
    A_Freq = float(analog_frequency_entry.get())
    S_Freq = float(sample_frequency_entry.get())
    phase = float(phase_shift_entry.get())
    t = np.arange(0, 1, 1/S_Freq)
    
    if Stype == 'sin':
        signal = A * np.sin(2 * np.pi * A_Freq * t + phase)
        plot_continus('Continuous Sin Wave',t,signal)
        plot_discrete('Discrete Sin Wave',t,signal)
        SignalSamplesAreEqual('Task 1 Test Cases\Signals\Sin_Cos\SinOutput.txt',[],signal)
    elif Stype == 'cos':
        signal = A * np.cos(2 * np.pi * A_Freq * t + phase)
        plot_continus('Continuous Cos Wave',t,signal)
        plot_discrete('Discrete Cos Wave',t,signal)
        SignalSamplesAreEqual('Task 1 Test Cases\Signals\Sin_Cos\CosOutput.txt',[],signal)
   


def plot_continus(title,t,signal):
    
    fig = plt.figure(figsize=(5, 4), dpi=100)
    plt.plot(t, signal,label='Continuous')
    plt.title(title)
    plt.vlines(t, [0], signal, colors='red', linestyles='dashed')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()
def plot_discrete(title,t,signal):
    # Plot the signal as a discrete signal
    plt.stem(t, signal, use_line_collection=True)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.grid(True)
    plt.show()
def Run_Generate_Signal():
    window = tk.Tk()
    window.title('Signal Genrator')
    window.geometry('500x700')
    
    # Create the signal type label and entry
    signal_type_label = tk.Label(window, text='Signal Type:')
    signal_type_label.pack()
    global signal_type_entry
    signal_type_entry = tk.Entry(window)
    signal_type_entry.pack()

    # Create the amplitude label and entry
    amplitude_label = tk.Label(window, text='Amplitude:')
    amplitude_label.pack()
    global amplitude_entry
    amplitude_entry = tk.Entry(window)
    amplitude_entry.pack()

    # Create the analog frequency label and entry
    analog_frequency_label = tk.Label(window, text='Analog Frequency:')
    analog_frequency_label.pack()
    global analog_frequency_entry
    analog_frequency_entry = tk.Entry(window)
    analog_frequency_entry.pack()

    # Create the sample frequency label and entry
    sample_frequency_label = tk.Label(window, text='Sample Frequency:')
    sample_frequency_label.pack()
    global sample_frequency_entry
    sample_frequency_entry = tk.Entry(window)
    sample_frequency_entry.pack()

    # Create the phase shift label and entry
    phase_shift_label = tk.Label(window, text='Phase Shift:')
    phase_shift_label.pack()
    global phase_shift_entry
    phase_shift_entry = tk.Entry(window)
    phase_shift_entry.pack()

    # Create the plot button
    plot_button = tk.Button(window, text='Plot', command=generate_signal)
    plot_button.pack()
    
    window.mainloop()

#Run_Generate_Signal()


