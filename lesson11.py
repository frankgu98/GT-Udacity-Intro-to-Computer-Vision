'''
Basis Set
-a basis B of a vector space V is a linearly independent subset of V that spans V
-suppose that B = {v_1, ..., v_n} is a finite subset of a vector space V over a field F (ex. ral or complex numbers). Then B is a basis if:
	1. Linear Independence
		For all c_1, ..., c_n in F, if c_1*v_1 + ... + c_n*v_n = 0, then necessarily a_1 = ... = a_n = 0
		-pretty much saying not in same direction
	2. Spanning
		For all x in V, there exists c_1, ..., c_n in F such that x = c_1*v_1 + ... + c_n*v_n
		-not necessarily orthogonal

Basis Sets of Images
-consider an image as a point in NxN space, can rasterize it into a single vector: [x_00, x_10, x_20, ..., x_(n-1)0, x_11, ..., x_(n-1)(n-1)].T
-the normal basis set for images would be: [0, 0, ..., 0, 1, 0, ...]
	-linearly independent
	-can create any image
	-not useful since it's a pixel by pixel look at image
-another basis set is fourier basis
	-made of low and high frequency change in image
	-idea: any periodic function can be rewritten as a weighted sum of sines and cosines of different frequencies
		-sum is called Fourier Series

Sum of Sines
-building block A*sin(wx + ϕ)
	-enough of these can make any signal
	-degrees of freedom:
		-A: amplitude
		-w: frequency (coarse vs fine)
		-ϕ: phase

Time and Frequency
-can usually ignore phase in computer vision since not trying to reconstruct image, just trying to extract useful information about power (A) and frequency (w)

Fourier Transform
-to understand frquency, w, parameterize it (instead of x or t)
-for every omega in (0, inf) (or (-inf, inf)), the Fourier Transform of f(x), F(w), holds the amplitude A and phase ϕ of the corresponding sinusoid
	-holds both by using complex numbers
	-F(w) = R(w) + iI(w)
		-R(w) is even/cos part
		-I(w) if odd/sin part

Computing Fourier Transform
-computes basis set of function
-integral from -inf to inf of sin(a*x + ϕ)sin(b*x + θ)
	-... = 0 if a != b
	-... = inf if a == b (unless |ϕ - θ| = 90 deg)
	-so if a is "unknown", then it can be found by trying integrals with b in a range, and seeing which integral is inf
-can be used to compute basis set for a general function f by checking all possible frequencies
	-don't have to do it for all phases since any phase can be given by weighted sum of integral with sin and cos

Fourier Transfor, More Formal
-see 2C-L1, video 9

Frequency Spectra
-largely only look at |F(w)|
-power spectra tends to fall off at higher frequency (for any natural signal)

Limitations
-Fourier transform, F(w) exists if integral from -inf to inf of |f(x)| exists
-if there's an interval T outside of which f is 0, can only do Fourier transform integral on interval

Discrete Fourier Transform
-see 2C-L1, video 12
-discrete frequency k (cycles per image/interval) can only go from -N/2 to N/2 since min period is 2 (1 sample high, 1 sample low) so number of cycles over N (frequency) would be N/2

2D Fourier Transform
-see 2C-L1, video 13

Examples
-removing high frequency
	-ringing- ripples from not having high frequency to smooth image
-removing low frequency
	-gives edges
-sharpening filter
	-accentuate high frequencies
-pictures with a lot of angled lines leads to higher magnitude lines in frequency spectrum perpendicular to direction of lines in original image
-essentually assumes that image continues periodically past acutal bouds
	-gives high magnitude line in vertical direction from the Transform "sticking" top and bottom edges together