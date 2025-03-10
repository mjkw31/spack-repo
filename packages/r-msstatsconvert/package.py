# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatsconvert(RPackage):
	"""Import Data from Various Mass Spectrometry Signal Processing Tools to MSstats Format

	MSstatsConvert provides tools for importing reports of Mass Spectrometry data processing tools into R format suitable for statistical analysis using the MSstats and MSstatsTMT packages.
	"""
	
	bioc = "MSstatsConvert" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MSstatsConvert_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MSstatsConvert/MSstatsConvert_1.12.0.tar.gz"]

	version("1.12.0", md5="1a8b79ba830db5296c2d3f589b398b7f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-log4r", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
