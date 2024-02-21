# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTweenr(RPackage):
	"""Interpolate Data for Smooth Animations.

	In order to create smooth animation between states of data, tweening is
	necessary. This package provides a range of functions for creating tweened
	data that can be used as basis for animation. Furthermore it adds a number
	of vectorized interpolaters for common R data types such as numeric, date
	and colour."""

	cran = "tweenr"

	version("2.0.2", md5="df4d4c8b2934f45fd8a838b14716744a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-farver", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-cpp11@0.4.2:", type=("build", "run"))
