# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdMogene10StV1(RPackage):
	"""Platform Design Info for Affymetrix MoGene-1_0-st-v1

	Platform Design Info for Affymetrix MoGene-1_0-st-v1
	"""
	
	bioc = "pd.mogene.1.0.st.v1" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pd.mogene.1.0.st.v1_3.14.1.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/pd.mogene.1.0.st.v1/pd.mogene.1.0.st.v1_3.14.1.tar.gz"]

	version("3.14.1", md5="c3767385af3b9a120c777adb6d6e3364", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pd.mogene.1.0.st.v1_3.14.1.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

	# annotation