'''
-another idea of images: 2D projection of 3D scene

Imaging system
-some device that allows projection of 3D points to a medium that will record light pattern
-losing information (3D->2D), want to recover it

Image Formation
-want light from 1 point in scene to appear in only 1 point on film/sensor
	-otherwise will have meaningless light everywhere
-aperture: small hole that lets in light
	-will invert image on film

Aperture
-focal length: distance between aperture and film
-smaller aperture -> sharper image (to a point)
	-exact size depends on ray size
-too small aperture -> diffraction effects

Lenses
-don't actually just use aperture, use lenses
-lenses are designed to all points at a particular distance are focused on 1 point on film
	-different distances may not be in focus

Thin Lenses
-see 3A-L1-7
-for perpendicular distances z, z` and focal length f, any point satisfying 1/z + 1/z` = 1/f are in focus

Depth of Field
-have a point that exactly in focus, how much does focus change as we move film slightly
	-depends on aperature size (controls how much rays from image can diverge)
	-depth of viable field (how deep things will be in focus) is better for smaller aperture

Field of View
-sometimes called zoom
-more zoom/longer focal length/smaller field of view means camera is more sensitive to movements
-also depends on retina/film size

Zooming and Moving are not the same
-large FOV (which requires moving close) can have large perspective distortion compared to being further and zooming (to keep same approximate size)
ex. dolly zoom

Cameras Aren't Perfect
-geometric distortion
	-from lens impoerfections
	-pin cushion, barrel
-chromatic aberration
	-rays of different wavelength are diffracted differently and focus at different places
-vignetting
	-some rays going through edges of lenses don;'t hit film and are lost

Lens Systems
-cameras now have many lenses
-designed to make images as if they went through a perfect pinhole camera
	-allows computer vision people to mostly just use pinhole model