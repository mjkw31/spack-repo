# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialomicsoverlay(RPackage):
	"""Spatial Overlay for Omic Data from Nanostring GeoMx Data

	Tools for NanoString Technologies GeoMx Technology. Package to easily graph on top of an OME-TIFF image. Plotting annotations can range from tissue segment to gene expression.
	"""
	
	bioc = "SpatialOmicsOverlay" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SpatialOmicsOverlay_1.2.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SpatialOmicsOverlay/SpatialOmicsOverlay_1.2.1.tar.gz"]

	version("1.2.1", md5="149a968f19aa22b57caca243b3480378")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-scattermore", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-geomxtools", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-rbioformats", type=("build", "run"))
