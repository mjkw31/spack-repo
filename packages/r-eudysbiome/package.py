# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REudysbiome(RPackage):
	"""Cartesian plot and contingency test on 16S Microbial data

	eudysbiome a package that permits to annotate the differential genera as harmful/harmless based on their ability to contribute to host diseases (as indicated in literature) or unknown based on their ambiguous genus classification. Further, the package statistically measures the eubiotic (harmless genera increase or harmful genera decrease) or dysbiotic(harmless genera decrease or harmful genera increase) impact of a given treatment or environmental change on the (gut-intestinal, GI) microbiome in comparison to the microbiome of the reference condition.
	"""
	
	bioc = "eudysbiome" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/eudysbiome_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/eudysbiome/eudysbiome_1.32.0.tar.gz"]

	version("1.32.0", md5="76023a8328d58f7d5b783679a08c7ea8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
