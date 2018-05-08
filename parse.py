import matplotlib.pyplot as plt

s = [
(7.691440, -4.606091),
(7.691440, -4.606091),
(7.691440, -4.606091),
(7.697617, -4.606261),
(7.691165, -4.599814),
(7.697617, -4.606261),
(7.697617, -4.606261),
(7.697342, -4.599984),
(7.697342, -4.599984),
(7.703553, -4.600166),
(7.691440, -4.606091),
(7.749383, -4.779403),
(7.842209, -5.147532),
(7.863516, -5.445924),
(7.931717, -5.800496),
(7.935047, -6.110202),
(7.912122, -6.401840),
(7.918002, -6.642793),
(7.873671, -6.897154),
(7.855532, -7.045585),
(7.836770, -7.051719),
(7.592092, -7.131543),
(7.401857, -7.152039),
(7.122023, -7.155992),
(6.772685, -7.164195),
(6.449878, -7.193684),
(6.126751, -7.202752),
(5.765784, -7.196891),
(5.443471, -7.199246),
(5.140269, -7.181742),
(4.711674, -7.166701),
(4.234002, -7.183859),
(3.920143, -7.186429),
(3.619434, -7.162238),
(3.275507, -7.150151),
(2.938753, -7.118089),
(2.739223, -7.117914),
(2.515129, -7.110041),
(2.272991, -7.087992),
(2.086172, -7.101605),
(2.086961, -6.853654),
(1.987269, -6.458403),
(1.930557, -5.899274),
(1.923309, -5.543068),
(1.906161, -5.317783),
(1.898793, -4.973608),
(1.881248, -4.582129),
(1.890612, -4.288926),
(1.873369, -3.898747),
(1.877036, -3.604793),
(1.843449, -3.191642),
(1.826211, -2.831379),
(1.831128, -2.510768),
(1.827894, -2.093585),
(1.810392, -1.762067),
(1.792173, -1.456416),
(1.785005, -1.336179),
(1.912055, -1.298660),
(2.198962, -1.269902),
(2.595194, -1.226065),
(2.963235, -1.176057),
(3.257016, -1.101715),
(3.493174, -1.032217),
(3.786611, -0.935304),
(4.102617, -0.850389),
(4.395362, -0.753791),
(4.802663, -0.664937),
(5.244572, -0.599336),
(5.532081, -0.581613),
(5.808761, -0.580764),
(6.103200, -0.585752),
(6.374140, -0.562135),
(6.744300, -0.557179),
(7.074561, -0.551462),
(7.388028, -0.550927),
(7.787988, -0.523819),
(8.183114, -0.507808),
(8.308494, -0.555102),
(8.404134, -0.967072),
(8.455567, -1.319580),
(8.471810, -1.674854),
(8.496618, -1.975251),
(8.528590, -2.391606),
(8.553830, -2.698234),
(8.581164, -3.037961),
(8.617218, -3.418131),
(8.640979, -3.795913),
(8.708442, -4.279803),
(8.731019, -4.635043),
(8.761319, -5.013354),
(8.810208, -5.389704),
(8.868071, -5.704788),
(8.920100, -6.022477),
(8.935623, -6.261832),
(8.924640, -6.288020),
(8.924570, -6.288010),
(8.930942, -6.288216),
(8.924570, -6.288010),
(8.924570, -6.288010)]

plt.plot(map(lambda x: x[0], s),map(lambda x: x[1], s))
plt.show()
