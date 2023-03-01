import numpy as np

def smooth(x, window_len=11, window='hanning'):
    # Adapted from https://stackoverflow.com/questions/20618804/how-to-smooth-a-curve-in-the-right-way
    if x.ndim != 1:
        raise ValueError("smooth only accepts 1 dimension arrays.")
    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")
    if window_len < 3:
        return x
    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError("Window is one of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")
    s = np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w = np.ones(window_len,'d')
    else:
        w = eval('np.'+window+'(window_len)')
    y = np.convolve(w/w.sum(),s,mode='valid')
    return y[(window_len//2-1):-(window_len//2)]

# Your original coordinates
coords = [[1,2],[3,2],[5,6],[3,3],[4,6],[5,9],[6,5],[5,7],[8,5],[8,8],[9,10],
          [9,10],[9,10],[9,10],[9,10],[9,10],[9,10],[9,10],
          [9,10],[9,10],[9.5 ,11.5 ],[19.5 ,20.5 ],[19.75 ,20.75 ],[19.875 ,20.875 ],
          [19.9375 ,20.9375 ],[19.96875 ,20.96875 ],[19.984375 ,20.984375 ],
          [19.9921875 ,20.9921875 ],[19.99609375 ,20.99609375 ],
          [19.998046875 ,20.998046875 ],[19.9990234375 ,21 ]]

# Separate x and y coordinates
x_coords = [c[0] for c in coords]
y_coords = [c[1] for c in coords]

# Smooth x and y coordinates separately
smoothed_x_coords = smooth(np.array(x_coords), window_len=7)
smoothed_y_coords = smooth(np.array(y_coords), window_len=7)

# Combine smoothed coordinates
smoothed_coords = list(zip(smoothed_x_coords.tolist(), smoothed_y_coords.tolist()))

# Print smoothed coordinates
print(smoothed_coords)