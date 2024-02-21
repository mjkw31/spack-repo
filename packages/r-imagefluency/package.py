# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImagefluency(RPackage):
	"""Image Statistics Based on Processing Fluency

	Get image statistics based on processing fluency theory. The
    functions provide scores for several basic aesthetic principles that
    facilitate fluent cognitive processing of images: contrast,
    complexity / simplicity, self-similarity, symmetry, and typicality.
    See Mayer & Landwehr (2018) <doi:10.1037/aca0000187> and Mayer & Landwehr
    (2018) <doi:10.31219/osf.io/gtbhw> for the theoretical background of the methods.
	"""
	
	homepage = "https://stm.github.io/imagefluency/"
	cran = "imagefluency" 

	version("0.2.4", md5="0a6348d5a9381780732cdb2ef90a57d2")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-readbitmap", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-openimager", type=("build", "run"))
