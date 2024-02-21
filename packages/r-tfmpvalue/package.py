# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfmpvalue(RPackage):
	"""Efficient and Accurate P-Value Computation for Position Weight Matrices.

	In putative Transcription Factor Binding Sites (TFBSs) identification from
	sequence/alignments, we are interested in the significance of certain match
	score. TFMPvalue provides the accurate calculation of P-value with score
	threshold for Position Weight Matrices, or the score with given P-value.
	This package is an interface to code originally made available by Helene
	Touzet and Jean-Stephane Varre, 2007, Algorithms Mol Biol:2, 15."""

	cran = "TFMPvalue"

	version("0.0.9", md5="8c536eb33fd4acd03fd33af1d5d2bf9f")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
