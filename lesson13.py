'''
FT Sampling Pairs
-FT of impulse train/comb function is another impulse train/comb function
	-recall FT scaling property
		-ie. that as pulses in space/image domain get far apart, pulses in frequency domain get closer together

Sampling and Reconstruction
-want to store continuous signal in discrete computer -> sampling
-to reconstruct, need to guess values between samples

Sampling in Digital Audio
-with enough dots, can recontruct by connecting dots

Undersampling
-what if we don't have "enough" dots
	-info is lost
	-indistinguishable from other (lower/higher) frequencies
-aliasing: signal "traveling in disguise" as other frequencies

Aliasing
-not enough samples to porperly understand what's going on
	ex. not enough pixels so bits of image get combined

Antialiasing
-how to stop aliasing?
	-sample more often
		-ie. higher resolution cameras
		-can't go on forever/not super robust
	-make signals less wiggly
		-ie. get rid of high freqency information
			-still better than aliasing
		-done by using lowpass filter on initial analog measurement and on analog output reconstructions

Impulse Train or Bed of Nails
-in 2D, comb is called bed of nails

Sampling Low Frequency Signals
-sampling can be done by multiplying continuous function, f(x) and comb, comb_M(x) (m is spacing between signals)
-in frequency, this is convolution of F(w) and comb_1/M(w), G(w)
-if ends for F(w) are small enough (ie. not much high frequency), can cut off G(w) (FT of sampled signal) to perfectly get F(w) and reconstruct f(x)
	-specifically need max frequency W < 1/(2M)
		-Nyquist sampling

Sampling High Frequency Signals
-edges in frequency domain overlap and add
-high frequency from a copy response adds into low frequency of main fresponse
-this is irreversible 
	-so high frequency needs to be removed before sampling
	-done by convolving continuous signal f(x) with an antialiasing filter h(x)
-see 2C-L3-10

Aliasing in Images
ex shrinking
	-can't simply take every 2nd pixel (subsample) to scale by 1/2 (will alias)
	-to do it properly, filter with anti aliasing filter (ex. Gaussian) then subsample

Campbell-Robson Contrast Sensitivity
-some frequencies matter more
	-higher frequency->less sensitive the human vision system is
	-need very high contrast for humans to see high frequency stuff

Image Compression
-using discrete cosine transform (DCT, similar to FT)
	-uses contrast-frequency analysis above to encode low frequency data with more precision than high frequency data
		-losing information but only really losing hard to notice information