# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSingscoreamlmutations(RPackage):
	"""Using singscore to predict mutations in AML from transcriptomic signatures

	This workflow package shows how transcriptomic signatures can be used to infer phenotypes. The workflow begins by showing how the TCGA AML transcriptomic data can be downloaded and processed using the TCGAbiolinks packages. It then shows how samples can be scored using the singscore package and signatures from the MSigDB. Finally, the predictive capacity of scores in the context of predicting a specific mutation in AML is shown.The workflow exhibits the interplay of Bioconductor packages to achieve a gene-set level analysis.
	"""
	
	homepage = "https://github.com/DavisLaboratory/SingscoreAMLMutations"
	bioc = "SingscoreAMLMutations" 
	urls = ["https://www.bioconductor.org/packages/release/workflows/src/contrib/SingscoreAMLMutations_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/workflows/src/contrib/Archive/SingscoreAMLMutations/SingscoreAMLMutations_1.18.0.tar.gz"]

	version("1.18.0", md5="f427ac59e2fa6470b47eb92506f45c9b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dcanr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-singscore", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tcgabiolinks", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))

	# workflow