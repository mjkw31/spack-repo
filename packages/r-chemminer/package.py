# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemminer(RPackage):
	"""Cheminformatics Toolkit for R

	ChemmineR is a cheminformatics package for analyzing drug-like small molecule data in R. Its latest version contains functions for efficient processing of large numbers of molecules, physicochemical/structural property predictions, structural similarity searching, classification and clustering of compound libraries with a wide spectrum of algorithms. In addition, it offers visualization functions for compound clustering results and chemical structures.
	"""
	
	homepage = "https://github.com/girke-lab/ChemmineR"
	bioc = "ChemmineR"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ChemmineR_3.54.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ChemmineR/ChemmineR_3.54.0.tar.gz"]

	version("3.54.0", md5="8dd1886811bdc4ac23c24fad60a9b238")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
