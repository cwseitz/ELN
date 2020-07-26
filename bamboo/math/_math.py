import scipy.optimize as op
import numpy as np
import math
from scipy.optimize import curve_fit

# """
# ~~~~~~~~~~~General Functions~~~~~~~~~~~~~~
# """

def fit_linear(x, y):

	"""Perform linear regression on bivariate data
	Parameters
	----------
	x: 1d ndarray
		raw x data
	y: 1d ndarray
		raw y data
	Returns
	-------
	popt, pcov: 1d ndarray
		optimal parameters and covariance matrix
	"""

	from scipy import stats

	slope, intercept, r, p, stderr = \
		stats.linregress(x,y)

	return slope, intercept, r, p

def fit_gaussian1d(x, y):

	"""1D Gaussian fitting function
	Parameters
	----------
	x: 1d ndarray
		raw x data
	y: 1d ndarray
		raw y data
	Returns
	-------
	popt, pcov: 1d ndarray
		optimal parameters and covariance matrix
	"""

	popt, pcov = curve_fit(gaussian1d, x, y)

	return popt, pcov

def gaussian1d(x,x0,amp,sigma):

	y = amp*np.exp(-(x-x0)**2/(2*sigma**2))

	return y

def fit_poisson1d(x,y):


	"""1D Scaled Poisson fitting function
	Parameters
	----------
	x: 1d ndarray
		raw x data
	y: 1d ndarray
		raw y data
	scale: float
		scaling factor for the poisson distribution
	Returns
	-------
	popt, pcov: ndarray
		optimal parameters and covariance matrix
	"""

	popt, pcov = curve_fit(poisson1d,x,y)

	return popt, pcov

def poisson1d(x, lambd, scale):

	return scale*(lambd**x/factorial(x))*np.exp(-lambd)

# """
# ~~~~~~~~~~~MSD Functions~~~~~~~~~~~~~~
# """

def fit_offset_msd(x,y, space='log'):

	"""Mean Squared Dispacement fitting
	Parameters
	----------
	x: 1d array
		raw x data
	y: 1d array
		raw y data
	space: string
		'log' for fitting in log space (default)
		'linear' for sitting in linear space
	Returns
	-------
	popt, pcov: 1d ndarray
		optimal parameters and covariance matrix
	"""

	cmax = 1e6
	popt, pcov = op.curve_fit(offset_msd, x, y,
							  bounds=(0, [np.inf, np.inf, cmax]),
							  maxfev=1000)

	return popt

def fit_msd(x,y, space='log'):

	"""Mean Squared Dispacement fitting
	Parameters
	----------
	x: 1d array
		raw x data
	y: 1d array
		raw y data
	space: string
		'log' for fitting in log space (default)
		'linear' for sitting in linear space
	Returns
	-------
	popt, pcov: 1d ndarray
		optimal parameters and covariance matrix
	"""

	def fit_msd_log(x, y):

		from scipy import stats

		x = [math.log(i) for i in x]
		y = [math.log(i) for i in y]

		slope, intercept, r, p, stderr = \
			stats.linregress(x,y)

		D = np.exp(intercept) / 4; alpha = slope
		popt = (D, alpha)
		return popt

	def fit_msd_linear(x, y):

		popt, pcov = op.curve_fit(msd, x, y,
								  bounds=(0, [np.inf, np.inf]))

		return popt

	if space == 'log':
		popt = fit_msd_log(x,y)
	elif space == 'linear':
		popt = fit_msd_linear(x,y)

	return popt

def offset_msd(x, D, alpha, c):

	return 4*D*(x**alpha) + c

def msd(x, D, alpha):

	return 4*D*(x**alpha)

# """
# ~~~~~~~~~~~Miscellaneous Functions~~~~~~~~~~~~~~
# """

def spot_count(x,a,tau,c):

	return a*(1-np.exp(-x/tau)) + c

def fit_spotcount(x, y):

	"""Spot count fitting function
	Parameters
	----------
	x: 1d ndarray
		raw x data
	y: 1d ndarray
		raw y data
	Returns
	-------
	popt, pcov: 1d ndarray
		optimal parameters and covariance matrix
	"""

	c = y[0]
	popt, pcov = op.curve_fit(lambda x,a,tau: spot_count(x,a,tau,c), x, y)
	popt = [*popt, c]

	return popt

def fit_expdecay(x,y):

	"""Exponential decay fitting function
	Parameters
	----------
	x: 1d ndarray
		raw x data
	y: 1d ndarray
		raw y data
	Returns
	-------
	popt, pcov: 1d ndarray
		optimal parameters and covariance matrix
	"""

	def exp_decay(x,a,b,c):

		return a*(np.exp(-(x-b)/c))

	popt, pcov = op.curve_fit(exp_decay, x, y)

	return popt, pcov

def fit_sigmoid(x,y):

	"""Sigmoid fitting function
	Parameters
	----------
	x: 1d ndarray
		raw x data
	y: 1d ndarray
		raw y data
	Returns
	-------
	popt, pcov: 1d ndarray
		optimal parameters and covariance matrix
	"""

	def sigmoid(x, a, b, c, d):

		return a/(1+np.exp(-b*(x-c))) + d

	param_bounds=([0,1],[np.inf,1.5])

	popt, pcov = op.curve_fit(sigmoid, x, y)

	return popt, pcov

