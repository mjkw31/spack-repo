# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissmethyl(RPackage):
	"""Analysing Illumina HumanMethylation BeadChip Data.

	Normalisation, testing for differential variability and differential
	methylation and gene set testing for data from Illumina's Infinium
	HumanMethylation arrays. The normalisation procedure is subset-quantile
	within-array normalisation (SWAN), which allows Infinium I and II type
	probes on a single array to be normalised together. The test for
	differential variability is based on an empirical Bayes version of Levene's
	test. Differential methylation testing is performed using RUV, which can
	adjust for systematic errors of unknown origin in high-dimensional data by
	using negative control probes. Gene ontology analysis is performed by
	taking into account the number of probes per gene on the array, as well as
	taking into account multi-gene associated probes."""

	bioc = "missMethyl"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/missMethyl_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/missMethyl/missMethyl_1.36.0.tar.gz"]

	version("1.36.0", md5="4773cfc60c545bb0a04dac0b6cc0ac4e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicanno-ilm10b4-hg19", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biasedurn", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicmanifest", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-methylumi", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-ruv", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
