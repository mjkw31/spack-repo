# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDupradar(RPackage):
	"""Assessment of duplication rates in RNA-Seq datasets

	Duplication rate quality control for RNA-Seq datasets.
	"""
	
	homepage = "https://www.bioconductor.org/packages/dupRadar"
	bioc = "dupRadar" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/dupRadar_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/dupRadar/dupRadar_1.32.0.tar.gz"]

	version("1.32.0", md5="306ba6ddb1786eb7ec5e6cb4bc15562e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rsubread@1.14.1:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
