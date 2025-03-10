# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmirHsMirna(RPackage):
	"""Various databases of microRNA Targets

	Various databases of microRNA Targets
	"""
	
	bioc = "RmiR.Hs.miRNA" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/RmiR.Hs.miRNA_1.0.7.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/RmiR.Hs.miRNA/RmiR.Hs.miRNA_1.0.7.tar.gz"]

	version("1.0.7", md5="4aedac188382447d9907d2617aa2e8e6")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation