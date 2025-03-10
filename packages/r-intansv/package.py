# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntansv(RPackage):
	"""Integrative analysis of structural variations

	This package provides efficient tools to read and integrate structural variations predicted by popular softwares. Annotation and visulation of structural variations are also implemented in the package.
	"""
	
	bioc = "intansv" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/intansv_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/intansv/intansv_1.42.0.tar.gz"]

	version("1.42.0", md5="d23f9f69f23ab113ea9ac7100cafb3f1")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
