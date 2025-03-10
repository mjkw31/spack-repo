# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterSpatial(RPackage):
	"""Save and Load Spatial 'Omics Data to/from File

	Save SpatialExperiment objects and their images into file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
	"""
	
	bioc = "alabaster.spatial" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/alabaster.spatial_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/alabaster.spatial/alabaster.spatial_1.2.0.tar.gz"]

	version("1.2.0", md5="906d73c492ba97e8eda563055c51bbfc")

	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-alabaster-sce", type=("build", "run"))
