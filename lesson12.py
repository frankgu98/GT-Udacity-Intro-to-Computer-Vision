'''
Fourier Transform and Convolution
-convolution in spacial domain is multiplication in frequency doman
-multiplication in spacial domain is convolution in frequency domain	

FFT
-can convolve big matrices by doing FFT on matrices then multiplying their frequency domain representations then doing IFT
	-ex large mask and large image

Smoothing and Blurring
-FT of Gaussian is Gaussian
	-FT of FT of Gaussian is original
-so by applying convolution principle above, smoothing with a Gaussian "keeps" low frequency, fatter Gaussian == more smoothing == skinnier FT of Gaussian == more low frequency (since distribution is centered)
ex. see 2C-L2-5

Properties of FT
-linearity
-convolution
-scaling: shrink in image domain is stretch in frequency domain
-differentiation: differentiation in image domain is multiplication by argument (frequency) in frequency domain

Fourier pairs
-junk from convolving with box filter averaging is from fourier series of box filter (sinc(w))
	-exactly like ringing (in frequency domain vs image domain)