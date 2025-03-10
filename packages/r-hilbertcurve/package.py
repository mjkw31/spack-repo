# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHilbertcurve(RPackage):
	"""Making 2D Hilbert Curve

	Hilbert curve is a type of space-filling curves that fold one dimensional axis into a two dimensional space, but with still preserves the locality. This package aims to provide an easy and flexible way to visualize data through Hilbert curve.
	"""
	
	homepage = "https://github.com/jokergoo/HilbertCurve"
	bioc = "HilbertCurve" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/HilbertCurve_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/HilbertCurve/HilbertCurve_1.32.0.tar.gz"]

	version("1.32.0", md5="97eed8a87d8bb062c5d0b900823f6bcc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-hilbertvis", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-circlize@0.3.3:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-polylabelr", type=("build", "run"))
