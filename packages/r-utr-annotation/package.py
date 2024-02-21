# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtrAnnotation(RPackage):
	"""Annotate Variants in the Untranslated Regions

	A fast, user-friendly tool for annotating potential deleterious variants in the untranslated regions for both human and mouse species. Y Liu, JD Dougherty (2021) <doi:10.1101/2021.06.23.449510>.
	"""
	
	cran = "utr.annotation"

	version("1.0.4", md5="e3d506ff75a13626ea09717c38d269ae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("py-tensorflow@1.14.0:", type=("build", "link", "run"))
