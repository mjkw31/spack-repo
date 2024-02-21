# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbioformats(RPackage):
	"""R interface to Bio-Formats

	An R package which interfaces the OME Bio-Formats Java library to allow reading of proprietary microscopy image data and metadata.
	"""
	
	homepage = "https://github.com/aoles/RBioFormats"
	bioc = "RBioFormats"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RBioFormats_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RBioFormats/RBioFormats_1.2.0.tar.gz"]

	version("1.2.0", md5="cd83827dd164a9b44ba3d0d08fd77b38")

	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-rjava@0.9.6:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("openjdk@1.7:", type=("build", "link", "run"))