def interpolate_lin(x_discrete, f_discrete, resolution=100, pad_size=0):

	"""Numpy wrapper for performing linear interpolation
	Parameters
	----------
	x_discrete: 1d ndarray
		discrete domain
	y: 1d ndarray
		discrete function of x_discrete
	Returns
	-------
	"""

	min_center, max_center = x_discrete[0], x_discrete[-1]
	x_cont = np.linspace(min_center, max_center, resolution)

	f_cont = np.interp(x_cont, x_discrete, f_discrete)
	if pad_size > 0:

		x_pad = np.linspace(min_center-pad_size, min_center, pad_size)
		f_cont_pad = np.full(pad_size, 0)
		x_cont = np.concatenate((x_pad, x_cont), axis=0)
		f_cont = np.concatenate((f_cont_pad, f_cont), axis=0)

	return x_cont, f_con

# """
# ~~~~~~~~~~~PSF Fitting~~~~~~~~~~~~~~
# """

def gaussian_2d(X, A, x0, y0, sig_x, sig_y, phi):
    """
    2D Gaussian function

    Parameters
    ----------
    X : 3d ndarray
        X = np.indices(img.shape).
		X[0] is the row indices.
        Y[1] is the column indices.
    A : float
        Amplitude.
    x0 : float
        x coordinate of the center.
    y0 : float
        y coordinate of the center.
    sig_x : float
        Sigma in x direction.
    sig_y : float
        Sigma in x direction.
    phi : float
        Angle between long axis and x direction.


    Returns
    -------
    result_array_2d: 21d ndarray
        2D gaussian.
    """

    x = X[0]
    y = X[1]
    a = (np.cos(phi)**2)/(2*sig_x**2) + (np.sin(phi)**2)/(2*sig_y**2)
    b = -(np.sin(2*phi))/(4*sig_x**2) + (np.sin(2*phi))/(4*sig_y**2)
    c = (np.sin(phi)**2)/(2*sig_x**2) + (np.cos(phi)**2)/(2*sig_y**2)
    result_array_2d = A*np.exp(-(a*(x-x0)**2+2*b*(x-x0)*(y-y0)+c*(y-y0)**2))

    return result_array_2d

def get_moments(img):
    """
    Get gaussian parameters of a x2D distribution by calculating its moments

    Parameters
    ----------
    img : 2d ndarray
        image.

    Returns
    -------
    params_tuple_1d: tuple
        parameters (A, x0, y0, sig_x, sig_y, phi).
    """

    total = img.sum()
    X, Y = np.indices(img.shape)
    x0 = (X*img).sum()/total
    y0 = (Y*img).sum()/total
    col = img[:, int(y0)]
    sig_x = np.sqrt(np.abs((np.arange(col.size)-y0)**2*col).sum()/col.sum())
    row = img[int(x0), :]
    sig_y = np.sqrt(np.abs((np.arange(row.size)-x0)**2*row).sum()/row.sum())
    A = img.max()
    phi = 0
    params_tuple_1d = A, x0, y0, sig_x, sig_y, phi
    return params_tuple_1d

def fit_gaussian_2d(img, diagnostic=False):
    """
    Fit gaussian_2d

    Parameters
    ----------
    img : 2d ndarray
        image.
    diagnostic : bool, optional
        If True, show the diagnostic plot

    Returns
    -------
    popt, pcov: 1d ndarray
        optimal parameters and covariance matrix

    Examples
    --------
    import numpy as np
    import matplotlib.pyplot as plt
    from cellquantifier.math.gaussian_2d import gaussian_2d, fit_gaussian_2d
    from cellquantifier.io.imshow import imshow
    X = np.indices((100,100))
    A, x0, y0, sig_x, sig_y, phi = 1, 50, 80, 30, 10, 0.174
    out_array_1d = gaussian_2d(X, A, x0, y0, sig_x, sig_y, phi)
    img = out_array_1d.reshape((100,100))
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()
    popt, p_err = fit_gaussian_2d(img, diagnostic=True)
    print(popt)
    """

    # """
    # ~~~~~~~~~~~~~~Prepare the input data and initial conditions~~~~~~~~~~~~~~
    # """

    X = np.indices(img.shape)
    x = np.ravel(X[0])
    y = np.ravel(X[1])
    xdata = np.array([x,y])
    ydata = np.ravel(img)
    p0 = get_moments(img)

    # """
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Fitting~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # """

    popt, pcov = curve_fit(gaussian_2d, xdata, ydata, p0=p0)
    p_sigma = np.sqrt(np.diag(pcov))
    p_err = p_sigma

    # """
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Diagnostic~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # """

    if diagnostic:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.imshow(img, cmap='gray')

        (A, x0, y0, sig_x, sig_y, phi) = popt
        (A_err, x0_err, y0_err, sigma_x_err, sigma_y_err, phi_err) = p_err
        Fitting_data = gaussian_2d(X,A,x0,y0,sig_x,sig_y,phi)
        ax.contour(Fitting_data, cmap='cool')
        ax.text(0.95,
                0.00,
                """
                x0: %.3f (\u00B1%.3f)
                y0: %.3f (\u00B1%.3f)
                sig_x: %.3f (\u00B1%.3f)
                sig_y: %.3f (\u00B1%.3f)
                phi: %.1f (\u00B1%.2f)
                """ %(x0, x0_err,
                      y0, y0_err,
                      sig_x, sigma_x_err,
                      sig_y, sigma_y_err,
                      np.rad2deg(phi), np.rad2deg(phi_err)),
                horizontalalignment='right',
                verticalalignment='bottom',
                fontsize = 12,
                color = (1, 1, 1, 0.8),
                transform=ax.transAxes)
        plt.show()

    return popt, p_err
