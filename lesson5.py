'''
-make sure filters are normalized - normalized correlation
	-make filter's standard deviation 1
	-make patch of pixels that filter is operating on's standard deviation 1

(normalized) Cross Correlation
	-if making a filter out of a section of signal, then the max value of the output will be where the filter was taken from signal
		-ie. filters as templates
	-location of max G = HⓍF is where in F, H (or the most similar section to H) can be found
		-for H not actually in F, template matching may still be meaningful if similar object actually is in F (similar in scale, orientation, general appearance, etc)
	-may not be perfect for finding objects images where exact template is not in image but can still get good candidate areas
	
