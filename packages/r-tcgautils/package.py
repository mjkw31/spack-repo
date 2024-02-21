# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgautils(RPackage):
	"""TCGA utility functions for data management

	A suite of helper functions for checking and manipulating TCGA data including data obtained from the curatedTCGAData experiment package. These functions aim to simplify and make working with TCGA data more manageable. Exported functions include those that import data from flat files into Bioconductor objects, convert row annotations, and identifier translation via the GDC API.
	"""
	
	bioc = "TCGAutils" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TCGAutils_1.22.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TCGAutils/TCGAutils_1.22.2.tar.gz"]

	version("1.22.2", md5="0a086006b357c8ed65ee0bfef09cef83")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocbaseutils", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicdatacommons", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-raggedexperiment@1.5.7:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
