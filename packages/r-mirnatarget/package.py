# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirnatarget(RPackage):
	"""gene target tabale of miRNA for human/mouse used for MiRaGE package

	gene target tabale of miRNA for human/mouse used for MiRaGE package
	"""
	
	bioc = "miRNATarget" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/miRNATarget_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/miRNATarget/miRNATarget_1.40.0.tar.gz"]

	version("1.40.0", md5="f1988a96af5f0232abfbe507854d49bb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

	# experiment