# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgrastr(RPackage):
	"""Rasterize Layers for 'ggplot2'.

	Rasterize only specific layers of a 'ggplot2' plot while simultaneously
	keeping all labels and text in vector format. This allows users to keep
	plots within the reasonable size limit without loosing vector properties of
	the scale-sensitive information."""

	cran = "ggrastr"

	version("1.0.2", md5="c255ae3787f2c84223965f64d0c58e3a")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-cairo@1.5.9:", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-ragg", type=("build", "run"))
