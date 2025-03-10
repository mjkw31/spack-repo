# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBuscorrect(RPackage):
	"""Batch Effects Correction with Unknown Subtypes

	High-throughput experimental data are accumulating exponentially in public databases. However, mining valid scientific discoveries from these abundant resources is hampered by technical artifacts and inherent biological heterogeneity. The former are usually termed "batch effects," and the latter is often modelled by "subtypes." The R package BUScorrect fits a Bayesian hierarchical model, the Batch-effects-correction-with-Unknown-Subtypes model (BUS), to correct batch effects in the presence of unknown subtypes. BUS is capable of (a) correcting batch effects explicitly, (b) grouping samples that share similar characteristics into subtypes, (c) identifying features that distinguish subtypes, and (d) enjoying a linear-order computation complexity.
	"""
	
	bioc = "BUScorrect" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BUScorrect_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BUScorrect/BUScorrect_1.20.0.tar.gz"]

	version("1.20.0", md5="6d24bece1ac7982a2a157e5cccc01b99")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
