# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensNcbiGrch38(RPackage):
	"""Full genome sequences for Homo sapiens (GRCh38)

	Full genome sequences for Homo sapiens (Human) as provided by NCBI (GRCh38, 2013-12-17) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Hsapiens.NCBI.GRCh38" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Hsapiens.NCBI.GRCh38_1.3.1000.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.NCBI.GRCh38/BSgenome.Hsapiens.NCBI.GRCh38_1.3.1000.tar.gz"]

	version("1.3.1000", md5="733d324b34d34d7da8c4bf38459f4fae", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Hsapiens.NCBI.GRCh38_1.3.1000.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation